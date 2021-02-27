# fb_friend_identifier
Given an unseen message from a facebook friend, predict who sent it!
<img src="https://github.com/jthaller/fb_friend_identifier/blob/master/readme_pic.jpg" width="800">

## extract_messages.py

This script loads the JSON files from facebook chat data, then extracts the messages and creates a dict ``messages_dict``, which is then saved as a pickle file named `fb_messages.pickle`. The pickle file is a dictionary of the form key='Sender', value=[message 1, message 2, ...]

## preprocessing.py

This vectorizes and lems them. Then, the dictionary is saved as a pickle file named `fb_messages_preprocessed.pickle`.

## friend_classifier.py

This script trains the classifier with MultinomialNB, then predicts ``mystery_message`` and prints the message and the prediction.

## Performance metrics

The classifier performs with around 55% accuracy on the test set, and similarly when tested with 5-fold cross validation. This score isn't amazing, but it is better than the 25% score that would be expected if it were working by random chance. I think that performance would be improved if the tokenization didn't split up contracted words and instead left them as they are uniquely written by each friend. Additionally, counting punctuation and adding this parameter to the NB classification parameters would likely improve performance. Countvectorization was a better predictor than tf-idf, and converting all the letters to lowercase also hurt performance slightly.
