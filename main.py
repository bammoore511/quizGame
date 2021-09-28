from question_model import Question
from quiz_brain import QuizBrain
import requests
# Question data from Open Trivia DB API
trivia = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")

question_data = trivia.json()['results']

# create banks of questions
easy_questions = []
medium_questions = []
hard_questions = []
# fill banks with data from Open Quiz DB
for question in easy_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    easy_questions.append(new_question)

for question in medium_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    medium_questions.append(new_question)

for question in hard_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    hard_questions.append(new_question)

easy_quiz = QuizBrain(easy_questions)
medium_quiz = QuizBrain(medium_questions)
hard_quiz = QuizBrain(hard_questions)
