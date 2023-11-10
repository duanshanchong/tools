#将raw格式的灰度转为jpg格式

import sys
from PIL import Image

if len(sys.argv) != 2:
    print('Usage: python script.py <file_path>')
    sys.exit(1)

file_path = sys.argv[1]
file_prefix = file_path.split('.')[0]

with open(file_path, 'rb') as f:
    raw_data = f.read()

width = 1920
height = 1364

try:
    image = Image.frombytes('L', (width, height), raw_data)
    image.save(f'{file_prefix}.jpg')
except ValueError as e:
    print(e)
