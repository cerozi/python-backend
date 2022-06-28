from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    """ SQLAlchemy DB connection"""

    def __init__(self) -> None:
        self.__connection_string = 'sqlite:///storage.db'
        self.session = None

    def get_engine(self):
        """ Return engine connection """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = self.get_engine()
        session_local = sessionmaker(engine)
        self.session = session_local()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()