# display_events.py
import epd7in3f
import time
from PIL import Image, ImageDraw, ImageFont
from calendar_parser import get_events

def display_events(events):
    epd = epd7in3f.EPD()
    epd.init()
    epd.Clear()
    image = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)
    y = 10
    for event in events:
        draw.text((10, y), f"{event['start'].strftime('%Y-%m-%d %H:%M')} - {event['summary']}", font=font, fill=0)
        y += 30
    epd.display(epd.getbuffer(image))
    epd.sleep()

events = get_events('https://raw.githubusercontent.com/Vomxy/fuzzy-octo-doodle/refs/heads/main/Essentials-2025-06-27.ics')  # Replace with your ICS file URL
display_events(events)
