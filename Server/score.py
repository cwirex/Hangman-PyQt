from sqlalchemy import Column, INTEGER, VARCHAR, FLOAT
from Server.dbase import Base


class Score(Base):
    __tablename__ = 'score'
    id = Column(INTEGER, primary_key=True)
    game_id = Column(INTEGER)
    nickname = Column(VARCHAR)
    points = Column(FLOAT)

    def __init__(self, game_id, nickname, points):
        self.game_id = game_id
        self.nickname = nickname
        self.points = points
