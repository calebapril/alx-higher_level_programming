#!/usr/bin/python3
""" Script that lists all City objects from the database hbtn_0e_101_usa """

if __name__ == "__main__":

    import sys
    from sqlalchemy.schema import Table
    from relationship_city import Base, City
    from relationship_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    s = Session(engine)
    for city in s.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    s.close()
