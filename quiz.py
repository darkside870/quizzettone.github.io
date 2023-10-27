import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz")
        
        self.questions = [
            {
                "question": "Qual è la capitale dell'Italia?",
                "options": ["Roma", "Milano", "Firenze", "Napoli"],
                "answer": "Roma"
            },
            {
                "question": "Quale è il fiume più lungo del mondo?",
                "options": ["Nilo", "Amazzonia", "Mississippi", "Gange"],
                "answer": "Nilo"
            },
            {
                "question": "Quale è il simbolo chimico dell'oro?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "answer": "Au"
            }
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="")
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            button.pack(fill=tk.BOTH, padx=10, pady=5)
            self.option_buttons.append(button)
        
        self.next_question()
    
    def next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            
            for i in range(4):
                self.option_buttons[i].config(text=question["options"][i])
            
            self.current_question += 1
        else:
            messagebox.showinfo("Quiz completato", f"Hai totalizzato {self.score} punti!")
            self.root.destroy()
    
    def check_answer(self, selected_option):
        question = self.questions[self.current_question - 1]
        if question["options"][selected_option] == question["answer"]:
            self.score += 1
        
        self.next_question()

root = tk.Tk()
quiz = Quiz(root)
root.mainloop()
