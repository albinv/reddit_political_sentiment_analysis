import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from config import LEFT_TRAINING_DATA, RIGHT_TRAINING_DATA, TRAINING_VALIDATION_SPLIT, MODEL_SAVE_NAME, TOKENIZER_SAVE_NAME
from utils import perform_preprocessing
from random import shuffle
from reddit import get_all_comments_from_subreddit
from file_manager import write_to_file, read_from_file
import matplotlib.pyplot as plt
import numpy as np
MAX_LEN = 500


def fetch_training_comments():
    left_wing_comments = set()
    right_wing_comments = set()

    for data_entry in LEFT_TRAINING_DATA:
        print("\n\nFetching data from reddit for left training: ")
        print(data_entry)
        comments = get_all_comments_from_subreddit(data_entry["name"],
                                                   data_entry["num_posts"],
                                                   data_entry["sort_order"],
                                                   data_entry["all_replies_option"])
        print("Fetched " + str(len(comments)) + " comments for this data set \n")
        for comment in comments:
            left_wing_comments.add(comment[0])

    for data_entry in RIGHT_TRAINING_DATA:
        print("\n\nFetching data from reddit for right training: ")
        print(data_entry)
        comments = get_all_comments_from_subreddit(data_entry["name"],
                                                   data_entry["num_posts"],
                                                   data_entry["sort_order"],
                                                   data_entry["all_replies_option"])
        print("Fetched " + str(len(comments)) + " comments for this data set \n")
        for comment in comments:
            right_wing_comments.add(comment[0])

    return list(left_wing_comments), list(right_wing_comments)


def combine_left_right_views(left, right):
    new_left = []
    for elem in left:
        new_left.append([elem, 0])

    new_right = []
    for elem in right:
        new_right.append([elem, 1])

    combined = new_left+new_right
    # shuffle for more accuracy when doing thr training
    shuffle(combined)

    comments = []
    values = []
    for comment in combined:
        comments.append(comment[0])
        values.append(comment[1])

    return comments, values


def train_model(left_wing_comments, right_wing_comments):
    cleaned_left = perform_preprocessing(left_wing_comments)
    cleaned_right = perform_preprocessing(right_wing_comments)
    comments, labels = combine_left_right_views(cleaned_left, cleaned_right)

    training_size = int(len(comments) * TRAINING_VALIDATION_SPLIT)
    training_comments = comments[0:training_size]
    testing_comments = comments[training_size:]
    training_labels = labels[0:training_size]
    testing_labels = labels[training_size:]

    tokenizer = Tokenizer(oov_token="<OOV>")
    tokenizer.fit_on_texts(training_comments)

    # Training Set
    training_sequences = tokenizer.texts_to_sequences(training_comments)
    training_padded = pad_sequences(training_sequences, maxlen=MAX_LEN, padding='post')

    # Validation Set
    testing_sequences = tokenizer.texts_to_sequences(testing_comments)
    testing_padded = pad_sequences(testing_sequences, maxlen=MAX_LEN, padding='post')

    # Create Model
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(100000, 64, input_length=MAX_LEN),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()

    # Train Model
    history = model.fit(np.array(training_padded), np.array(training_labels), epochs=30,
                        validation_data=(np.array(testing_padded), np.array(testing_labels)), verbose=2, shuffle=True)

    # save model for future use
    model.save(MODEL_SAVE_NAME)
    write_to_file(tokenizer, TOKENIZER_SAVE_NAME)
    plot_training_results_graph(history, "accuracy")
    plot_training_results_graph(history, "loss")


def plot_training_results_graph(history, string):
    plt.plot(history.history[string])
    plt.plot(history.history['val_' + string])
    plt.xlabel("Epochs")
    plt.ylabel(string)
    plt.legend([string, 'val_' + string])
    plt.show()


def get_political_sentiment_prediction(comments_list):
    model = tf.keras.models.load_model(MODEL_SAVE_NAME)
    tokenizer = read_from_file(TOKENIZER_SAVE_NAME)
    new_comments_list = []
    for comment in comments_list:
        cleaned_comment = perform_preprocessing([comment[0]])
        if cleaned_comment != ['']:
            sequences = tokenizer.texts_to_sequences(cleaned_comment)
            padded = pad_sequences(sequences, maxlen=MAX_LEN, padding='post')
            prediction = model.predict(padded)
            new_comments_list.append([comment[1], prediction.tolist()[0][0], comment[0]])
    return new_comments_list
