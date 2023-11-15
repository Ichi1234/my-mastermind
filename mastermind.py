import random

class Boards:

    def __init__(self):
        #user setup
        self.colors_num = int(input("How many colors? (1-8): "))
        while self.colors_num > 8:
            self.colors_num = int(input("How many colors? (1-8): "))

        self.positions_num = int(input("How many positions? (1-10): "))
        while self.positions_num > 10:
            self.positions_num = int(input("How many positions? (1-10): "))
        #color
        self.colors = []
        self.add_colors()

        #The solution is here
        self.answer = ["3", "3", "1", "3"]
        # self.random_answer()

        print(self.answer) ###TODO delete this when finish
        #How many round user play
        self.round = 1

    def add_colors(self):
        for i in range(self.positions_num):
            if i < self.colors_num:
               self.colors.append(str(i+1))
            else:
               self.colors.append(random.randint(1, self.colors_num))

    def random_answer(self):
        for i in range(self.positions_num):
            self.answer.append(random.choice(self.colors))

    def clues(self, user_num):

        list_user = list(user_num)
        user_clues = ""
        if list_user == self.answer:
            return None
        else:
            check = []
            for i in range(len(self.answer)):
                 if list_user[i] == self.answer[i]:
                         user_clues += "0"
                         check.append(list_user[i])
                 elif list_user[i] in self.answer and list_user[i] not in check:
                         user_clues += "X"
                         check.append(list_user[i])
                 else:
                     user_clues += "."

        #swap string place
        random_list = random.sample(user_clues, len(user_clues))
        self.round += 1

        return "".join(random_list)

#main
board = Boards()

while True:
    user_guess = input("What is your guess?: ")
    print(f"Your guess is {user_guess}")
    clue = board.clues(user_guess)
    if clue is None:
        print(f"You solve it after {board.round} rounds")
        print()
        board = Boards()

    else:
        print(clue)
    print()