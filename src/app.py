"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Team-based soccer training and matches",
        "schedule": "Wednesdays and Saturdays, 4:00 PM - 6:00 PM",
        "max_participants": 18,
        "participants": ["alex@mergington.edu", "chris@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball skills and play team games",
        "schedule": "Tuesdays and Thursdays, 5:00 PM - 6:30 PM",
        "max_participants": 15,
        "participants": ["jordan@mergington.edu", "taylor@mergington.edu"]
    },
    "Painting Workshop": {
        "description": "Learn painting techniques and create artworks",
        "schedule": "Mondays, 3:00 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["mia@mergington.edu", "lucas@mergington.edu"]
    },
    "Drama Club": {
        "description": "Perform plays and develop acting skills",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": ["charlotte@mergington.edu", "liam@mergington.edu"]
    },
    "Math Club": {
        "description": "Explore advanced mathematical concepts and problem-solving",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["noah@mergington.edu", "ava@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Build robots and compete in robotics competitions",
        "schedule": "Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 10,
        "participants": ["ethan@mergington.edu", "zoe@mergington.edu"]
    },
    "Volleyball Club": {
        "description": "Learn volleyball techniques and play friendly matches",
        "schedule": "Tuesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["ryan@mergington.edu", "lily@mergington.edu"]
    },
    "Track and Field Team": {
        "description": "Training in various track and field events",
        "schedule": "Mondays, Wednesdays, and Fridays, 3:00 PM - 5:00 PM",
        "max_participants": 25,
        "participants": ["natalie@mergington.edu", "zach@mergington.edu"]
    },
    "Photography Club": {
        "description": "Explore photography techniques and edit images",
        "schedule": "Wednesdays, 3:00 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["isabella@mergington.edu", "mason@mergington.edu"]
    },
    "Music Ensemble": {
        "description": "Practice instruments and perform musical pieces",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": ["elena@mergington.edu", "oliver@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Tuesdays, 5:00 PM - 6:30 PM",
        "max_participants": 16,
        "participants": ["caleb@mergington.edu", "hannah@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific topics",
        "schedule": "Fridays, 3:00 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["tyler@mergington.edu", "amelia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up")

    # Prevent exceeding capacity
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")

    # Register the student
    activity["participants"].append(email)

    return {
        "message": f"{email} has been signed up for {activity_name}",
        "participants": activity["participants"]
    }
