from sqlalchemy import create_engine

class DBConnectionHandler:
    """ SQLAlchemy DB connection"""


    def __init__(self) -> None:
        self.__connection_string = 'sqlite:///storage.db'
        self.session = None

    def get_engine(self):
        """ Return engine connection """
        engine = create_engine(self.__connection_string)
        return engine