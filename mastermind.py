import random

class Boards:

    def __init__(self):
        self.colors = [1, 2, 3, 4, 5, 6, 7, 8]
        self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # self.answer = [random.choice(self.colors),random.choice(self.colors),
        #                random.choice(self.colors), random.choice(self.colors)]
        self.answer = ["1", "2", "3", "4"]
    def clues(self, user_num):
        list_user = list(user_num)

        user_clues = ""
        if list_user == self.answer:
            return "WIN"
        else:
            for i in range(len(self.answer)):
                 if list_user[i] == self.answer[i]:
                         user_clues += "0"
                 elif list_user[i] in self.answer:
                         user_clues += "X"
                 else:
                     user_clues += "."
        return user_clues


###TODO Make user setup
# colors_num = input("How many colors? ")
# positions_num = input("How many positions? ")

# print(f"Playing Mastermind with {colors_num} colors and {positions_num} positions")

# while True:
#    user_guess = input("What is your guess ")
#    print(f"Your guess is {user_guess}")
board = Boards()
user_guess = input("What is your guess ")
print(f"Your guess is {user_guess}")
print(board.clues(user_guess))