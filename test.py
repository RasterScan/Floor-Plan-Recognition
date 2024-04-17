import os
import base64
import cv2
import time
import requests
import numpy as np
from tqdm import tqdm


def test(src_dir):
    dst_dir = './result'
    url = 'https://api.rasterscan.com/products/get-floorplan-raw'

    for filename in tqdm(os.listdir(src_dir)):
        files = {'image': open(os.path.join(src_dir, filename), 'rb')}
        r = requests.post(url, files=files)

        json_data = r.json()

        im_bytes1 = base64.b64decode(json_data['image'].split(',')[1])
        im_arr1 = np.frombuffer(im_bytes1, dtype=np.uint8)

        image = cv2.imdecode(im_arr1, flags=cv2.IMREAD_COLOR)

        cv2.imwrite(os.path.join(dst_dir, filename), image)
        time.sleep(2)


if __name__ == '__main__':
    src_dir = './images'
    test(src_dir)

