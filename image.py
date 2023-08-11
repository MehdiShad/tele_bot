from PIL import Image, ImageDraw, ImageFont
from api import invitation_templates
# font = ImageFont.truetype(size=75)
bg = Image.open('temp/VforVendeta.jpg')
white = (255, 255, 225)
def test_image(api):
    # vendeta = Image.open('temp/images.png')#.resize((100, 100))
    # bg.paste(vendeta, (0, 0), vendeta)  
    draw = ImageDraw.Draw(bg)
    draw.text((10, 150), 'shad hastam', fill=white)
    draw.text((10, 135), f"all_templates:{api['all_templates']}", fill=white)
    # bg.show()
    bg.save('image.png')

# test_image(invitation_templates())