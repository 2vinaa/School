import random



class Player:
    def __init__(self, name):
        self.name = name
        self.score = random.randint(10, 99)


    def __str__(self):
        return f"{self.name}:{self.score}"



class Scoreboard:
    def __init__(self):
        self.score_player_list = []
        self.len = 0

    def add_to_list(self, user:Player):
        if user not in self.score_player_list:
            self.score_player_list.append(user)
            self.len += 1
        else:
            pass

    def bubblesort(self):
        n = self.len
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.score_player_list[j].score > self.score_player_list[j + 1].score:
                    tmp = self.score_player_list[j + 1]
                    self.score_player_list[j + 1] = self.score_player_list[j]
                    self.score_player_list[j] = tmp

    def __str__(self):
        result = ""
        for element in self.score_player_list:
            result += str(element) + "\n"
        return result




if __name__ == "__main__":
    scoreboard = Scoreboard()
    player1 = Player("Alice")
    player2 = Player("Bob")
    player3 = Player("Charlie")

    scoreboard.add_to_list(player1)
    scoreboard.add_to_list(player2)
    scoreboard.add_to_list(player3)


    print("Before sorting:")

    print(scoreboard)

    scoreboard.bubblesort()

    print("After sorting:")

    print(scoreboard)






