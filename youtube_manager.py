import json



# Load Data
def load_data():
    videos = []
    pass
# 1: List all YouTube videos
def list_all_video(videos):
    pass
# 2: Add a new YouTube video
def add_video(videos):
    pass
# 3: Update YouTube video details
def update_video_details(videos):
    pass
# 4: Delete a YouTube video
def delete_video(videos):
    pass



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