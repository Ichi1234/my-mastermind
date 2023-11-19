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
        self.answer = []
        self.random_answer()

        #How many round user play
        self.round = 1

    def add_colors(self):
        """add number correspond with user_amount of number"""
        for i in range(self.positions_num):
            if i < self.colors_num:
               self.colors.append(str(i+1))
            else:
               self.colors.append(random.randint(1, self.colors_num))

    def random_answer(self):
        """random solution from colors in self_colors"""
        for i in range(self.positions_num):
            self.answer.append(random.choice(self.colors))

    def clues(self, user_num):
        """give clue to user"""
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
                 elif list_user[i] in self.answer and self.answer.count(list_user[i]) >= list_user.count(list_user[i]):
                         user_clues += "X"
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
    while len(user_guess) != len(board.answer):
        print(f"Your input need to have only {board.positions_num} character.")
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