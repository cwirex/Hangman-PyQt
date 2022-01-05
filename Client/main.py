from Client.game import Game
from Server.dbase import Base, Session, engine

game = Game()


def main():
    # Todo: Aktualizuj kategorie (mainWindow)
    # Todo: Wczytaj hasła
    game.run()


if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
        session = Session()
        session.commit()
        session.close()
        game.set_online()
    except:
        print("Couldn't connect to database, running in offline mode.")
    finally:
        main()
