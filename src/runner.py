thonimport json
import os
from extractors.tiktok_parser import parse_tiktok_video
from outputs.exporters import export_data

def main():
    video_urls = ["https://www.tiktok.com/@user/video/1234567890"]  # Example TikTok URLs
    results = []

    for url in video_urls:
        try:
            video_data = parse_tiktok_video(url)
            results.append(video_data)
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    export_data(results)

if __name__ == "__main__":
    main()