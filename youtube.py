# Import the necessary modules and classes
from pytube import YouTube

# Set the URL of the YouTube video you want to download
video_url = 'YOUTUBE_URL'

# Create a YouTube object and get the video
video = YouTube(video_url)

# Download the video in the highest available resolution
video.streams.get_highest_resolution().download()
