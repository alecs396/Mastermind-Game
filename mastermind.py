"""The nim module contains the classes for playing the Nim strategy game.

Worked with Nathan Page and group 4

Author(s):  Alec Swainston
"""
import random


class Game:
    """A period of turn-based play ending in a definate result. The 
    responsibility of Game is to control the sequence of play.
    
    Stereotype: Controller
    """
    def play(self):
        official = Official()
        players = []
        boards = [Board(), Board()]
        _next = 0
        
        official.register(players)
        while not boards[0].is_solved() and not boards[1].is_solved():
            official.display(boards)
            player = players[_next]
            board = boards[_next]
            player.make_move(board)	
            official.check(board, player)
            _next = (_next + 1) % len(players)


class Player:
    """A person taking part in a game. The responsibility of Player is to make 
    moves and keep track of their identity.
    
    Stereotype: Information Holder
    """
    def __init__(self, _id, name):
        self._id = _id
        self._name = name
        
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name
    
    def make_move(self, board):
        print(f"{self._name}'s turn:")
        user_guess = str(input(f"Enter your guess: "))
        guess = (user_guess)
        board.update(guess)

    
class Board:
    """A designated area for playing a game. The responsibility of Board is 
    to keep track of the items in play.
    
    Stereotype: Information Holder
    """
    def __init__(self):
        # a tuple of a random number to be guessed
        # generate two random numbers for the players to guess
        code = random.randint(1000, 9999)
        self._code = str(code)
        self._guess = "----"
        self._hint = "****"

    def get_codes(self):
        return self._code

    def is_solved(self):
        return self._code == self._guess

    def update(self, guess):
        self._guess = guess
        self._hint = self._create_hint()


    def _create_hint(self):
        hint = ""
        for index, letter in enumerate(self._guess):
            if self._code[index] == letter:
                hint += "x"
            elif letter in self._code:
                hint += "o"
            else:
                hint += "*"
        return hint


class Official:
    """A person who officiates in a game. The responsibility of Official is to 
    perform special duties including: check if there's a winner, display the 
    board and register players.
    
    Stereotype: Service Provider
    """
    def check(self, board, player):
        if board.is_solved():
            name = player.get_name()
            print(f"\n{name} won!")

    def display(self, boards):
        text =  "\n--------------------"
        for i in range(2):
            _id = i + 1
            text += (f"\nPlayer {_id}: {boards[i]._guess}, {boards[i]._hint}")  
        text += "\n--------------------"
        print(text)

    def register(self, players):
        for i in range(2):
            _id = i + 1
            name = input(f"Player {_id} name: ")
            player = Player(_id, name)
            players.append(player)

    
if __name__ == "__main__":
    game = Game()
    game.play()