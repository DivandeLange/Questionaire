from tkinter import *
from questionnaire_classes import Question, Quiz
import requests
import html

# Constants
DARK_NAVY = "#000435"
WHITE = "#FFFFFF"
FONT_NAME = "Courier"

# Global variable for the tkinter window
window = Tk()

def main():
    """
        Initializes or resets the questionnaire GUI.
        """
    # Clear existing widgets from the window
    for widget in window.winfo_children():
        widget.destroy()

    try:
        # getting 20 questions from open Trivia database api and saved results from json file to data list
        response = requests.get(url="https://opentdb.com/api.php?amount=20&category=18&type=boolean")
        response.raise_for_status()
    except requests.RequestException as error:
        # Print an error message if fetching questions fails
        print(f"Error fetching questions: {error}")
    else:
        data = response.json()["results"]

        # creating a list of objects created from Question class
        list_of_question_objects = []

        # looping through each item in data list,
        for item in data:
            # Decode HTML entities in the question and answer
            question_text = html.unescape(item["question"])
            correct_answer = html.unescape(item["correct_answer"])

            # creating new object from Question class with question and correct_answer as arguments passed in
            new_question = Question(question_text, correct_answer)

            # adding new created object to list of question objects
            list_of_question_objects.append(new_question)


        #### ----- Creation of GUI ---- ####

        # Creating window title and padding
        window.title("Questionnaire")
        window.config(bg=DARK_NAVY, pady=20, padx=20, highlightthickness=0)

        # Setting up canvas image and packing on window
        canvas = Canvas(width=512, height=128, bg=DARK_NAVY, highlightthickness=0)
        img = PhotoImage(file="./Images/Questionnaire.png")
        canvas.create_image(250, 64, image=img)
        canvas.grid(column=1, row=0)

        # Keep the image reference alive
        window.img = img

        # Creating Questions label to appear on window
        question_label = Label(text="", fg=WHITE, bg=DARK_NAVY,
                               font=(FONT_NAME, "15", "normal"),
                               wraplength=400,
                               justify="center")
        question_label.grid(column=1, row=1)
        question_label.config(pady=100)

        # Creating score label to appear on window and display score
        score_label = Label(text="", fg=WHITE, bg=DARK_NAVY, font=(FONT_NAME, "20", "normal"))
        score_label.grid(column=2, row=4)

        # creating quiz object from Quiz class and passing in list of questions objects
        quiz = Quiz(list_of_question_objects, question_label, score_label)

        # Initialize the first question
        question_label.config(text=f"Q.1: {quiz.question_list[0].question}")

        # Initializing the first score
        score_label.config(text=f"Score: {quiz.score}")

        # Creating image button to appear on window
        true_image = PhotoImage(file="./Images/True.png")
        true_button = Button(image=true_image, bg=DARK_NAVY, borderwidth=0, command=quiz.check_true)
        true_button.grid(column=0, row=3)
        window.true_image = true_image  # Keep the image reference alive

        # Creating image button to appear on window
        false_image = PhotoImage(file="./Images/False.png")
        false_button = Button(image=false_image, bg=DARK_NAVY, borderwidth=0, command=quiz.check_false)
        false_button.grid(column=2, row=3)
        window.false_image = false_image  # Keep the image reference alive

        # Reset Button
        reset_image = PhotoImage(file="./Images/reset.png")
        reset_button = Button(image=reset_image, bg=DARK_NAVY, borderwidth=0, command=reset_program)
        reset_button.grid(column=1, row=4)
        window.reset_image = reset_image  # Keep the image reference alive

# reset the program when reset button is clicked
def reset_program():
    main()

if __name__ == "__main__":
    main()
    window.mainloop()