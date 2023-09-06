import json
import requests
import sys
import os

service1_url = os.environ.get("SERVICE1_URL", "http://service1:8080")

# Parse URL from stdin
web_page = sys.stdin.readline().strip()

# Fetch website content
try:
  response = requests.get(web_page)
  response.raise_for_status()
  text = response.text
except requests.exceptions.RequestException as e:
  print(f"Failed to fetch page {web_page}: {e}")
  sys.exit(1)

data = {
  "hash_func": "md5",
  "message": text
}

try:
  headers = {'Content-Type': 'application/json'}
  response = requests.post(url=service1_url, data=json.dumps(data), headers=headers)
  response.raise_for_status()

  print(response.text)
  print(f"Response code: {response.status_code}")
except requests.exceptions.RequestException as e:
  print(f"Failed to send data to {service1_url}: {e}")
  sys.exit(1)