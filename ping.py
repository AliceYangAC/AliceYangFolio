import requests

URLS = [
    "https://aliceyangfolio.onrender.com/"  # Replace with your actual Render URL
]

for url in URLS:
    try:
        response = requests.get(url, timeout=10)
        print(f"Pinged {url} — Status: {response.status_code}")
    except Exception as e:
        print(f"Error pinging {url}: {e}")
