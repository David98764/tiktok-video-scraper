thonimport requests
from bs4 import BeautifulSoup

def parse_tiktok_video(url):
    """Scrape video data from TikTok URL."""
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch video at {url}")

    soup = BeautifulSoup(response.text, "html.parser")
    video_data = {}

    # Extracting video metadata (simplified)
    video_data["authorMeta"] = {
        "name": soup.find("h1", {"class": "author-name"}).text,
        "avatar": soup.find("img", {"class": "author-avatar"})["src"]
    }
    video_data["text"] = soup.find("p", {"class": "video-caption"}).text
    video_data["diggCount"] = int(soup.find("span", {"class": "like-count"}).text)
    video_data["shareCount"] = int(soup.find("span", {"class": "share-count"}).text)
    video_data["playCount"] = int(soup.find("span", {"class": "play-count"}).text)
    video_data["musicMeta"] = {
        "musicName": soup.find("p", {"class": "music-name"}).text,
        "musicAuthor": soup.find("p", {"class": "music-author"}).text
    }

    return video_data