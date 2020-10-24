# extract messages for preprocessing
## Last time I scraped facebook messages I did so on the html files using bs4
## This time I will scrape JSON files.

import json
import pickle


jeremy = "Jeremy Thaller"
mike = "Zeran Ji"
mike_json1 = "./messages_json/inbox/ZeranJi_XXnwiz4w7g/message_1.json"
mike_json2 = "./messages_json/inbox/ZeranJi_XXnwiz4w7g/message_2.json"

rohan = "Rohan Kadambi"
rohan_json1 = "./messages_json/inbox/RohanKadambi_NQvgRgwgtQ/message_1.json"
rohan_json2 = "./messages_json/inbox/RohanKadambi_NQvgRgwgtQ/message_2.json"
rohan_json3 = "./messages_json/inbox/RohanKadambi_NQvgRgwgtQ/message_3.json"
#there is a message_4.json but I don't think it's a great idea to include messages from 9th grade.
#oldest message in rohan_json3 is from Jan 4 2015

thomas = "Thomas Malchodi"
thomas_json1 = "./messages_json/inbox/ThomasMalchodi_PFq8d7gKmg/message_1.json"

true = True
#Structure: dict{key=string friend: value: [array of strings]}
messages_dict = {"Rohan Kadambi": [], "Zeran Ji": [], "Thomas Malchodi": [], "Jeremy Thaller": []}

def scrape_friend(name, data):
    for block in data["messages"]:
        try:
            if block["sender_name"] == name:
                # print(block["content"])
                temp_mess = block["content"]
                messages_dict[name].append(temp_mess)
        except KeyError:
            pass

# this should probably be in preprocessing but it makes more sense to nest the call in the scraping
# so I'm keeping this method in this script
def fix_encoding_issues(obj):
    for key in obj:
        if isinstance(obj[key], str):
            obj[key] = obj[key].replace('â\x80\x99', "\'") #needed to brute force convert these characters
            obj[key] = obj[key].replace('\u00e2\u0080\u0099', "\'") #needed to brute force convert these characters
            obj[key] = obj[key].encode('latin_1').decode('utf-8')
            obj[key] = obj[key].replace('\n', '') #not sure why this was needed but it was
        elif isinstance(obj[key], list):
            obj[key] = list(map(lambda x: x if type(x) != str else x.encode('latin_1').decode('utf-8'), obj[key]))
        pass
    return obj


#open file, scrape messages and add to messages_dict
#mike
with open(mike_json1) as read_file:
    data = json.load(read_file, object_hook=fix_encoding_issues)
    scrape_friend(jeremy, data)
    scrape_friend(mike, data)

with open(mike_json2) as read_file:
    data = json.load(read_file, object_hook=fix_encoding_issues)
    scrape_friend(jeremy, data)
    scrape_friend(mike, data)
#rohan
with open(rohan_json1, "r") as read_file:
    data = json.load(read_file, object_hook=fix_encoding_issues)
    scrape_friend(jeremy, data)
    scrape_friend(rohan, data)

with open(rohan_json2, "r") as read_file:
    data = json.load(read_file, object_hook=fix_encoding_issues)
    scrape_friend(jeremy, data)
    scrape_friend(rohan, data)

with open(rohan_json3, "r") as read_file:
    data = json.load(read_file, object_hook=fix_encoding_issues)
    scrape_friend(jeremy, data)
    scrape_friend(rohan, data)
#thomas
with open(thomas_json1, "r") as read_file:
    # data = json.load(read_file)
    data = json.load(read_file, object_hook=fix_encoding_issues)
    scrape_friend(jeremy, data)
    scrape_friend(thomas, data)

#save it as a pickle
with open('fb_messages.pickle', 'wb') as handle:
    pickle.dump(messages_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

#double check it worked
with open('fb_messages.pickle', 'rb') as handle:
    b = pickle.load(handle)
    print(b)
print(messages_dict == b)

#save it as a json
with open('fb_messages.json', 'w', encoding='utf-8') as handle:
    json.dump(messages_dict, handle)


# print(f"Rohan: {messages_dict[rohan][-50:]}")
print(f"Thomas: {messages_dict[thomas][-50:]}")
# print(f"Mike: {messages_dict[mike][-50:]}")
# print(f"Jeremy: {messages_dict[jeremy][-3:]}")



# Structure. Note, when a picture is sent, it doesn't say "content: str", it says "photos: [{uri: ,creation_timestamp: }]".
# It's a dict in an array. I'm ignoring pictures, anyway, so this makes it easy.
#
# sample_dict = {
#   "participants": [
#     {
#       "name": "Zeran Ji"
#     },
#     {
#       "name": "Jeremy Thaller"
#     }
#   ],
#   "messages": [
#     {
#       "sender_name": "Jeremy Thaller",
#       "timestamp_ms": 1587763611349,
#       "content": "Lolol",
#       "type": "Generic"
#     },
#     {
#       "sender_name": "Zeran Ji",
#       "timestamp_ms": 1587763579045,
#       "photos": [
#         {
#           "uri": "messages/inbox/ZeranJi_XXnwiz4w7g/photos/90541292_539096823676084_7598840419950002176_n_1226093940931953.png",
#           "creation_timestamp": 1587763578
#         }
#       ],
#       "type": "Generic"
#     }
#       ],
#   "title": "Zeran Ji",
#   "is_still_participant": true,
#   "thread_type": "Regular",
#   "thread_path": "inbox/ZeranJi_XXnwiz4w7g"
# }

# # print(sample_dict["messages"][0]["content"])
# for block in sample_dict["messages"]:
#     if block["sender_name"] == 'Jeremy Thaller':
#         print(block["content"])
