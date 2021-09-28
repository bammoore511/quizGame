import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def has_more_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {html.unescape(current_question.text)} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == "t":
            user_answer = "true"
        elif user_answer.lower() == "f":
            user_answer = "false"
        # else:
        #     print("Please enter a valid response.")

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"Wrong. The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}\n")
