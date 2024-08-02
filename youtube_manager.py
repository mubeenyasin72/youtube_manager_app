import json



# Load Data
def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found")
        return []
    
# Save Data Helper
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

# 1: List all YouTube videos
def list_all_video(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos,start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']} ")
    print("*" * 70)
    
# 2: Add a new YouTube video
def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("Video added successfully")
    
# 3: Update YouTube video details
def update_video_details(videos):
    list_all_video(videos)
    index = int(input("Enter the index of the video to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new name of the video:")
        time = input("Enter the new time of the video:")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print("Video details updated successfully")
    else:
        print("Invalid index")

# 4: Delete a YouTube video
def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the index of the video to delete: "))
    
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("Video deleted successfully")
    else:
        print("Invalid index")
        
        
        



def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_all_video(videos)
        elif choice == "2":
            add_video(videos)
        elif choice == "3":
            update_video_details(videos)
        elif choice == "4":
            delete_video(videos)
        elif choice == "5":
            print("Exiting the app")
            break
        else:
            print("Invalid choice")
            
    

if __name__ == "__main__":
    main()