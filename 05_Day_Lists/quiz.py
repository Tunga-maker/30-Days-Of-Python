print("Welcome to the Quiz App!")

name = input("What is your name? ")
print("Hello, " + name + "! Let's test your knowledge.")

score = 0

questions = [
    "What is the capital of France? ",
    "What is 5 + 3? ",
    "What color is the sky? "
]

answers = [
    "Paris",
    "8",
    "blue"
]

for i in range(len(questions)):
    user_answer = input(questions[i])
    if user_answer == answers[i]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong! The answer is " + answers[i])

print("You scored " + str(score) + " out of " + str(len(questions)))