#Jeremy Thaller May 6, 2020
# Given an unseen message, the script predicts who sent the message.
# I used personal fb chats as training data, and I used messages from group chats as testing data  
# The only thing needed to be edited is the mystery_message string.

#Import docs with messages in them
from extract_messages import messages_dict

# import sklearn modules here:
# from preprocessing import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

rohan = "Rohan Kadambi"
mike = "Zeran Ji"
thomas = "Thomas Malchodi"
jeremy = "Jeremy Thaller"

# Setting up the combined list of friends' writing samples
friends_docs = messages_dict[rohan]+ messages_dict[mike] + messages_dict[thomas] + messages_dict[jeremy]
# Setting up labels for the 4 friends
friends_labels = [1]*(len(messages_dict[rohan])) + [2]*(len(messages_dict[mike])) + [3]*(len(messages_dict[thomas])) + [4]*(len(messages_dict[jeremy]))

#never before seen message for which the NN will predict the sender
mystery_message = "big boi manipulation lol"


# Create bow_vectorizer:
bow_vectorizer = CountVectorizer()
# Define friends_vectors:
friends_vectors = bow_vectorizer.fit_transform(friends_docs)
# Define mystery_vector:
mystery_vector = bow_vectorizer.transform([mystery_message])

# Define friends_classifier:
friends_classifier = MultinomialNB()

# Train the classifier:
friends_classifier.fit(friends_vectors, friends_labels)

# Change prediction back to a name:
predictions = friends_classifier.predict(mystery_vector)
if predictions == [1]:
    predictions = rohan
elif predictions == [2]:
    predictions = mike
elif predictions == [3]:
    predictions = thomas_json1
elif predictions == [4]:
    predictions = jeremy
print(f"Test message for prediction: \"{mystery_message}\"")
print(f"Prediction: Message sent from {predictions}")


# # Uncomment the print statement:
# print("The postcard was from {}!".format(mystery_friend))
