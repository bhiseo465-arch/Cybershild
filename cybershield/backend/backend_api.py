from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


app = FastAPI()


# -----------------------------
# DATABASE (TEMP MEMORY STORAGE)
# -----------------------------

quizzes = [

    {
        "id": 1,
        "title": "Phishing Awareness",
        "description": "Detect fake banking emails.",
        "difficulty": "Beginner",
    },

    {
        "id": 2,
        "title": "OTP Scam Protection",
        "description": "Learn safe OTP practices.",
        "difficulty": "Intermediate",
    },
]


leaderboard = [

    {
        "name": "Omkar",
        "score": 980,
    },

    {
        "name": "Aarav",
        "score": 920,
    },
]


simulations = [

    {
        "id": 1,

        "scenario":
        "You receive a WhatsApp message asking for urgent UPI payment.",

        "answer":
        "Scam",

        "explanation":
        "Scammers create urgency to manipulate users.",
    },

    {
        "id": 2,

        "scenario":
        "Your bank app asks you to verify login through official notification.",

        "answer":
        "Safe",

        "explanation":
        "Official banking apps use verified authentication.",
    },
]


# -----------------------------
# Pydantic Models
# -----------------------------

class Quiz(BaseModel):

    title: str

    description: str

    difficulty: str


class Score(BaseModel):

    name: str

    score: int


# -----------------------------
# ROOT ROUTE
# -----------------------------

@app.get("/")
def home():

    return {
        "message":
        "CyberShield Backend Running"
    }


# -----------------------------
# GET QUIZZES
# -----------------------------

@app.get("/quizzes")
def get_quizzes():

    return {
        "quizzes":
        quizzes
    }


# -----------------------------
# CREATE QUIZ
# -----------------------------

@app.post("/quizzes")
def create_quiz(
    quiz: Quiz
):

    new_quiz = {

        "id":
        len(quizzes) + 1,

        "title":
        quiz.title,

        "description":
        quiz.description,

        "difficulty":
        quiz.difficulty,
    }

    quizzes.append(new_quiz)

    return {

        "message":
        "Quiz created successfully",

        "quiz":
        new_quiz,
    }


# -----------------------------
# GET LEADERBOARD
# -----------------------------

@app.get("/leaderboard")
def get_leaderboard():

    return {
        "leaderboard":
        leaderboard
    }


# -----------------------------
# ADD SCORE
# -----------------------------

@app.post("/leaderboard")
def add_score(
    score: Score
):

    leaderboard.append({

        "name":
        score.name,

        "score":
        score.score,
    })

    return {

        "message":
        "Score added successfully"
    }


# -----------------------------
# GET SCAM SIMULATIONS
# -----------------------------

@app.get("/simulations")
def get_simulations():

    return {
        "simulations":
        simulations
    }


# -----------------------------
# NFT REWARD SIMULATION
# -----------------------------

@app.post("/mint-nft")
def mint_nft():

    return {

        "status":
        "success",

        "message":
        "UGF processed gasless NFT mint successfully",

        "tx_hash":
        "0xCYBERSHIELD123456",
    }