# College Event Scraper API

A scalable and efficient FastAPI-based backend that scrapes, aggregates, and serves structured event data from CMRIT Student Club and Department websites as a RESTful JSON API.

## Tech Stack

- Python 3
- FastAPI
- BeautifulSoup4
- Requests
- Uvicorn (ASGI server)
- asyncio
- functools.lru_cache

## Installation

1. Clone this repository:
   git clone https://github.com/yourusername/college-event-scraper-api.git
    cd college-event-scraper-api

2. Install dependencies:
    pip install -r requirements.txt

3. Run the FastAPI server:
    uvicorn app:app --reload
    

## Deployment

You can deploy this API on popular platforms like [Render](https://render.com/), [Railway](https://railway.app/), [Heroku](https://heroku.com/), or cloud providers like AWS, Azure, and GCP.

## Project Structure

├── app.py
├── requirements.txt
├── student_club.py
├── depart_level.py
└── README.md

## Contributing

Pull requests are welcome! Open an issue or submit a PR for improvements and bug fixes.


**Made with ❤️ by Rishu Kumar**
