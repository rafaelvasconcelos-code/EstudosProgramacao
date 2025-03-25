from pytubefix import YouTube
import os

def download_youtube_video(url, output_path=None):
    try:
        # Create a YouTube object with the video URL
        yt = YouTube(url)

        # Display video details
        print(f"Title: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"Length: {yt.length // 60} minutes {yt.length % 60} seconds")
        print(f"Views: {yt.views}")

        # Get the highest resolution stream (video + audio)
        video_stream = yt.streams.get_highest_resolution()
        audio_stream = yt.streams.get_audio_only()

        # Set default output path to current directory if none provided
        if output_path is None:
            output_path = os.getcwd()  # Current working directory
        else:
            # Ensure the output directory exists
            os.makedirs(output_path, exist_ok=True)

        # Download the video
        print("Downloading VIDEO...")
        #video_stream.download(output_path)
        print(f"Download completed! Video saved to: {os.path.join(output_path, f'{yt.title}.mp4')}")

        print("Downloading AUDIO...")
        audio_stream.download(output_path)
        print(f"Download completed! AUDIO saved to: {os.path.join(output_path, f'{yt.title}.mp3')}")        



    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Get user input
    video_url = "hhttps://www.youtube.com/watch?v=WykOxY55yw0"

    # Optional custom path
    save_path = input("Enter the download path (or press Enter for current directory): ").strip()
    if save_path == "":
        save_path = None

    # Download the video
    download_youtube_video(video_url, save_path)

if __name__ == "__main__":
    main()