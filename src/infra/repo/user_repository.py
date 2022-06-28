from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users

class UserRepository:
    """inserts value at DB"""

    InsertData = namedtuple("Users", ["id", "name", "password"])

    @classmethod
    def inserts_value(cls, name: str, password: str):
        with DBConnectionHandler() as db_conn:
            try:
                new_user = Users(name=name, password=password)
                db_conn.session.add(new_user)
                db_conn.session.commit()

                return cls.InsertData(id=new_user.id, name=new_user.name, password=new_user.password)
            except:
                db_conn.session.rollback()
                raise