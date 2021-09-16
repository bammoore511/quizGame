from data import *
from question_model import Question

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