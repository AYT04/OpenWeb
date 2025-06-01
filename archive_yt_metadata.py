import os
import json
from googleapiclient.discovery import build

# Replace with your API key
API_KEY = ""

# Open the file containing the YouTube URLs
with open("videos.txt", "r") as f:
    youtube_urls = [line.strip() for line in f.readlines()]

# Create the YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Open the output file
with open("metadata.txt", "w") as output_file:
    for url in youtube_urls:
        # Extract the video ID from the URL
        video_id = url.split("v=")[1] if "v=" in url else url.split("/")[-1]

        # Make the API request to fetch the video metadata
        request = youtube.videos().list(
            part="id,snippet",
            id=video_id
        )
        response = request.execute()

        # Check if the response contains any items
        if response.get("items"):
            # Extract the metadata from the response
            metadata = response["items"][0]["snippet"]
            channel_name = metadata["channelTitle"]
            description = metadata["description"]

            # Write the metadata to the output file
            output_file.write(f"Video ID: {video_id}\n")
            output_file.write(f"Channel Name: {channel_name}\n")
            output_file.write(f"Description: {description}\n\n")
        else:
            output_file.write(f"Video ID: {video_id} - Not found\n\n")
