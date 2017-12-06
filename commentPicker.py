import json
import requests

# post id
print("Please enter the post number: ")
post_id = input()
# token
print("Please enter the token from facebook: ")
token = input()
# save the name which need to be selected
name_list = []
print('Please enter the name you want, press enter to continue: ')
while True:
    index = input()
    if index not in name_list and index!="":
         name_list.append(index)
    elif index == '':
        print("Your list is as below: ")
        print(name_list)
        break
    else:
        print("You already input this name")
# send the API requests to FB
res = requests.get("https://graph.facebook.com/v2.8/{}/comments?limit=1000&access_token={}".format(post_id, token))
# Loop through the comments and print the comment id
print("The comment id you want are as below: ")
while "paging" in res.json():
    for comment in res.json()["data"]:
        name = comment['from']['name']
        if name in name_list:
            print(comment['id'])
    if "next" in res.json()["paging"]:
        res = requests.get(res.json()["paging"]["next"])
    else:
        break
