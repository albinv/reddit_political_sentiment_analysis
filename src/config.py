CLIENT_ID = "jshyL9CMgH5nEg"
CLIENT_SECRET = "WEHm5M9WLUd7PzjzydlUUKiHSH1vnw"
USER_AGENT = "sentiment_analysis by u/albinv1"

DATA_PATH = "../data/"

# the split between training data and the validation data, 0.8 means 80% for training
TRAINING_VALIDATION_SPLIT = 0.8

MODEL_SAVE_NAME = "political_sentiment_model"
TOKENIZER_SAVE_NAME = "tokenizer"

# Add as many subreddits to train model to recognise left_wing commenter's
LEFT_TRAINING_DATA = [
    {"name": "labouruk", "num_posts": 200, "sort_order": "top", "all_replies_option": False},  # UK
    {"name": "democrats", "num_posts": 200, "sort_order": "top", "all_replies_option": False},  # US
    {"name": "ndp", "num_posts": 200, "sort_order": "top", "all_replies_option": False}  # Canada
]

# Add as many subreddits to train model to recognise right_wing commenter's
RIGHT_TRAINING_DATA = [
    {"name": "tories", "num_posts": 200, "sort_order": "top", "all_replies_option": False},  # UK
    {"name": "Republican", "num_posts": 200, "sort_order": "top", "all_replies_option": False},  # US
    {"name": "CanadianConservative", "num_posts": 200, "sort_order": "top", "all_replies_option": False}  # Canada
]

# The words that don't add much meaning to a sentence...
NLTK_STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll",
                  "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's",
                  'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs',
                  'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is',
                  'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
                  'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
                  'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
                  'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
                  'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
                  'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
                  'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",
                  'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn',
                  "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't",
                  'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn',
                  "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

SAFE_KEY = b'XV2PzWestOEz1w2kE2uKeUBBDObKb39IEV9FNY5kQB4='
