import sys
from PIL import Image

images = [Image.open(x) for x in ['scatter.png','data.png']]

widths, heights = zip(*(i.size for i in images))

height = sum(heights)
new_im = new_im = Image.new('RGB', (widths[0], height))

new_im.paste(images[0], (0,0))
new_im.paste(images[1],(0,heights[0]))

new_im.save('combined.png')
