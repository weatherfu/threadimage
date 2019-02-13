from PIL import Image
from resizeimage import resizeimage
with open('britfeel.jpg', 'r+b') as britfeelfile:
    with Image.open(britfeelfile) as britfeelimage:
        size = britfeelimage.size
        height = size[1]
        for number in range(0, 10):
            britfeelimage = resizeimage.resize_height(britfeelimage, height - number)
            britfeelimage.save('britfeel_' + str(number) + '.jpg', britfeelimage.format)
