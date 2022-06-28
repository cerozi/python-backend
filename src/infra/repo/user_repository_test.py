from src.infra.repo import UserRepository
from src.infra.config import DBConnectionHandler
from faker import Faker


faker = Faker()
user_repo = UserRepository()
db_conn = DBConnectionHandler()

def test_insert_user():
    """tests an user insertion at DB"""

    name = faker.name()
    password = faker.word()
    engine = db_conn.get_engine()

    new_user = user_repo.inserts_value(name=name, password=password)
    query_user = engine.execute(f"SELECT * FROM users WHERE id={new_user.id}").fetchone()

    engine.execute(f"DELETE FROM users WHERE id={new_user.id}")

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password


