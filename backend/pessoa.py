from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+pg8000://postgres@db/catalogo', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'Pessoa'

    # Colunas da tabela.
    id = Column(Integer, primary_key=True)
    nome = Column('nome', String(32))
    sobrenome = Column('sobrenome', String(32))
    email = Column('email', String(32))

    def __init__(self, nome, sobrenome, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email


def save_pessoa(pessoa):
    # Removendo todas as tabelas do banco.
    # Base.metadata.drop_all(engine)

    # Criando todas as tabelas.
    Base.metadata.create_all(engine)

    session = Session()
    session.add(pessoa)
    session.commit()
    session.close()
