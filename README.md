Title: Questionnaire App

Description:

The given Python script creates an interactive quiz application using the tkinter library for the graphical user interface (GUI) and the requests module for fetching quiz data. It demonstrates a structured approach to designing a user-friendly application with real-time API integration and GUI controls.

Overview:

The script initializes a tkinter window (window) and fetches a set of 20 true/false questions from the Open Trivia Database API. These questions are parsed into Question objects, which store the question text and correct answers. The questions are passed into a Quiz object that manages the quiz state, including the current question number, the user’s score, and GUI elements for displaying the question and score.

Components:

1. Constants and Globals:

Constants like DARK_NAVY, WHITE, and FONT_NAME define consistent styles for the GUI.
Window is a global tkinter root instance used to manage all GUI components.
A global quiz variable holds the current quiz instance.

2. Main Function:

The main() function resets the GUI and initializes a new quiz session.
It fetches questions from the API, processes them, and initializes the quiz interface.
Error handling ensures good operation in case the API request fails.

3.	Question and Quiz Classes:

Question encapsulates the question text and its answer.
Quiz manages the quiz logic, including the current question, score, and interactions with tkinter labels

4.	GUI Design:

The GUI features a title, a canvas displaying an image, and labels for the question and score.
Buttons for “True,” “False,” and “Reset” provide user interaction, invoking appropriate callback functions when clicked.
The design uses consistent styles and layouts for a professional look.

5.	Core Functions:

Check_true() and check_false() handle user input for true/false buttons. They check the user’s answer against the correct answer, update the score, and move to the next question.
Check_questions_left() determines whether there are more questions to display or if the quiz is complete, updating the GUI accordingly.
Reset_program() resets the quiz by re-invoking the main() function.

6.	Dynamic Question Handling:

Questions and answers are dynamically fetched from the API, decoded to handle HTML entities, and stored in a list of Question objects.
The application seamlessly transitions between questions, updating labels dynamically.

7. Loop:

The script concludes with window.mainloop(), which keeps the application running and responsive to user inputs.


Strengths:

API Integration: Fetching live data from an API keeps the quiz dynamic and varied.
Encapsulation: The Question and Quiz classes encapsulate data and behavior, adhering to object-oriented principles.
Error Handling: API requests include error handling to ensure stability.
GUI Design: A simple and user-friendly interface is created with tkinter.


This script is a strong foundation for a Python-based quiz application, showcasing modular design, API usage, and GUI development.