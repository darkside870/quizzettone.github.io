from tkinter import Tk, Label, Button, Entry

def start_quiz():
    score = 0
    current_question = 0
    questions = [
        "Qual'è il frutto che inizia con la m e finisce la a ed è formata da 4 lettere?",
        "Chi è il figlio di Maye Musk?",
        "Quando è iniziata la 1 guerra mondiale?",
        "Chi ha vinto il pallone d'oro 2012?"
    ]
    answers = ["mela", "Elon Musk", "1914", "Messi"]

    def check_answer():
        nonlocal score, current_question
        answer = answer_entry.get().strip()
        if answer.lower() == answers[current_question].lower():
            score += 1
        current_question += 1
        if current_question < len(questions):
            show_question()
        else:
            show_result()

    def show_question():
        question_label.config(text=questions[current_question])
        answer_entry.delete(0, 'end')

    def show_result():
        result_label.config(text=f"Hai totalizzato {score} punti su {len(questions)} ({score/len(questions)*100}%)")
        answer_entry.config(state="disabled")
        submit_button.config(state="disabled")

    root = Tk()
    root.title("Quiz App")
    root.geometry("400x300")
    root.configure(bg="#f2f2f2")

    welcome_label = Label(root, text="Benvenuto nel nostro gioco", font=("Arial", 16), bg="#f2f2f2")
    welcome_label.place(relx=0.5, rely=0.1, anchor="center")

    question_label = Label(root, text="", font=("Arial", 14), bg="#f2f2f2")  # Aumenta la dimensione del font a 14
    question_label.place(relx=0.5, rely=0.3, anchor="center")

    answer_entry = Entry(root, font=("Arial", 14))  # Aumenta la dimensione del font a 14
    answer_entry.place(relx=0.5, rely=0.4, anchor="center")

    submit_button = Button(root, text="Invia", font=("Arial", 14), bg="#4caf50", fg="white", command=check_answer)  # Aumenta la dimensione del font a 14
    submit_button.place(relx=0.5, rely=0.5, anchor="center")

    result_label = Label(root, text="", font=("Arial", 16), bg="#f2f2f2")  # Aumenta la dimensione del font a 16
    result_label.place(relx=0.5, rely=0.7, anchor="center")

    show_question()

    root.mainloop()

start_quiz()
