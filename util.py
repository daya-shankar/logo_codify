import config
from PIL import Image

def to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def get_image(path):
    conf = config.get()
    im = Image.open(path)
    (width, height) = im.size
    newwidth = int(round(width + (width * conf["svg"]["ratio"]), 0))
    im = im.resize((newwidth, height))
    return im.convert('RGB')