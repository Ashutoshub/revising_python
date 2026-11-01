
import json

def list_videos(video):
    print("\n")
    print("*" * 70)
    for i, vid in enumerate(video, start=1):

        print(f"{i}.{vid['name']}, duration: {vid['time']}")
    print("\n")
    print("*" * 70)

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            data = json.load(file)
           
            return data
    except FileNotFoundError:
        return [] 

def save_data_helper(video):
    with open("youtube.txt", "w") as file:
        json.dump(video, file)

def add_video(video):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    video.append({"name": name, "time": time})
    save_data_helper(video)

def update_video(video):
    list_videos(video)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(video):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")
        video[index - 1] = {"name": name, "time": time}
        save_data_helper(video)
    else:
        print("Invalid video number.")

def delete_video(video):
    list_videos(video)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(video):
        del video[index - 1]
        save_data_helper(video)
    else:
        print("Invalid video number.")
def main():
    video = load_data()
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
                list_videos(video)
            case "2":
                add_video(video)
            case "3":
                update_video(video)
            case "4":
                delete_video(video)
            case "5":
                print("Exiting the YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
