from src.infra.config import DBConnectionHandler
from src.infra.entities import Users

class FakerRepo:
    """ inserts value at DB """

    @classmethod
    def inserts_value(cls):
        with DBConnectionHandler() as db_conn:
            try:
                math = Users(name="Matheus", password="Cerozi")
                db_conn.session.add(math)
                db_conn.session.commit()
            except:
                db_conn.session.rollback()
                raise