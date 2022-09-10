#!/usr/bin/python3
""" Script that lists all State objects, and corresponding
    City objects, contained in the database hbtn_0e_101_usa """

if __name__ == "__main__":

    import sys
    from relationship_city import Base, City
    from relationship_state import State
    from sqlalchemy.schema import Table
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    s = Session(engine)
    for state in s.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    s.close()
