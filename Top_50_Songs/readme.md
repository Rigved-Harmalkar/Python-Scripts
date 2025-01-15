# Billboard Top 50 Songs Flask App

This Flask application fetches the top 50 songs from the **Billboard Hot 100** and allows the user to download them in `.mp3` format. The app also supports saving a list of the top songs to a file with a timestamp (e.g., `billboard_songs_Feb_2025.json`).

## Features

- Displays the top 50 songs on the Billboard Hot 100 chart.
- Allows users to download songs directly.
- Automatically saves the top 50 songs to a file each month (with a timestamp).

## Requirements

- Python 3.6+
- `requests` library for fetching data from Billboard.
- `BeautifulSoup` for parsing the HTML page.
- `yt-dlp` for downloading songs from YouTube.

## Installation

### Step 1: Clone the repository
Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/billboard-top-50-flask-app.git
