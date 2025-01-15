import os
import subprocess
import requests
from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)


# Function to fetch Billboard Top 50 songs
def fetch_billboard_top_50():
    url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    songs = []
    for item in soup.select("li.o-chart-results-list__item h3"):
        title = item.get_text(strip=True)
        artist = item.find_next("span").get_text(strip=True)
        songs.append(f"{title} - {artist}")

    return songs[:50]


# Function to download a song using yt-dlp
def download_from_youtube(song_name):
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads", "BillboardSongs")

    if not os.path.exists(downloads_folder):
        os.makedirs(downloads_folder)

    command = [
        "yt-dlp",
        f"ytsearch1:{song_name}",
        "-x",
        "--audio-format", "mp3",
        "-o", f"{downloads_folder}/%(title)s.%(ext)s"
    ]

    subprocess.run(command)


# Route: Homepage
@app.route("/")
def home():
    songs = fetch_billboard_top_50()
    return render_template("index.html", songs=songs)


# Route: Download Selected Songs
@app.route("/download", methods=["POST"])
def download():
    data = request.json
    selected_songs = data.get("songs", [])

    for song in selected_songs:
        download_from_youtube(song)

    return jsonify({"message": f"Downloaded {len(selected_songs)} songs to your Downloads/BillboardSongs folder!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

