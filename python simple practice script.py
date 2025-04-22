from datetime import date
import random
from collections import namedtuple
import textwrap

import time

results = [None, None, None, None]  # This list serves to store the last results of each exercise


def main():
    global results
    menu = {"1": "First exercise", "2": "Second exercise", "3": "Third exercise", "4": "Fourth exercise"}  # CREATING
    # THE MENU FROM WHICH THE USER WILL CHOOSE WHICH EXERCISE TO DO
    while True:
        options = menu.keys()
        for entry in options:
            print(entry, menu[entry])
        selection = input("Please select a choice:")
        if selection == '1':  # selecting the first exercise
            results[0] = exercise_1()
            print(results[0])
            menu_2(0, exercise_1)
        elif selection == '2':  # selecting the second exercise
            results[1] = exercise_2()
            print(results[1])
            menu_2(1, exercise_2)
        elif selection == '3':  # selecting the thir exercise
            results[2] = exercise_3()
            print(results[2])
            menu_2(2, exercise_3)
        elif selection == '4':  # selecting the fourth exercise
            results[3] = exercise_4()
            print(results[3])
            menu_2(3, exercise_4)
        else:  # if the user enters a non-valid option
            print("Unknown selection")


def menu_2(exe, exe_fc):  # this is the menu that user will see after doing each exercise
    menu_2 = {"1": "See Results", "2": "Do another exercise", "3": "Do the same exercise", "4": "Terminate "
                                                                                                "the program"}

    while True:
        options_2 = menu_2.keys()
        for entry in options_2:
            print(entry, menu_2[entry])
        selection_2 = input("Please select a choice")
        if selection_2 == "1":  # if the user selects to see the results of exercises
            for i in range(len(results)):
                if results[i] is None:
                    print("You haven't done the exercise number " + str(i + 1) + " yet!")
                else:
                    print(results[i])
        elif selection_2 == "2":  # if the user chooses to return to the main menu of exercises
            return
        elif selection_2 == "3":  # if the user chooses to redo the exercises that he has just done
            results[exe] = exe_fc()
            print(results[exe])
        elif selection_2 == "4":  # if the user chooses to quit/terminate the program
            exit()


############################################################
############################################################
############################################################
############################################################

# EXERCISE 1

def exercise_1():
    print("Welcome to exe1.Input the birthday date in way like this YYYY-MM-DD.\n")

    while True:
        try:
            # ΗΜΕΡ ΑΠΟ ΧΡΗΣΤΗ
            birth = date.fromisoformat((input("BIRTH DATE: ")))

            # ΗΜΕΡ ΓΕΝΝ ΧΡΗΣΤΗ
            print("\nbirth day is : " + str(birth) + "\n")
            today = date.today()

            # ΥΠΟΛΟΓΙΣΜΟΣ ΧΡΟΝΩΝ-ΜΗΝΩΝ-ΗΜΕΡΩΝ
            years = (today - birth).days // 365
            months = ((today - birth).days - years * 365) // 30
            dayz = ((today - birth).days - years * 365 - months * 30)

            # ΕΛΕΓΧΟΣ ΓΙΑ ΜΕΓΑΛΥΤΕΡΗ ΗΜΕΡ ΑΠΟ ΤΗΝ ΤΩΡΙΝΗ
            if (years < 0 or months < 0 or dayz < 0):
                print("try again\n")
                continue
            else:
                return (
                        "your age is " + str(years) + " years ," + str(months) + " months and " + str(dayz) + " days.")

        except ValueError:
            print("try again")
            continue


# EXERCISE 2


class Quiz:
    def __init__(self, list_of_questions, list_of_answers, score):
        self.list_of_questions = list_of_questions  # this is the list of questions that will be displayed as a quiz
        self.list_of_answers = list_of_answers  # this will be used to store the answers of the quiz-taker
        self.score = score  # keeping track of how the user is doing by calculating his/her score

    def next_question(self):  # this will take care of the questions are displayed one after the other
        self.list_of_answers = []  # creating an empty list for the answers that will be given by the user
        for question in self.list_of_questions:
            print(question.question)  # displaying the question
            user_answer = input(question.choices)  # asking the user to answer the displayed question
            flag = False
            while not flag:
                if user_answer not in question.choices:  # if the user enters a non-valid option ie an option not from
                    # (a, b, c or d)
                    print("Please choose a valid option!")
                    user_answer = input(question.choices)  # asking again for a valid answer
                else:  # if the answer is valid
                    flag = True
                    self.list_of_answers.append(user_answer)  # storing the answer in the list of answers created above

    def calc_vathmo(self):
        self.score = 0  # the score is initially equals to zero
        for i in range(5):
            if self.list_of_answers[i] in self.list_of_questions[i][2]:  # if the answer is correct
                self.score += 3  # we add 3 points to the user's score
            else:
                self.score -= 1  # if the answer is wrong we subtract a point from the user's score
        return self.score


