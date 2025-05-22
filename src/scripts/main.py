from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from typing import List, Optional

app = FastAPI()

# Конфігурація бази даних
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Biocide1324!",
    "database": "mydb"
}

# ───────────── Моделі ─────────────
class UserBase(BaseModel):
    email: str
    password: str
    name: str
    surname: str
    nickname: str

class User(UserBase):
    id: int

class QuizBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    User_id: int

class Quiz(QuizBase):
    id: int

# ───────────── ENDPOINTS: User ─────────────
@app.get("/users", response_model=List[User])
def get_users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM User")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

@app.post("/users", status_code=201)
def create_user(user: UserBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO User (email, password, name, surname, nickname) VALUES (%s, %s, %s, %s, %s)",
        (user.email, user.password, user.name, user.surname, user.nickname)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User created"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE User SET email=%s, password=%s, name=%s, surname=%s, nickname=%s WHERE id=%s",
        (user.email, user.password, user.name, user.surname, user.nickname, user_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User updated"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM User WHERE id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "User deleted"}

# ───────────── ENDPOINTS: Quiz ─────────────
@app.get("/quizzes", response_model=List[Quiz])
def get_quizzes():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Quiz")
    quizzes = cursor.fetchall()
    cursor.close()
    conn.close()
    return quizzes

@app.post("/quizzes", status_code=201)
def create_quiz(quiz: QuizBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Quiz (name, description, User_id) VALUES (%s, %s, %s)",
        (quiz.name, quiz.description, quiz.User_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Quiz created"}

@app.put("/quizzes/{quiz_id}")
def update_quiz(quiz_id: int, quiz: QuizBase):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Quiz SET name=%s, description=%s, User_id=%s WHERE id=%s",
        (quiz.name, quiz.description, quiz.User_id, quiz_id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Quiz updated"}

@app.delete("/quizzes/{quiz_id}")
def delete_quiz(quiz_id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Quiz WHERE id=%s", (quiz_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Quiz deleted"}
