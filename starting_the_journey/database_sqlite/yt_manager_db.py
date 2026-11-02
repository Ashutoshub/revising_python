import sqlite3
conn = sqlite3.connect('yt_videos.db')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
 ''')

def list_videos():
    cur.execute("SELECT * FROM videos")
    videos = cur.fetchall()
    if not videos:
        print("No videos found.")
    else:
        for video in videos:
            print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")

def add_video(name, time):
    cur.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(id, name, time):
    cur.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id))
    conn.commit()

def delete_video(id):
    cur.execute("DELETE FROM videos WHERE id = ?", (id,))
    conn.commit()

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
                name = input("Enter new video name: ")
                time = input("Enter new video time: ")
                update_video(id, name, time)
            case "4":
                id = input("Enter the video ID to delete: ")
                delete_video(id)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")
    conn.close()
if __name__ == "__main__":
    main()