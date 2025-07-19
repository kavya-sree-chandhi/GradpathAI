import requests
from pymongo import MongoClient

# ====== CONFIGURATION ======
API_KEY = "*****"    # Replace with your actual key!
queries = ["machine learning tutorial", "deep learning", "AI interview", "NLP tutorial", "data science project", "neural networks lecture", "computer vision crash course", "python for AI", "artificial intelligence basics", "transformer models explained"]  # You can add more queries!

# ====== MONGODB SETUP ======
client = MongoClient("mongodb://localhost:27017/")
db = client["gradpath_ai"]
videos_collection = db.videos

# ====== FUNCTION TO FETCH AND SAVE VIDEOS ======
def fetch_and_save_videos(search_query):
    url = (
        "https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&q={search_query}&type=video&maxResults=50&key={API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    
    for item in data.get("items", []):
        video = {
            "title": item['snippet']['title'],
            "description": item['snippet']['description'],
            "channel": item['snippet']['channelTitle'],
            "publishedAt": item['snippet']['publishedAt'],
            "url": f"https://youtube.com/watch?v={item['id']['videoId']}",
            "tags": [search_query]
        }
        videos_collection.insert_one(video)
        print("Inserted:", video["title"])

# ====== MAIN INGESTION LOOP ======
if __name__ == "__main__":
    for q in queries:
        print(f"\nFetching videos for: {q}")
        fetch_and_save_videos(q)
    print("\nData ingestion complete!")

