from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


class DataBase(object):

    def __init__(self, url):
        self.engine = create_engine(url)
        self.session_class = sessionmaker(bind=self.engine)

    @property
    @contextmanager
    def session(self):
        session = self.session_class()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_all(self):
        Base.metadata.create_all(self.engine)

    def drop_all(self):
        Base.metadata.drop_all(self.engine)
