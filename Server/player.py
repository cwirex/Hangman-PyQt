from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN
from Server.dbase import Base


class Player(Base):
    """
    Class representing a player
    """
    __tablename__ = 'player'
    nickname = Column(VARCHAR, primary_key=True)
    email = Column(VARCHAR)
    avatar = Column(INTEGER)
    gender = Column(BOOLEAN)  # 1 - M, 0 - F

    def __init__(self, nickname, email="?", avatar=1, gender=False):
        """
        Initialize the object

        :param nickname:  string representing the player, must be unique
        :param email: string
        :param avatar: integer
        :param gender: boolean True if male, False if female
        """
        self.nickname = nickname
        self.email = email
        self.avatar = avatar
        self.gender = gender

