from quiz_brain import QuizBrain
import tkinter as tk
THEME_COLOR = "#375362"
GREEN = "#2cb474"
RED = "#ec645c"


class QuizWindow:
    """ Main window for Quizbrain """

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzy")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        pads = {"padx": 20, "pady": 20}  # paddings

        self.score_text = tk.Label(
            text="Score: 0", font=('Arial', 14, 'normal'))
        self.score_text.config(bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, **pads)

        FONT = ("Arial", 20, "italic")
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Etwas",
            font=FONT,
            fill=THEME_COLOR
        )

        image_true = tk.PhotoImage(file="images/true.png")
        image_false = tk.PhotoImage(file="images/false.png")
        btn_style = {"highlightthickness": 0, "border": 0}

        self.btn_true = tk.Button(image=image_true, **btn_style)
        self.btn_true.grid(column=0, row=2, **pads)
        self.btn_true.config(command=self.btn_true_click)

        self.btn_false = tk.Button(image=image_false, **btn_style)
        self.btn_false.grid(column=1, row=2, **pads)
        self.btn_false.config(command=self.btn_false_click)

        self.get_next_question()
        self.window.mainloop()

    def btn_true_click(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def btn_false_click(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(500, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg='white')
        score_text = f"Score: {self.quiz.score}"
        self.score_text.config(text=score_text)

        if self.quiz.still_has_questions():
            q_next = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_next)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You answered all the questions!")
            self.btn_true.config(state="disabled")
            self.btn_false.config(state="disabled")
