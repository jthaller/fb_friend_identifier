#Jeremy Thaller May 6, 2020
# Given an unseen message, the script predicts who sent the message.
# I used personal fb chats as training data, and I used messages from group chats as testing data
# The only thing needed to be edited is the mystery_message string.

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split
import pickle
import json
from preprocessing import preprocess_text, get_part_of_speech
from sklearn.model_selection import cross_val_score

# with open('fb_messages_preprocessed.pickle', 'wb') as gerkin:
#     messages_dict = pickle.load(gerkin)

with open('fb_messages_preprocessed.json') as read_file:
    messages_dict = json.load(read_file)

rohan = "Rohan Kadambi"
mike = "Zeran Ji"
thomas = "Thomas Malchodi"
jeremy = "Jeremy Thaller"

# Setting up the combined list of friends' writing samples
friends_docs = messages_dict[rohan] + messages_dict[mike] + messages_dict[thomas] + messages_dict[jeremy]

# Setting up labels for the 4 friends
friends_labels = [1]*(len(messages_dict[rohan])) + [2]*(len(messages_dict[mike])) + [3]*(len(messages_dict[thomas])) + [4]*(len(messages_dict[jeremy]))

# Create bow_vectorizer:
# {key=word: val=frequency)
bow_vectorizer = CountVectorizer()

# Define friends_vectors:
friends_vectors = bow_vectorizer.fit_transform(friends_docs)

# Define friends_classifier:
friends_classifier = MultinomialNB()

# train test split
X_train, X_test, y_train, y_test = train_test_split(friends_vectors, friends_labels, test_size=0.33, random_state=42)

#never before seen message for which the NN will predict the sender
# mystery_message = "big boi manipulation lol"
mystery_message = '''lmao well since you're up, ill update and say i will never not buy anything off of amazon ever again literally found the same shoe for 40 dollars less than their sale?'''
mystery_message = preprocess_text(mystery_message)

# Define mystery_vector:
mystery_vector = bow_vectorizer.transform([mystery_message])

# Train the classifier:
# friends_classifier.fit(friends_vectors, friends_labels)
friends_classifier.fit(X_train, y_train)


# Change prediction back to a name:
predictions = friends_classifier.predict(mystery_vector)
confidence = friends_classifier.predict_proba(mystery_vector) #technically the probability.
score = friends_classifier.score(X_test, y_test)
score1 = friends_classifier.score(X_train, y_train)

# cv_score = cross_val_score(friends_classifier, friends_vectors, friends_labels, cv=5 )
# print(cv_score)

if predictions == [1]:
    predictions = rohan
elif predictions == [2]:
    predictions = mike
elif predictions == [3]:
    predictions = thomas
elif predictions == [4]:
    predictions = jeremy

print(f"Training Accuracy: {score1}\n Testing Accuracy: {score}\n")
print(f"Test message for prediction: \n \"{mystery_message}\" \n")
print(f"Prediction: Message sent from: \n {predictions}")
print(f"\nconfidence: \n {confidence}")
