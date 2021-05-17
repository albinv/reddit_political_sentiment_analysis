# reddit_political_sentiment_analysis


Sentiment analysis involves looking at public comments (such as tweets) to determine the mood (such as happy, sad, angry, and so on). Some very sophisticated apps exist that can do this in real time (ie. the mood right now). See en.wikipedia.org/wiki/Sentiment_analysis for an overview. Machine learning code libraries exist that can help to detect emotional sentiment, but not much work has been done on detecting political sentiment.


The aim of this project is to use data mining, natural language processing and machine learning to examine public comments for sentiment over longer periods of time. To create a reddit bot that can trawl specified subreddits and extract comments (in an anonymised form), analyse those comments for sentiment, and build up a visualisation of that sentiment. One of the things we are interested in is whether we can categorise text as “left-wing” or “right-wing” in a political sense.

The second phase of the project will involve visualising the sentiment in an interesting way, or even allowing the user to navigate through the data in some kind of semantic web of sentiment. This should be visually appealing and user friendly.

## Installation:


Installation can be done through the makefile

- To install the dependencies: run `make install_dependencies`
- To uninstall the dependencies run `make uninstall_dependancies`
- To start the back-end server, first install the dependencies and then run `make start_back_end`
- To start the front-end server run `make start_front_end`