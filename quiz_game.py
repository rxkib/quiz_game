def new_game():
    guesses = []
    correct_guesses = 0
    ques_num = 1

    for key in questions:
        print("-----")
        print(key)
        for i in options[ques_num - 1]:
            print(i)
        guess = input("Enter a b c or d ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        ques_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


def display_score(correct, total):
    print("----")
    print("results")
    print("----")
    print("answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("guesses: ", end="")
    for i in total:
        print(i, end="")
    print()

    score = int((correct / len(questions)) * 100)
    print("ur score: " + str(score) + "%")


def play_again():
    response = input("Play again? (y/n) ").upper()
    if response == "Y":
        return True
    else:
        return False


questions = {
    "Who created python? ": "A",
    "When was it created? ": "B",
    "What is my age? ": "C",
    "Where am i from? ": "D"
}

options = [["A. Guido", "B. Rakib", "C. Jakob", "D. Morse"],
           ["A. 2000", "B. 1991", "C. 2016", "D. 2008"],
           ["A. 18", "B. 19", "C. 20", "D. 21"],
           ["A. pak", "B. ind", "C. aus", "D. bd"]]

new_game()
while play_again():
    new_game()
print("bye")
