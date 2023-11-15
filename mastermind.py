import random

class Boards:

    def __init__(self):
        self.colors = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.answer = [random.choice(self.colors),random.choice(self.colors),
                       random.choice(self.colors), random.choice(self.colors)]
        print(self.answer) ###TODO delete this when finish
        self.round = 1
    def clues(self, user_num):
        list_user = list(user_num)

        user_clues = ""
        if list_user == self.answer:
            return None
        else:
            for i in range(len(self.answer)):
                 if list_user[i] == self.answer[i]:
                         user_clues += "0"
                 elif list_user[i] in self.answer:
                         user_clues += "X"
                 else:
                     user_clues += "."
        random_list = []
        list_user_clue = list(user_clues)
        for j in range(len(user_clues)):
            random_choice = random.choice(list_user_clue)
            list_user_clue.remove(random_choice)
            random_list.append(random_choice)
        self.round += 1

        return "".join(random_list)


###TODO Make user setup
# colors_num = input("How many colors? ")
# positions_num = input("How many positions? ")

# print(f"Playing Mastermind with {colors_num} colors and {positions_num} positions")

board = Boards()
while True:
#    user_guess = input("What is your guess ")
#    print(f"Your guess is {user_guess}")


    user_guess = input("What is your guess ")
    print(f"Your guess is {user_guess}")
    clue = board.clues(user_guess)
    if clue is None:
        print(f"You solve it after {board.round} rounds")
        board = Boards()
    else:
        print(clue)
    print()