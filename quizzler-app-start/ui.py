from tkinter import *
from turtle import color
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UiInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzier")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f"score: 0", fg="white", font=("Arial", 12), bg=THEME_COLOR, highlightthickness=0)
        self.label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=30, pady=50)

        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", font=("Arial", 12), width=280)

        self.image_true = PhotoImage(file="C:/Users/acer/Desktop/Coding/Python Code/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day_34/quizzler-app-start/images/true.png")
        self.image_false = PhotoImage(file="C:/Users/acer/Desktop/Coding/Python Code/100 Days of Code The Complete Python Pro Bootcamp for 2022/Day_34/quizzler-app-start/images/false.png")

        self.buttom_true = Button(image=self.image_true, command=self.true_choose)
        self.buttom_true.grid(row=2, column=0)
        self.buttom_false = Button(image=self.image_false, command=self.false_choose)
        self.buttom_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.question_number <= 9:
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        elif self.quiz.question_number > 9:
            self.canvas.itemconfig(self.question_text, text=f"""You're reached the end of the quiz.\n
        Your final score was: {self.quiz.score}/{self.quiz.question_number}"""
            )
            self.buttom_true.config(state="disabled")
            self.buttom_false.config(state="disabled")

    def true_choose(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_choose(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")

        self.window.after(1000, self.get_next_question)

        