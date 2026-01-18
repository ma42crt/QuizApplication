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
def login():
    correct_username = "admin"
    correct_password = "1234"
    attempts = 0
    while attempts < 3:
        username = input("Enter User Name")
        password = input("Enter Password")

        if username == correct_username and password == correct_password:
            print("\nLogin Successful\n")
        else:
            print("Details are incorrect, Please try Again")
            attempts+=1
    print("You used the all attempts please try again later")
    return