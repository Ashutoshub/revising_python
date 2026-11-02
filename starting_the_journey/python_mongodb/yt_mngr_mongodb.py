from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb+srv://youtubepy:Ashu@youtube.sz7brr4.mongodb.net/")
db = client["ytmanager"]
videos_collection = db["videos"]
print(videos_collection)

def list_videos():
    videos = videos_collection.find()
    if not videos:
        print("No videos found.")
    else:
        for video in videos:
            print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})

def update_video(id, new_name, new_time):
    videos_collection.update_one({"_id": id}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(id):
    videos_collection.delete_one({"_id": id})

def main():
    while True:
        print("\n YouTube Manager | choose an option:")
        print("1. list all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)
            case "3":
                id = input("Enter the video ID to update: ")
                id = ObjectId(id)
                new_name = input("Enter new video name: ")
                new_time = input("Enter new video time: ")
                update_video(id, new_name, new_time)
            case "4":
                id = input("Enter the video ID to delete: ")
                id = ObjectId(id)   
                delete_video(id)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()