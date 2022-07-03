import json
import time
import os
import csv

user_feed_items = []
header = ['shortcode',
          'account',
          'url',
          'duration',
          'title',
          'published_datetime',
          'Thumbnail',
          'comment',
          'like',
          'video_play_count',
          'video_view_count',
          'category']

folderpath = 'C://narasi-project//insta-new-update//input//narasi//'
list_response  = os.listdir(folderpath)
print(list_response)

for x in list_response:
    filename = os.path.join(folderpath,x)
    timestr = time.strftime("%Y%m%d-%H%M%S")

    directory = os.path.join('./data',timestr)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, 'r',encoding="utf-8") as j:
        output_response = json.loads(j.read())

    feed_item = output_response["items"]

    nama_file = feed_item[0]['media']["user"]["username"] + ".csv"

    for i in range(len(feed_item)):
        user_feed_items.append(feed_item[i]['media'])

    with open(os.path.join(directory,nama_file), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for item in user_feed_items:
            writer.writerow([
                    item["code"],
                    item["user"]["username"],
                    'https://www.instagram.com/reel/' + item["code"] + "/",
                    item["video_duration"],
                    item["caption"]["text"],
                    time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item["taken_at"])),
                    item["video_versions"][1]["url"],
                    item["comment_count"],
                    item["like_count"],
                    item["play_count"],
                    item["view_count"],
                    "Reels"
                ])

