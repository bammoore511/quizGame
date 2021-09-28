from question_model import Question
from quiz_brain import QuizBrain
import requests
# Question data from Open Trivia DB API
parameters = {
    "amount": 10,
    "type": "boolean",
}
difficulty = input("Difficulty (Easy/Medium/Hard): ").lower()
parameters["difficulty"] = difficulty
trivia = requests.get(url="https://opentdb.com/api.php", params=parameters)
trivia.raise_for_status()
question_data = trivia.json()['results']

# create banks of questions
questions = []

# fill banks with data from Open Quiz DB
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizBrain(questions)

while quiz.has_more_questions():
    quiz.next_question()
