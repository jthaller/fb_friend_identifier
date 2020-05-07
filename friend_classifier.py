# Starting code was stuff I wrote for codeacademy course where they build a friends_classifier

#Import docs with messages in them


# import sklearn modules here:
# from preprocessing import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from extract_messages import messages_dict

rohan = "Rohan Kadambi"
mike = "Zeran Ji"
thomas = "Thomas Malchodi"
jeremy = "Jeremy Thaller"

# Setting up the combined list of friends' writing samples
friends_docs = messages_dict[rohan]+ messages_dict[mike] + messages_dict[thomas] + messages_dict[jeremy]
# Setting up labels for your three friends
friends_labels = [1]*(len(messages_dict[rohan])) + [2]*(len(messages_dict[mike])) + [3]*(len(messages_dict[thomas])) + [4]*(len(messages_dict[jeremy]))


mystery_message = """
big boi manipulation lol
"""

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

# Change predictions:
predictions = friends_classifier.predict(mystery_vector)
if predictions == [1]:
    predictions = rohan
elif predictions == [2]:
    predictions = mike
elif predictions == [3]:
    predictions = thomas_json1
elif predictions == [4]:
    predictions = jeremy
print(f"prediction: message from {predictions}")


# # Uncomment the print statement:
# print("The postcard was from {}!".format(mystery_friend))
