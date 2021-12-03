"""
Welcome to Simple python quiz game
"""
import sys

class Question:
    """ The class based implementation of python quiz game"""
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
    @classmethod
    def greet(cls):
        """Function Introduce user about game"""
        print("Welcome to AskPython Quiz")

    @classmethod
    def interest(cls):
        """Function knows the interest of the user"""
        play = input("Are you ready to play the Quiz ?")

        if play != "yes":
            sys.exit()
            
question_prompts = [
    "Question 1: What is your Favourite programming language?",
    "Question 2: Do you follow any author on AskPython?",
    "Question 3: What is the name of your favourite website for learning Python?"
]

questions = [
    Question(question_prompts[0], "python"),
    Question(question_prompts[1], "yes"),
    Question(question_prompts[2], "askpython"),
]


def run_quiz(quest):
    """Quiz code started from here"""
    score = 0.1
    noq = 0
    Question.greet()
    Question.interest()
    for question in quest:
        answer = input(question.prompt)
        if answer == question.answer:
            print("correct")
            score += 33.33
            noq += 1
        else:
            print("incorrect")
    print(f"Thankyou for Playing this small quiz game, you attempted {noq} questions correctly!")
    print(f"Marks obtained: {round(score)}")
    print("BYE!")


run_quiz(questions)
