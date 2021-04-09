from sentiment_analysis import fetch_training_comments, train_model
from file_manager import write_to_file, read_from_file
from utils import *
from endpoints import start_server


# 1. Get Training Data
# left, right = fetch_training_comments()
# write_to_file(left, "left_wing_training")
# write_to_file(right, "right_wing_training")

# 2. Create Model
# train_model(read_from_file("left_wing_training"), read_from_file("right_wing_training"))

# 3. Start Webpage
start_server()
