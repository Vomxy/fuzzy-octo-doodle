# calendar_parser.py
import requests
from icalendar import Calendar
import datetime

def get_events(ics_url):
    response = requests.get(ics_url)
    cal = Calendar.from_ical(response.text)
    events = []
    for component in cal.walk():
        if component.name == "VEVENT":
            summary = component.get('summary').to_ical().decode('utf-8')
            dtstart = component.get('dtstart').dt
            dtend = component.get('dtend').dt
            events.append({
                'summary': summary,
                'start': dtstart,
                'end': dtend
            })
    return events

ics_url = 'https://raw.githubusercontent.com/Vomxy/fuzzy-octo-doodle/refs/heads/main/Essentials-2025-06-27.ics'
events = get_events(ics_url)
