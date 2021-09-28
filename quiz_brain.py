import html
import requests


# Get the question data from the Open Trivia API based on the chosen difficulty
def get_data(difficulty: str):
    parameters = {"amount": 10, "type": "boolean", "difficulty": difficulty.lower()}
    trivia = requests.get(url="https://opentdb.com/api.php", params=parameters)
    trivia.raise_for_status()
    return trivia.json()['results']


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.current_question = None

    def has_more_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return html.unescape(self.current_question.text)

    def check_answer(self, user_answer: str) -> bool:

        if user_answer == self.current_question.answer:
            self.score += 1
            return True
        else:
            return False
