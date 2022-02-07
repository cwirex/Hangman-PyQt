from Client.game import Game
from Server.dbase import Base, Session, engine


def main():
    """Runs the game in online or offline mode."""
    game.run()


if __name__ == '__main__':
    game = Game()
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
