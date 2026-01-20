
# function to store all quiz questions, options and their answer
def quiz_questions():
    return [
        {"question": "Which device is used to input text into a computer?",
         "options": ["Monitor", "Keyboard", "Printer", "Speaker"],
         "answer": 2},

        {"question": "What does RAM stand for?",
         "options": ["Read Access Memory", "Random Access Memory","Run Access Memory", "Rapid Action Memory"],
         "answer": 2},

        {"question": "Which number is an even number?",
         "options": ["7", "9", "11", "12"],
         "answer": 4},

        {"question": "Which of these is an operating system?",
         "options": ["Python", "Windows", "Google", "HTML"],
         "answer": 2},

        {"question": "What is 15 - 7?",
         "options": ["6", "7", "8", "9"],
         "answer": 3},

        {"question": "Which word is a verb?",
         "options": ["Happy", "Run", "Blue", "Tall"],
         "answer": 2},

        {"question": "Which symbol is used for comments in Python?",
         "options": ["//", "#", "/*", "--"],
         "answer": 2},

        {"question": "Which planet is closest to the Sun?",
         "options": ["Earth", "Mars", "Mercury", "Venus"],
         "answer": 3},

        {"question": "What is the result of 4 × 5?",
         "options": ["15", "18", "20", "25"],
         "answer": 3},

        {"question": "Which of these is a web browser?",
         "options": ["Chrome", "Linux", "Python", "Windows"],
         "answer": 1},

        {"question": "Which unit is used to measure data size?",
         "options": ["Meter", "Kilogram", "Byte", "Second"],
         "answer": 3},

        {"question": "Which shape has four equal sides?",
         "options": ["Rectangle", "Triangle", "Circle", "Square"],
         "answer": 4},
    ]

# function to run login
def login():
    correct_username = "admin"
    correct_password = "1234"
    attempts = 0
    while attempts < 3:
        username = input("Enter User Name: ")
        password = input("Enter Password: ")

        # check if username and password are correct
        if username == correct_username and password == correct_password:
            print("\nLogin Successful!\n")
            return True  # login successful and then next process
        else:
            print("Details are incorrect. Please try again.\n")
            attempts += 1

    print("You used all attempts. Please try again later.")
    return False  # login failed, it will stop the program here 

def user_answer():
    # while loop will ask the user for input until the user input valid input
    while True:
        answer = input("Your answer (1-4): ")
        if answer in ["1", "2", "3", "4"]:
            return int(answer)
        else:
            print("Invalid input. Please enter 1, 2, 3, or 4.")



def run_quiz():
        

    print("Welcome to the Holton College Digital Quiz!")
    print("Choose the correct option (1–4).\n")

    questions = quiz_questions()  # to get the question from question list
    score = 0

    # loop through each question
    for i in range(len(questions)):
        question = questions[i]

        # print question number and text
        print(f"Question {i + 1}: {question['question']}")

        # print all 4 options
        for j in range(4):
            print(f"{j + 1}. {question['options'][j]}")

        # to check the answer from list
        user_ans = user_answer()

        if user_ans == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")

    # show final score
    print("Quiz Finished!")
    print("Your final score:", score, "/", len(questions))

    # show percentage score
    percentage = (score / len(questions)) * 100
    print(f"Your percentage score: {percentage:.2f}%")

    # show pass/fail
    if percentage >= 50:
        print("Congratulations! You passed the quiz.")
    else:
        print("You did not pass. Try again next time!")
    print("Thank you for playing the Holton College Quiz!")


# program starts here
# first the program will run the login function and then the main quiz
if login():
    run_quiz()
