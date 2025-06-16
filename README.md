# AYTWiki - Wiki for Creators! (Please Contribute if you want!)

### AYTWikiDL

```html
<!DOCTYPE html>
<html>
<head>
  <title>Creators</title>
  <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap'>
  <style>
    body { font-family: 'Open Sans', sans-serif; background-color: #f9f9f9; }
    .container { max-width: 800px; margin: 40px auto; padding: 20px; background-color: #fff; border: 1px solid #ddd; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
    .creator { margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #ccc; }
    .creator h2 { margin-top: 0; }
  </style>
</head>
<body>
  <div class='container'>
  </div>
</body>
</html>
```
```bash
#!/bin/bash

# Define the input file name
INPUT_FILE="creators.txt"

# Check if the input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "The file $INPUT_FILE does not exist."
    exit 1
fi

# Create a temporary file to store unique creator names
TMP_FILE="unique_creators.txt"

# Sort the input file and remove duplicates
sort -u "$INPUT_FILE" > "$TMP_FILE"

# Read the temporary file and create an HTML file for each unique creator
while IFS= read -r line; do
    # Replace spaces in the creator's name with hyphens for the file name
    filename="${line// /-}.html"
    
    # Start writing the HTML content
    echo "<!DOCTYPE html>" > "$filename"
    echo "<html>" >> "$filename"
    echo "<head>" >> "$filename"
    echo "  <title>$line</title>" >> "$filename"
    echo "  <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap'>" >> "$filename"
    echo "  <style>" >> "$filename"
    echo "    body { font-family: 'Open Sans', sans-serif; background-color: #f9f9f9; }" >> "$filename"
    echo "    .container { max-width: 800px; margin: 40px auto; padding: 20px; background-color: #fff; border: 1px solid #ddd; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }" >> "$filename"
    echo "  </style>" >> "$filename"
    echo "</head>" >> "$filename"
    echo "<body>" >> "$filename"
    echo "  <div class='container'>" >> "$filename"
    echo "    <h1>$line</h1>" >> "$filename"
    echo "    <p>This is a brief description of $line.</p>" >> "$filename"
    echo "  </div>" >> "$filename"
    echo "</body>" >> "$filename"
    echo "</html>" >> "$filename"
    
    echo "Created $filename"
done < "$TMP_FILE"

# Remove the temporary file
rm "$TMP_FILE"
```

```python
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
```