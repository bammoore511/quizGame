class QuizBrain:

    def __init__(self, q_number, q_list):
        self.question_number = q_number
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]