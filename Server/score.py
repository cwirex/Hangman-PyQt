from sqlalchemy import Column, INTEGER, VARCHAR, FLOAT
from Server.dbase import Base


class Score(Base):
    """
    Class representing the score of a player in a single game
    """
    __tablename__ = 'score'
    id = Column(INTEGER, primary_key=True)
    game_id = Column(INTEGER)
    nickname = Column(VARCHAR)
    points = Column(FLOAT)

    def __init__(self, game_id, nickname, points):
        """
        Initialize object

        :param game_id: integer
        :param nickname: string representing the player
        :param points: integer representing the number of points gained in a given game
        """
        self.game_id = game_id
        self.nickname = nickname
        self.points = points
