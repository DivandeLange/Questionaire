
class Question:
    """
    A class to represent a single question in the quiz.

    Attributes:
        question (str): The text of the question.
        answer (str): The correct answer to the question ("True" or "False").
    """

    def __init__(self, text, answer):
        self.question = text
        self.answer = answer

class Quiz:
    """
    A class to represent the quiz and manage its functionality.

    Attributes:
        question_number (int): The current question index in the quiz.
        question_list (list): A list of Question objects for the quiz.
        score (int): The user's current score.
        q_label (Label): A tkinter Label widget for displaying the question.
        s_label (Label): A tkinter Label widget for displaying the score.
    """

    def __init__(self, list_of_questions, q_label,  s_label):
        self.question_number = 0
        self.question_list = list_of_questions
        self.score = 0
        self.q_label = q_label
        self.s_label = s_label

    # to check if questions still left or at end of quiz
    def check_questions_left(self):
        if self.question_number < len(self.question_list):
            # Update the question label with the next question
            next_question = self.question_list[self.question_number]
            self.q_label.config(text=f"Q.{self.question_number + 1}: {next_question.question}")
        else:
            # Handle the end of the quiz
            self.q_label.config(text=f"Quiz Completed. Final Score: {self.score}/20")

    def check_true(self):
        # Get the current question object
        current_question = self.question_list[self.question_number]

        # Access the correct answer from the Question object
        correct_answer = current_question.answer

        # Check if the answer is correct
        if correct_answer == 'True':
            self.score += 1 # Increment the score if the answer is correct
            self.s_label.config(text=f"Score: {self.score}") # Update the score label

        # Move to the next question
        self.question_number += 1

        # calling function to check if questions still left or at end of quiz
        self.check_questions_left()


    def check_false(self):
        # Get the current question object
        current_question = self.question_list[self.question_number]

        # Access the correct answer from the Question object
        correct_answer = current_question.answer

        # Check if the answer is correct
        if correct_answer == 'False':
            self.score += 1 # Increment the score if the answer is correct
            self.s_label.config(text=f"Score: {self.score}") # Update the score label

        # Update the score label
        self.question_number += 1

        # calling function to check if questions still left or at end of quiz
        self.check_questions_left()

