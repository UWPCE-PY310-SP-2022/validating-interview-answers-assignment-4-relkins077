import re

def blank_check(check):
    while check == '':
        check = input("Please enter the required information: ")
    else:
        return check

def email_check(email):
    while True:
        if not email:
            print("Please provide your email address.")
            email = input("what is your email address?: ")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("The email format isnt correct. Please try again.")
            email = input("what is your email address?: ")
        else:
            return email


name = input("what is your name?: ")
name = blank_check(name)
print(f"Ok, {name}! Let's gather a few more details about your stay: ")
conf_id = input("what is your conference ID?: ")
conf_id = blank_check(conf_id)
org = input("what organization do you represent?: ")
org = blank_check(org)
email = input("what is your email address?: ")
email = email_check(email)
food = input("any food preferences?: ")
food = blank_check(food)

classes = ("Python for beginners", "Database development with Python",
           "Python for data science", "Advanced Python for application developers")
answers = []
for x in classes:
    print(f"{name},Would you like to attend", x, "Y/N?")
    response = input()
    while response.lower() not in ('y', 'n'):
        response = input("please only enter a Y for yes of a N for no: ")
    answers.append(response)
    if response.lower() == 'y':
        print("ok, i've reserved you a seat!")
    else:
        print("ok, maybe some other time!")
print(f"ok {name}, we have your responses listed as follows:")
for i, j in zip(classes, answers):
    print(i, j)
count = 0
for i in answers:
    if i.lower() == 'y':
        break
    elif i.lower() == 'n':
        count += 1
if count == len(answers):
    print("you're going to be bored!")

#####################
import csv

# function to validate user input for yes or no
def question_check(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'yes' or user_input == 'no':
            return user_input
        else:
            print('Please enter either "yes" or "no".')

# function to validate user input for a question between 10 and 30 characters long
def length_limit_check(prompt):
    while True:
        user_input = input(prompt).strip()
        if len(user_input) >= 10 and len(user_input) <= 30:
            return user_input
        else:
            print('Please enter a question between 10 and 30 characters long.')

# read all questions from CSV file
with open('questions.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader) # skip header row
    questions = []
    for row in csv_reader:
        questions.append(row)
        print('{:<5} {:<30}'.format(row[0], row[1]))

# validate each question with user
for i in range(len(questions)):
    while True:
        user_input = question_check(f'Is the question "{questions[i][1]}" correct? (yes/no) ')
        if user_input == 'yes':
            break
        else:
            new_question = length_limit_check('Enter a new question between 10 and 30 characters long to replace the current question: ')
            user_input = question_check(f'Do you still want to keep this question? (yes/no) ')
            if user_input == 'yes':
                questions[i][1] = new_question
                break
            else:
                user_input = question_check(f'Are you sure you want to delete this question? (yes/no) ')
                if user_input == 'yes':
                    questions.pop(i)
                    break

# write updated questions to CSV file
with open('questions.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['id', 'question'])
    for i in range(len(questions)):
        csv_writer.writerow([i+1, questions[i][1]])

# prompt user for new question to add to CSV file
new_question = length_limit_check('Enter a new question between 10 and 30 characters long to add to the table: ')
with open('questions.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow([len(questions)+1, new_question])

# prompt user for their name and answer each question
name = input('What is your name? ')
with open('answers.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    for i in range(len(questions)):
        answer = input(f'{questions[i][1]}: ')
        csv_writer.writerow([name, i+1, answer])

# print all questions from CSV file
with open('questions.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader) # skip header row
    print('\nCurrent questions:')
    for row in csv_reader:
        print('{:<5} {:<30}'.format(row[0], row[1]))


# Read in all questions in the questions.csv file
with open('C:/Users/relki/Desktop/questions.csv') as questions_file:
    questions_reader = csv.reader(questions_file)
    next(questions_reader, None)  # skip header
    questions = [row for row in questions_reader]

# Read in all answers in the answers.csv file
with open('C:/Users/relki/Desktop/answers.csv') as answers_file:
    answers_reader = csv.reader(answers_file)
    next(answers_reader, None)  # skip header
    answers = [row for row in answers_reader]

# Delete any answers that no longer have a valid question (see the deleted question from Part 1)
valid_question_ids = set(row[0] for row in questions)
answers = [row for row in answers if row[1] in valid_question_ids]

# Sort answers by the interviewee's names, alphabetically
answers.sort(key=lambda row: row[0])

# Prints out the questions, one at a time, along with the corresponding set of answers from all interviewees. Format it nicely!
for question in questions:
    print(question[1])
    question_answers = [row for row in answers if row[1] == question[0]]
    for answer in sorted(question_answers, key=lambda row: row[0]):
        print(f"\t- {answer[2]} (interviewee: {answer[0]})")