from tinydb import TinyDB


db = TinyDB('chess.json')


class Player:
    '''Class defining a player and its attributes'''

    def __init__(self, name, firstname, date_of_birth, gender, ranking, score=0, opponents_name=[]):
        '''This is the class constructor'''

        self.name = name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.score = score
        self.opponents_name = opponents_name

    def save(self):
        '''This method serialize an instance and save it in the db'''

        serialized_player = {'name': self.name, 'firstname': self.firstname,
                             'date_of_birth': self.date_of_birth, 'gender': self.gender,
                             'ranking': self.ranking, 'score': self.score,
                             'opponents': self.opponents_name}
        players_table = db.table('players')
        players_table.insert(serialized_player)

    def deserialize_players(list_of_players):
        '''get the db and deserializes instances of players'''
        deserialized_list = []
        for player in list_of_players:
            deserialized_list.append(Player(
                player['name'], player['firstname'], player['date_of_birth'],
                player['gender'], player['ranking'], player['score'], player['opponents'], player['opponents_name']))
        return deserialized_list

    def get_score(self):
        '''To make appear the score of a player'''
        return self.score

    def set_ranking(self, ranking):
        '''method to change the ranking of a player'''
        self.ranking = ranking

    def set_score(self, score):
        '''method to change the score of a player'''
        self.score += float(score)

    def add_opponents(self, opponent):
        '''method to add an opponents to the player's list'''
        self.opponents_name.append(str(opponent.name))

    def get_opponents(self):
        '''return the list of a payer's passed opponents'''
        return self.opponents_name

    def check_max_player(list_of_players):
        '''method to verify if the number of players
        is a adequation with the tournaments attribute
        about the number of players needed'''
        if len(list_of_players) == 8:
            return True

    def load_player(name):
        '''this method loads an instance of player from is name
        chosing the right one in the db'''
        player_table = db.table('players')
        players = player_table.all()
        for player in players:
            if player['name'] == str(name):
                target = Player(name=player['name'], firstname=player['firstname'],
                                date_of_birth=player['date_of_birth'],
                                gender=player['gender'], ranking=player['ranking'],
                                score=player['score'], opponents_name=player['opponents'])
                return target
