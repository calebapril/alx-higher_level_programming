#!/usr/bin/python3
""" Script that creates the State “California” with the City
    “San Francisco” from the database hbtn_0e_100_usa """

if __name__ == "__main__":

    import sys
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    s = Session(engine)
    news = State(name='California')
    newc = City(name='San Francisco')
    news.cities.append(newc)
    s.add_all([news, newc])
    s.commit()
    s.close()
