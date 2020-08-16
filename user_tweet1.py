import tweepy
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

key = ""
secretKey = ""
token = ""
tokenSecret = ""

auth = tweepy.OAuthHandler(key,secretKey)
auth.set_access_token(token,tokenSecret)
api = tweepy.API(auth)

pos_list= open("./kata_positif.txt","r")
pos_kata = pos_list.readlines()
neg_list= open("./kata_negatif.txt","r")
neg_kata = neg_list.readlines()

def search(key,date = "2020-07-27"):
    search_words = key
    date_since = date
    new_search = search_words + " -filter:retweets"

    tweets = tweepy.Cursor(api.search, q=new_search, lang="id", since=date_since).items(1000)

    items = []
    for tweet in tweets:
        item = []
        item.append (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
        items.append(item)
    hasil = pd.DataFrame(data=items, columns=['tweet'])

    s=[]
    a=[]
    for item in items:
        count_p = 0
        count_n = 0
        for kata_pos in pos_kata:
            if kata_pos.strip() in item[0]:
                count_p +=1
        for kata_neg in neg_kata:
            if kata_neg.strip() in item[0]:
                count_n +=1
        h = count_p-count_n
        if h==0:
            rs = "Netral"
        elif h>0:
            rs = "Positif"
        elif h<0:
            rs = "Negatif"
        s.append(h)
        a.append(rs)
    hasil["kesimpulan"] = a
    hasil["value"] = s
    return hasil
def asd(hasil,nama):
    a=[]
    a.append(nama)
    rata = np.average(hasil["value"])
    a.append(rata)
    a.append(np.median(hasil["value"]))
    rs=""
    if rata==0:
        rs = "Netral"
    elif rata>0:
        rs = "Positif"
    elif rata<0:
        rs = "Negatif"
    a.append(rs)
    return a

s=[]
hasil = search("Jouska")
s.append(asd(hasil,"Jouska"))
hasil = search("Anies")
s.append(asd(hasil,"Anies"))
hasil = search("Terawan")
s.append(asd(hasil,"Terawan"))

result = pd.DataFrame(data=s, columns=['Nama','Rata-rata','Median','Kesimpulan'])

print(result)