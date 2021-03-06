import os

import requests

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
r = requests.get(IMAGE_URL, stream=True)  # stream loading
os.makedirs('./img/', exist_ok=True)

with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
