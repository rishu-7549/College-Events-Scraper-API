import asyncio
from fastapi import FastAPI
import student_club
import depart_level

app = FastAPI()

async def get_student_club_events():
    return await asyncio.to_thread(student_club.events)

async def get_depart_level_events():
    return await asyncio.to_thread(depart_level.events)

eventsDictionary = {
    'developer': 'rishu',
    'student_club': [],
    'depart_level': [],
    'success': True
}

@app.get('/')
async def home():
    return "The CMRIT Events API is HERE! Maintained and Developed by RISHU from MCA."

@app.get("/events")
async def get_events():
    tasks = [get_student_club_events(), get_depart_level_events()]
    results = await asyncio.gather(*tasks)
    eventsDictionary['student_club'] = results[0]
    eventsDictionary['depart_level'] = results[1]
    return eventsDictionary