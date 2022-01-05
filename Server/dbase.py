from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgres_acc = 'postgresql://student2:st2021%2@212.182.24.105:15432/student2'

engine = create_engine(postgres_acc)
Session = sessionmaker(bind=engine)
Base = declarative_base()


