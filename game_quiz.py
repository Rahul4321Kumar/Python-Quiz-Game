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
            



class StartGame():
    def __init__(self, questions):
        self.questions = questions

    def run_quiz(self):
        """Quiz code started from here"""
        score = 0.1
        number_of_question = 0
        Question.greet()
        Question.interest()
        for question in self.questions:
            answer = input(question.prompt)
            if answer == question.answer:
                print("correct")
                score += 33.33
                number_of_question += 1
            else:
                print("incorrect")
        print(f"Thankyou for Playing this small quiz game, you attempted {number_of_question} questions correctly!")
        print(f"Marks obtained: {round(score)}")
        print("BYE!")


question_prompts = {
    "1": "What is your Favourite programming language?",
    "2": "Do you follow any author on AskPython?",
    "3": "What is the name of your favourite website for learning Python?"
    
}

q1 =Question(question_prompts["1"], "python")
q2=Question(question_prompts["2"], "yes")
q3=Question(question_prompts["3"], "askpython")

questions=[q1, q2, q3]

start=StartGame(questions)
start.run_quiz()

