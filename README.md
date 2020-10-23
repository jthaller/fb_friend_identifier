# fb_friend_identifier
Given an unseen message from a facebook friend, predict who sent it!
<img src="https://github.com/jthaller/fb_friend_identifier/blob/master/readme_pic.jpg" width="800">

## extract_messages.py
This script loads the JSON files from facebook chat data, then extracts the messages and creates a dict ``messages_dict``, which is then saved as a pickle file named `fb_messages.pickle`. The pickle file is a dictionary of the form key='Sender', value=[message 1, message 2, ...]

## preprocessing.py
This vectorizes and lems them. Then, the dictionary is saved as a pickle file named `fb_messages_preprocessed.pickle`.

## friend_classifier.py
This script trains the NN with MultinomialNB, then predicts ``mystert_message`` and prints the message and the prediction.
