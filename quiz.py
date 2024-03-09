import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz App")
        self.master.geometry("400x300")
        self.master.configure(bg="#FFFFFF")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Rome"],
                "answer": "Paris"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["2", "3", "4", "5"],
                "answer": "4"
            },
            {
                "question": "Who is the president of the USA?",
                "options": ["Donald Trump", "Barack Obama", "Joe Biden", "Hillary Clinton"],
                "answer": "Joe Biden"
            }
        ]
        self.current_question = 0
        self.total_score = 0

        self.question_label = tk.Label(self.master, text="", font=("Arial", 14), bg="#FFFFFF")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            option_button = tk.Button(self.master, text="", command=lambda option=i: self.select_option(option), font=("Arial", 12), bg="#DDDDDD", fg="#333333", activebackground="#CCCCCC")
            option_button.pack(pady=5, padx=10, fill=tk.X)
            self.option_buttons.append(option_button)

        self.feedback_label = tk.Label(self.master, text="", font=("Arial", 12), bg="#FFFFFF")
        self.feedback_label.pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i], state="normal")
            self.feedback_label.config(text="")
        else:
            self.show_score()

    def select_option(self, option):
        selected_option = self.questions[self.current_question]["options"][option]
        correct_answer = self.questions[self.current_question]["answer"]

        if selected_option == correct_answer:
            self.feedback_label.config(text="Your answer is correct!", fg="green")
            self.total_score += 1
        else:
            self.feedback_label.config(text=f"Sorry, the correct answer is {correct_answer}.", fg="red")

        for button in self.option_buttons:
            button.config(state="disabled")
        self.master.after(1000, self.next_question)

    def next_question(self):
        self.current_question += 1
        self.display_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Total Score: {self.total_score}/{len(self.questions)}")
        self.master.destroy()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
