# Define the dictionary as a constant
QUESTIONS = {
    '1': 'Your partner makes hurtful jokes?',
    '2': 'Your partner blackmails you?',
    '3': 'Your partner lies or cheats on you?',
    '4': 'Your partner ignores you or applies the silent treatment?',
    '5': 'Your partner is jealous of you?',
    '6': 'Your partner stalks you or stalks you on social networks?',
    '7': 'Your partner blames you?',
    '8': 'Your partner disqualifies you?',
    '9': 'Your partner ridicules or offends you?',
    '10': 'Your partner humiliates you in public?',
    '11': 'Your partner intimidates or threatens you?',
    '12': 'Your partner controls or prohibits you: friends, family, money, places, appearance, activities, cell phone, emails, social networks?',
    '13': 'Your partner destroys personal items?',
    '14': 'Your partner gropes you?',
    '15': 'Your partner gives you aggressive caresses?',
    '16': 'Your partner hits you "playing"?',
    '17': 'Your partner pinches or scratches you?',
    '18': 'Your partner pushes or pulls you?',
    '19': 'Your partner slaps you?',
    '20': 'Your partner kicks you?',
    '21': 'Your partner kicks you?',
    '22': 'Your partner locks you up or isolates you?',
    '23': 'Your partner threatens you with objects or weapons?',
    '24': 'Your partner threatens to kill you?',
    '25': 'Your partner spreads intimate content without consent through digital media?',
    '26': 'Your partner forces a sexual relationship?',
    '27': 'Your partner sexually abuses you?',
    '28': 'Your partner rapes you?',
    '29': 'Your partner mutilates you?',
    '30': 'Your partner murders you.'
}

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ViolenceQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Violence Detection Quiz")
        self.counter = 0

        # Cargar la imagen
        self.image = Image.open("/Users/rorygrimm/Documents/No_More_Violence.png")  # Asegúrate de que esta es la ruta correcta a tu imagen
        self.image = self.image.resize((200, 200), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(root, image=self.photo)
        self.image_label.pack(pady=10)

        self.intro_label = tk.Label(root, text="Welcome to the Violence Detection Quiz. This Quiz is a useful tool that allows you to be alert, trained and attentive to detect and address the different manifestations of violence that are hidden in everyday life and that are often confused or unknown. Answer Yes or No to each question, in the end, you will know the situation you are in and you will be given timely instructions and support telephone numbers.", wraplength=400, justify=tk.CENTER, pady=10)
        self.intro_label.pack()

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, padx=10, pady=5)
        self.start_button.pack()

        self.help_button = tk.Button(root, text="Help", command=self.show_help, padx=10, pady=5)
        self.help_button.pack()

    def start_quiz(self):
        self.intro_label.pack_forget()
        self.start_button.pack_forget()
        self.help_button.pack_forget()
        self.current_question = 0
        self.ask_question()

    def ask_question(self):
        if self.current_question < len(QUESTIONS):
            self.question_label = tk.Label(root, text=QUESTIONS[str(self.current_question + 1)], wraplength=400, justify=tk.LEFT, pady=10)
            self.question_label.pack()
            
            self.yes_button = tk.Button(root, text="Yes", command=lambda: self.record_answer(1))
            self.no_button = tk.Button(root, text="No", command=lambda: self.record_answer(0))
            self.yes_button.pack(side=tk.LEFT, padx=20)
            self.no_button.pack(side=tk.RIGHT, padx=20)
        else:
            self.show_result()

    def record_answer(self, answer):
        self.counter += answer
        self.current_question += 1
        self.question_label.pack_forget()
        self.yes_button.pack_forget()
        self.no_button.pack_forget()
        self.ask_question()

    def show_result(self):
        self.result_label = tk.Label(root, text=f"You scored {self.counter} points out of 30.", wraplength=400, justify=tk.CENTER, pady=10)
        self.result_label.pack()
        
        if 1 <= self.counter <= 5:
            message = "GREEN LEVEL\nThe violence is just beginning, but be careful, because it will increase. These are the first red flags that show you that you are with an abusive and toxic person. This is the best time to get out of the relationship."
        elif 5 < self.counter <= 17:
            message = "YELLOW LEVEL\nThe violence is advancing too much and too fast. React, don't let yourself be destroyed!Don't forget that violence only gets worse. It is necessary that you inform yourself about the cycle of violence, which has the following phases: accumulation of tension, outbreak of violence and honeymoon."
        elif 17 < self.counter <= 22:
            message = "ORANGE LEVEL\nAt this level, violence is also physical, you need to contact your support network (they can be family, friends, or even new people, there is always someone willing to help). Remember that you are a valuable person, who deserves love, respect, dignified treatment and a happy life. You can always start over, and there are people who are willing to support you. Please, love yourself above all, you will always be the most important person in your own life."
        else:
            message = "RED LEVEL\nYou need professional help, go to domestic violence support centers, psychologists, shelters, and non-profit support foundations. Surely someone will be able to help you make a plan to get out of this situation THAT YOU DON'T DESERVE. In Mexico, per day, there are up to 11 femicides. Your life is valuable, you don't deserve to be treated this way.YOU ARE NOT ALONE!"

        messagebox.showinfo("Result", message)

    def show_help(self):
        help_message = """
        If you or someone you know is in immediate danger, call emergency services.

        National Domestic Violence Hotline: 1-800-799-7233
        Loveisrespect: 1-866-331-9474
        National Sexual Assault Hotline: 1-800-656-4673

        Visit these websites for more information:
        www.thehotline.org
        www.loveisrespect.org
        """
        messagebox.showinfo("Help", help_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ViolenceQuizApp(root)
    root.mainloop()
