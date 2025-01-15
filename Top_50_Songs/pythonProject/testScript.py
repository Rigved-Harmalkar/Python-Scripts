import requests
from bs4 import BeautifulSoup
import os
import subprocess


def fetch_billboard_top_50():
    url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

    # Parse the song titles and artists
    songs = []

    for item in soup.select("li.o-chart-results-list__item h3"):
        title = item.get_text(strip=True)
        artist = item.find_next("span").get_text(strip=True)
        songs.append(f"{title} {artist}")

    return songs[:50]


# Step 2: Search and Download Songs from YouTube
def download_from_youtube(song_name, download_path="./downloads"):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Use yt-dlp to download
    command = [
        "yt-dlp",
        f"ytsearch1:{song_name}",  # Search for the song
        "-x",  # Extract audio
        "--audio-format", "mp3",  # Save as mp3
        "-o", f"{download_path}/%(title)s.%(ext)s"  # Save format
    ]

    subprocess.run(command)




# def main():
#     songs = fetch_billboard_top_50()
#     print(f"Found {len(songs)} songs.")
#
#     for song in songs:
#         print(f"Downloading: {song}")
#         try:
#             download_from_youtube(song)
#         except Exception as e:
#             print(f"Failed to download {song}: {e}")
#
#
# if __name__ == "__main__":
#     main()