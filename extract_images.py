import requests
from bs4 import BeautifulSoup

# URL of the Tumblr post
url = "https://17th-angel.tumblr.com/post/40125138257/shinji-ikari-raising-project-game-with-the-scenes"

# Fetch the page
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch the page. Status Code: {response.status_code}")
    exit()

# Parse the page
soup = BeautifulSoup(response.text, "html.parser")

# Find all image tags
image_urls = []
for img in soup.find_all("img"):
    img_url = img.get("src")
    if img_url:
        image_urls.append(img_url)

# Print the extracted image URLs
for idx, img_url in enumerate(image_urls, start=1):
    print(f"Image {idx}: {img_url}")