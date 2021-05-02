import json
from tinydb import TinyDB, Query
from model import player as play
from model import tournoi as tour
import operator

db = TinyDB('chess.json')


class Player:
    '''Class defining a player and its attributes'''

    def __init__(self, name, firstname, date_of_birth, gender, ranking, score, opponents):
        '''This is the class constructor'''

        self.name = name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.opponents = opponents

    def save(self):
        '''This method serialize an instance and save it in the db'''

        serialized_player = {'name': self.name, 'firstname': self.firstname,
                             'date_of_birth': self.date_of_birth, 'gender': self.gender, 'ranking': self.ranking, 'score': self.score, 'opponents': self.opponents}
        players_table = db.table('players')
        players_table.insert(serialized_player)

    def deserialize_players(all_players, list_player):
        '''get the db and deserializes instances of players'''

        for player in all_players:
            list_player.append(Player(
                player['name'], player['firstname'], player['date_of_birth'], player['gender'], player['ranking'], score=0, opponents=[]))

    # get player's infos

    def get_score(self):
        return self.score

    def set_ranking(self, ranking):
        self.ranking = ranking

    def has_match(self, nex_player):
        if next_player in self.opponents:
            return False

    def set_score(self, score):
        self.score += int(score)

    def add_opponents(self, opponent):
        self.opponents.append(str(opponent.name))

    def get_opponents(self):
        return self.opponents