def exercise_2():
    full_name = str(input("Please enter your name: "))  # asking the user for his or her fullname
    question = namedtuple("question", "question choices correct")  # the format of the variable question
    list_of_questions = [
        question("What is the last character of the word ΄΄προγραμματισμός΄΄", "a)γ\nb)ς\nc)α\nd)δ\n", {"b", "ς"}),
        question("What is the capital of Greece", "a)Ναύπλιο\nb)Ηράκλειο\nc)Πάτρα\nd)Αθήνα\n", {"d", "Αθήνα"}),
        question("What is the color of an orange", "a)black\nb)yellow\nc)orange\nd)pink\n", {"c", "orange"}),
        question("Greece is a country in what continent", "a)Europe\nb)Africa\nc)Asia\nd)North America\n",
                 {"a", "Europe"}),
        question("How many letters are in the Greek language", "a)23\nb)24\nc)25\nd)26\n", {"b", "24"})]
    mon_quiz = Quiz(list_of_questions, [], 0)  # activating the quiz with the list of questions created above
    mon_quiz.next_question()  # activating the questions to be displayed and taking the user's answers
    score = mon_quiz.calc_vathmo()  # calculating the score
    return full_name + " your score is " + str(score)


# EXERCISE 3


class GUESS:
    def __init__(self, number, guessed_number, number_of_tries):
        self.number = number # the number chosen by the computer
        self.guessed_number = guessed_number # the guessed of the user
        self.number_of_tries = number_of_tries # the number of tries of the user

    def is_bigger(self):
        if self.number < self.guessed_number: # checking if the guess is bigger than the chosen number
            return 1
        else:
            return 0

    def is_smaller(self):
        if self.number > self.guessed_number: # checking if the guess is smaller than the chosen number
            return 1
        else:
            return 0

    def check(self):
        while self.number != self.guessed_number:
            if GUESS.is_bigger(self):
                print("Your guess is bigger, please try again!")
                self.number_of_tries += 1
                self.guessed_number = int(input("Please enter another guess: "))
            elif GUESS.is_smaller(self):
                print("Your guess is smaller, please try again!")
                self.number_of_tries += 1
                self.guessed_number = int(input("Please enter another guess: "))
        return (
                "Congratulations your guess " + str(
            self.guessed_number) + " is correct and you've guessed right in " + str(
            self.number_of_tries + 1) + " tries")


def exercise_3():
    a = int(input("If you want to guess a number that the computer chose enter 1\nIf you want the computer to guess "
                  "a number that you choose enter 2\n"))
    # CASE ONE THE USER WILL BE GUESSING
    if a == 1:
        number = random.randint(1, 100)
        guessed_number = int(input("Please enter your guess: "))
        my_guess = GUESS(number, guessed_number, 0)
        return my_guess.check()
    # CASE TWO THE COMPUTER WILL BE GUESSING
    elif a == 2:
        c = int(input("enter a number from 1 to 100"))
        d = random.randint(1, 100)
        biggest = 100
        smallest = 1
        number_of_tries_of_the_computer = 1
        while c != d:
            small_or_big = str(input("the computer guessed "+str(d)+", if this guess is smaller than your number "
                                                                    "enter the letter s, if it's bigger enter the "
                                                                    "letter b"))
            if small_or_big == "s":
                smallest = d+1
                d = random.randint(smallest, biggest)
                number_of_tries_of_the_computer += 1
            elif small_or_big == "b":
                biggest = d-1
                d = random.randint(smallest, biggest)
                number_of_tries_of_the_computer += 1
            else:
                small_or_big = int(input("please enter the letter s if the guess is smaller or b if it's bigger"))
        return "the computer guess " + str(d) + " is right, number of tries is " + str(number_of_tries_of_the_computer)
    else:
        a = str(input("the choice you've given is incorrect please choose again:\nIf you want to guess a number that "
                      "the computer chose enter 1\nIf you want the computer to guess "
                      "a number that you choose enter 2\n"))


# EXERCISE 4


class Board:
    def __init__(self):
        self.state = ['-'] * 9
        self.game = True
        self.queue = []
        self.sign = ['X', 'O']

    def __str__(self):
        return textwrap.dedent(f"""
            7|8|9\t{self.state[6]} {self.state[7]} {self.state[8]}
            4|5|6\t{self.state[3]} {self.state[4]} {self.state[5]}
            1|2|3\t{self.state[0]} {self.state[1]} {self.state[2]}
        """)

    def add_player(self, player):
        if not self.sign:
            raise Exception("only two players are supported at a time")
        player.sign = self.sign.pop(0)
        self.queue.append(player)

    def change_state(self, move):
        if self.state[move - 1] == '-':
            self.state[move - 1] = self.queue[0].sign
            return True
        else:
            return False

    def run(self):
        print(self)
        while self.game:
            while not self.change_state(self.queue[0].take_input()):
                print("Invalid move, try again")
            print(self)
            if self.win():
                self.game = False
                return self.queue[0].sign + " wins"
            elif self.tie():
                self.game = False
                return 'Tied'
            else:
                self.change_turn()

    def change_turn(self):
        self.queue.append(self.queue.pop(0))

    def win(self):
        check_win = (self.state[2:9:3], self.state[3:6],
                     self.state[0:9:3], self.state[2:7:2],
                     self.state[1:9:3], self.state[6:9],
                     self.state[0:9:4], self.state[:3])

        if [self.queue[0].sign] * 3 in check_win:
            # print(self.queue[0].sign, "wins")
            return True

    def tie(self):
        if '-' not in self.state:
            # print('Tied')
            return True
        else:
            return False


class Player:
    def __init__(self):
        self.sign = None

    def take_input(self):
        spot = ''
        while spot not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            spot = (input(f"Type a number to place {self.sign} "))
        return int(spot)


def exercise_4():
    print("Welcome to exe4.TICTACTOE game.")
    ttt = Board()
    x = ttt.add_player(Player())
    o = ttt.add_player(Player())
    return ttt.run()


main()
