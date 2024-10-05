from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

database_url = 'sqlite:///library.db'
engine = create_engine(database_url)
Base = declarative_base()


class Test(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# new_user = Test(username='Sandy', email='sandy@gmail.com', password='cool-password')
# session.add(new_user)
# session.commit()

# all_users = session.query(Test).all()
# user = session.query(Test).filter_by(username='Sandy').first()

session.close()
