from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["gradpath_ai"]
videos = db.videos

# Print all videos with the tag "deep learning"
for video in videos.find({"tags": "deep learning"}):
    print(video)
