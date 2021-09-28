from tkinter import *
from quiz_brain import QuizBrain


class QuizUI:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("QuizzMe")
        self.window.config(padx=30, pady=30, bg="#262626")

        self.score_label = Label(
            text=f"Score: {quiz.score}",
            fg="white",
            bg="#262626",
            font=("Arial", 20)
        )
        self.score_label.grid(row=0, column=1)
        self.q_label = Label(
            text=f"Question: {self.quiz.question_number}",
            fg="white",
            bg="#262626",
            font=("Arial", 20)
        )
        self.q_label.grid(row=0, column=0)

        self.question_canvas = Canvas(width=400, height=350, bg="white", highlightthickness=0)
        self.question_text = self.question_canvas.create_text(
            200,
            175,
            width=380,
            text="Some question text",
            fill="#262626",
            font=("Arial", 20, "italic")
        )
        self.question_canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="assets/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="assets/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.has_more_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.q_label.config(text=f"Question: {self.quiz.question_number + 1}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="Quiz Over :)")
            self.false_button.config(command=NONE)
            self.true_button.config(command=NONE)

    def true_pressed(self):
        self.respond(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.respond(self.quiz.check_answer("False"))

    def respond(self, is_right: bool):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.question_canvas.update()
        self.window.after(1000, self.get_next_question())
