#note, I'll have to decide how I want to treat emoji's and stickers.
#e.g. "content": "\u00f0\u009f\u009a\u0080" is a rocket sticker, but gets scraped as weird_symbol\x9f\x9a\x80

# thoughts: using str.lower() might actually not help predictions since it
# removes some of the unique stylistic proclivities

#my preprocess text method is pretty clunky. It has to go through everything 3 times
# once to .lower()/remove html links, next to tokenize, and then one more time to lemmatize.
# I'm wondering now if I can combine the first pass with the tokenization

import nltk, re
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter
from nltk.corpus import wordnet as wn
import pickle
import json
# from extract_messages import messages_dict


#deleting linked messages from the array is going to be less efficient
#than just creating a new array (time-wise). You'd have to shift all the 
# array elements down whenever a link popped up.
def preprocess_text(text):
  preprocessed_text = {}
  num_links = dict() #just curious to see how many links each friend sent
  for key, array in text.items():
    print(f'Processing {key} ...')
    num_links[key] = 0
    preprocessed_text[key] = []
    str = ""
    for message in array:
      # print(message)
      if re.search(r'^https?:\/\/.*[\r\n]*', message):
        num_links[key] = num_links[key] + 1
        continue
      cleaned = re.sub(r'\W+', ' ', message).lower()
      str = " ".join((str, cleaned))
  print(f'Number of links: \n {num_links}')
  return preprocessed_text

def preprocess_text_array_version(text):
  preprocessed_text = {}
  num_links = dict() #just curious to see how many links each friend sent
  for key, array in text.items():
    print(f'Processing {key} ...')
    num_links[key] = 0
    preprocessed_text[key] = []
    for message in array:
      if re.search(r'^https?:\/\/.*[\r\n]*', message):
        num_links[key] = num_links[key] + 1
        continue
      cleaned = re.sub(r'\W+', ' ', message).lower()
      tokenized = word_tokenize(cleaned) #turn a many strings to list of words
      normalized = " ".join([normalizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized])
      preprocessed_text[key].append(normalized)

  print(f'Number of links: \n {num_links}')
  return preprocessed_text



normalizer = WordNetLemmatizer()

def get_part_of_speech(word):
  probable_part_of_speech = wn.synsets(word)
  pos_counts = Counter()
  pos_counts["n"] = len(  [ item for item in probable_part_of_speech if item.pos()=="n"]  )
  pos_counts["v"] = len(  [ item for item in probable_part_of_speech if item.pos()=="v"]  )
  pos_counts["a"] = len(  [ item for item in probable_part_of_speech if item.pos()=="a"]  )
  pos_counts["r"] = len(  [ item for item in probable_part_of_speech if item.pos()=="r"]  )
  most_likely_part_of_speech = pos_counts.most_common(1)[0][0]
  return most_likely_part_of_speech

# def preprocess_text(text_dictionary):
#   for messages in text_dictionary:
#     cleaned = re.sub(r'\W+', ' ', text).lower()
#     cleaned = re.sub(r'^https?:\/\/.*[\r\n]*', '', cleaned)
#     tokenized = word_tokenize(cleaned)
#     normalized = " ".join([normalizer.lemmatize(token, get_part_of_speech(token)) for token in tokenized])
#     print(type(normalized))
#   return normalized


with open('fb_messages.pickle', 'rb') as handle:
  unprocessed = pickle.load(handle)
  # preprocessed_text = preprocess_text(unprocessed)
  preprocessed_text = preprocess_text_array_version(unprocessed)

  # save it as a pickle
with open('fb_messages_preprocessed.pickle', 'wb') as handle:
  pickle.dump(preprocessed_text, handle, protocol=pickle.HIGHEST_PROTOCOL)

#save it as a json
with open('fb_messages_preprocessed.json', 'w', encoding='utf-8') as handle:
    json.dump(preprocessed_text, handle)

# print(preprocess_text(messages_dict["Rohan Kadambi"][0:10]))
