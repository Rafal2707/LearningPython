def new_game():
    guessess = []
    correct_guesses = 0
    question_num = 1
    for question in questions:
        print(question)
        for option in options[question_num-1]:
            print(option)
        guess = input("enter (A, B, C, or D): ")
        guess = guess.upper()
        guessess.append(guess)

        correct_guesses += check_answer(questions.get(question), guess)
        question_num += 1

    display_score(correct_guesses, guessess)
def check_answer(answer, guess):
    if answer == guess:
        print("correct!")
        return 1
    else:
        print("incorrect!") 
        return 0 
        
def display_score(correct_guesses, guessess):
    print("RESULTS")
    print("Answers: ", end="")
    for question in questions:
        print(questions.get(question), end=" ")
    print()
    print("Guessess: ", end="")
    for guess in guessess:
        print(guess, end=" ")

    score = int(correct_guesses/len(questions)*100)
    print()
    print("Your score is: " + str(score)+"%")


def play_again():
    response = input("Do you want to play again? (Yes/No): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "Who created Python?: " : "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: " : "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. I don't know"]
]

new_game()
while play_again():
    new_game()

print("Thank you for playing")