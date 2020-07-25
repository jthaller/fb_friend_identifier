# fb_friend_identifier
Given an unseen message from a facebook friend, predict who sent it!

## extract_messages.py
This script loads the JSON files from facebook chat data, then extracts the messages and creates a dict ``messages_dict``, which is imported into the next two scripts

## preprocessing.py
Current not necessary. This vectorizes and lems them, Bag-of-Words style.

## friend_classifier.py
This script trains the NN with MultinomialNB, then predicts ``mystert_message`` and prints the message and the prediction.
