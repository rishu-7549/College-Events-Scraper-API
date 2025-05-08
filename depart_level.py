import requests
from bs4 import BeautifulSoup
from functools import lru_cache

@lru_cache(maxsize=None)
def events():
  """Scrapes the events from the CMRIT Department & Institute Level."""
  
  url = "https://sites.google.com/cmrit.ac.in/department-institute-level-act/"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")

  events = []
  for event in soup.find_all("section", class_="yaqOZd lQAHbd", limit=10):
    title = event.find("p", class_="zfr3Q CDt4Ke").text
    start_date_and_time = event.find_all("p", class_="zfr3Q CDt4Ke")[1].text
    end_date_and_time = event.find_all("p", class_="zfr3Q CDt4Ke")[2].text
    image_poster = event.find("img")["src"] 
    registration_link = event.find("a", class_="XqQF9c")
    if registration_link and registration_link["href"]:
        registration_link = registration_link["href"]
    else:
        registration_link = None

    events.append({
        "title": title.strip(),
        "start_date": start_date_and_time.split(":")[0].strip(),
        "end_date": end_date_and_time.split(":")[0].strip(),
        "image_poster": image_poster,
        "registration_link": registration_link,
    })

  return events

if __name__ == "__main__":
  for event in events():
    print(event)

