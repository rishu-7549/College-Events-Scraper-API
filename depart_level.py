import requests
from bs4 import BeautifulSoup
from functools import lru_cache
import logging

@lru_cache(maxsize=None)
def events():
  """Scrapes the events from the CMRIT Department & Institute Level."""
  
  url = "https://sites.google.com/cmrit.ac.in/department-institute-level-act/"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  
  # Extract date and time
  def extract_after_colon(text):
    return text.partition(":")[2].strip()

  events = []
  for event in soup.find_all("section", class_="yaqOZd lQAHbd", limit=10):
    paragraph = event.find_all("p", class_="zfr3Q CDt4Ke")
    title = paragraph[0].text.strip() if len(paragraph) > 0 else "N/A"
    start_date_and_time = paragraph[1].text if len(paragraph) > 1 else ""
    end_date_and_time = paragraph[2].text if len(paragraph) > 2 else ""
    start_date = extract_after_colon(start_date_and_time)
    end_date = extract_after_colon(end_date_and_time)
    image_poster = event.find("img")["src"] 
    registration_link = event.find("a", class_="XqQF9c")
    if registration_link and registration_link["href"]:
        registration_link = registration_link["href"]
    else:
        registration_link = None

    events.append({
        "title": title.strip(),
        "start_date": start_date,
        "end_date": end_date,
        "image_poster": image_poster,
        "registration_link": registration_link,
    })

  return events

if __name__ == "__main__":
  for event in events():
    print(event)

