import requests
from bs4 import BeautifulSoup
from functools import lru_cache

@lru_cache(maxsize=None)
def events():
  """Scrapes the events from the CMRIT student clubs website."""
  
  url = "https://sites.google.com/cmrit.ac.in/cmritstudentclubs/"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  
  

  events = []
  for event in soup.find_all("section", class_="yaqOZd qeLZfd", limit=15):
    title = event.find("p", class_="zfr3Q CDt4Ke").text
    start_date_and_time = event.find_all("p", class_="zfr3Q CDt4Ke")[1].text
    end_date_and_time = event.find_all("p", class_="zfr3Q CDt4Ke")[2].text
    
    # exception handling for image poster
    try:
       image_poster = event.find("img")["src"]
    except:
       image_poster = None 
  
    # exception handling for registration link
    try:
      registration_link = event.find("a", class_="XqQF9c")["href"]
    except:
       registration_link = None
    
    events.append({
        "title": title.strip(),
        "start_date": start_date_and_time.split(":")[1].strip(),
        "end_date": end_date_and_time.split(":")[1].strip(),
        "image_poster": image_poster,
        "registration_link": registration_link,
    })

  return events

if __name__ == "__main__":
  for event in events():
    print(event)

