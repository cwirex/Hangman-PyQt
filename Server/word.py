from sqlalchemy import Column, INTEGER, VARCHAR
from Server.dbase import Base


class Word(Base):
    __tablename__ = 'word'
    id = Column(INTEGER, primary_key=True)
    word = Column(VARCHAR)
    category = Column(VARCHAR)

    def __init__(self, word, category):
        self.word = word
        self.category = category
