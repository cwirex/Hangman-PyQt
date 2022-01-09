from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN
from Server.dbase import Base


class Player(Base):
    __tablename__ = 'player'
    nickname = Column(VARCHAR, primary_key=True)
    email = Column(VARCHAR)
    avatar = Column(INTEGER)
    gender = Column(BOOLEAN)  # 1 - M, 0 - F

    def __init__(self, nickname, email="?", avatar=1, gender=False):    # try, except
        self.nickname = nickname
        self.email = email
        self.avatar = avatar
        self.gender = gender

