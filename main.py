import quiz_brain
from question_model import Question
from quiz_brain import QuizBrain, get_data
from quiz_ui import QuizUI
from tkinter import *
import requests

# Initial UI Setup
initial_window = Tk()
initial_window.title("QuizzMe")
initial_window.config(padx=30, pady=30, bg="#262626")


# Function to go to main page after difficulty is chosen
def next_page(difficulty: str):
    initial_window.destroy()
    # get data
    question_data = quiz_brain.get_data(difficulty)
    # create banks of questions
    questions = []

    # fill banks with data from Open Quiz DB
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        questions.append(new_question)

    quiz = QuizBrain(questions)
    QuizUI(quiz)


title = Label(
    text="Welcome to QuizzMe",
    padx=20,
    pady=20,
    bg='#262626',
    fg="#d9048e",
    font=('Arial', 35)
)
title.grid(column=0, row=0, columnspan=3)

difficulty_label = Label(
    text="Choose your difficulty",
    padx=20,
    pady=40,
    bg='#262626',
    fg="#d9048e",
    font=('Arial', 20)
)
difficulty_label.grid(column=0, row=1, columnspan=3)

easy_button = Button(
    text="Easy",
    padx=10,
    bg="#9b0bd9",
    font=('Arial', 15),
    bd=0,
    command=lambda: next_page("easy")
)
easy_button.grid(column=0, row=2)

med_button = Button(
    text="Medium",
    padx=10,
    bg="#f2cb05",
    font=('Arial', 15),
    bd=0,
    command=lambda: next_page("med")
)
med_button.grid(column=1, row=2)

hard_button = Button(
    text="Hard",
    padx=10,
    bg="#2bc7d9",
    font=('Arial', 15),
    bd=0,
    command=lambda: next_page("hard")
)
hard_button.grid(column=2, row=2)

initial_window.mainloop()
