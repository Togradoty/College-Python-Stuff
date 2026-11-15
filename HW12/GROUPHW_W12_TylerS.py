import random

def main():
    #reads file and creates the dictionary
    capitals = {}
    file = open("state_capitals.txt", "r")

    for line in file:
        state, capital = line.split()
        capitals[state] = capital

    file.close()

    # displays dictionary
    print(capitals)

    correct = 0
    incorrect = 0
    states = list(capital.keys())

    #asks for five random questions
    for question in range(5):
        state = random.choice(states)
        states.remove(state)

        answer = input(f"What is the capital of {state}: ")

        #check if answer correct or wrong
        if answer.strip().lower() == capitals[state].lower():
            correct += 1
        else:
            incorrect += 1

    #displays result
    print(f"You answered {correct} state capitals correctly.")
    print(f"You answered {incorrect} state capitals incorrectly.")

if __name__ == "__main__":
    main()