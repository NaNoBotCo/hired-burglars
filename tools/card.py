"""Share card, 1200x630: a house at night with a lit window, a van, and the title."""
import pathlib
from PIL import Image, ImageDraw, ImageFont

out = pathlib.Path(__file__).resolve().parent.parent / "docs" / "card.jpg"
W, H = 1200, 630
G, INK, GOLD, RED, WOOD, BLUE, NIGHT = (18, 20, 25), (236, 234, 228), (240, 194, 60), (226, 104, 92), (176, 122, 76), (125, 162, 230), (27, 34, 56)
img = Image.new("RGB", (W, H), G)
d = ImageDraw.Draw(img)
d.rectangle([640, 0, W, H], fill=NIGHT)
d.polygon([(700, 300), (900, 160), (1100, 300)], fill=WOOD, outline=INK, width=5)
d.rectangle([715, 300, 1085, 520], fill=(27, 30, 37), outline=INK, width=5)
d.rectangle([760, 400, 820, 520], fill=WOOD, outline=INK, width=4)
d.rectangle([960, 340, 1040, 400], fill=GOLD, outline=INK, width=4)
d.line([(1000, 340), (1000, 400)], fill=INK, width=3); d.line([(960, 370), (1040, 370)], fill=INK, width=3)
d.ellipse([990, 348, 1012, 370], fill=(18, 20, 25))
d.rectangle([1010, 520 - 10, 1180, 590], fill=BLUE, outline=INK, width=4)
d.ellipse([1030, 575, 1060, 605], fill=INK); d.ellipse([1130, 575, 1160, 605], fill=INK)
F = "/System/Library/Fonts/Supplemental/"
big = ImageFont.truetype(F + "Georgia Bold.ttf", 92)
th = ImageFont.truetype(F + "Tahoma Bold.ttf", 56)
small = ImageFont.truetype(F + "Courier New Bold.ttf", 28)
thsmall = ImageFont.truetype(F + "Tahoma.ttf", 30)
d.text((64, 110), "SECURITY WORK, AS TOYS", font=small, fill=GOLD)
d.text((60, 160), "Hired", font=big, fill=INK)
d.text((60, 255), "Burglars", font=big, fill=INK)
d.text((64, 370), "ขโมยรับจ้าง", font=th, fill=(163, 167, 176))
d.text((64, 460), "Paid to break in, with your say-so.", font=small, fill=INK)
d.text((64, 500), "งัดบ้าน โดยคุณอนุญาต", font=thsmall, fill=(163, 167, 176))
d.text((64, 570), "nanobotco.github.io/hired-burglars", font=small, fill=GOLD)
img.save(out, quality=88)
print(out)
