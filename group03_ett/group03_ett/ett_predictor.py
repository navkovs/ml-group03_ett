"""
Implementation of the decision tree predictor
"""

import pickle

ROTTERDAM_HAMBURG_AGENT = 0
KIEL_GDYNIA_AGENT = 1
ROTTERDAM_HAMBURG = 2
KIEL_GDYNIA = 3


def ett_predictor(latitude, longitude, length, breadth, route):
    """
    The function ett_predictor is at the core of the ETT prediction application. It takes the ship data and loads the trained decision tree and uses the predict method of the trained decision tree class to estimate an expected travel time.

    :param latitude: The current latitude of the ship
    :type latitude: Float
    :param longitude: The current longitude of the ship
    :type longitude: Float
    :param length: Length of the ship
    :type length: Float
    :param breadth: Breadth of the ship
    :type breadth: Float
    :param route: The route of the ship (0: Rotterdam-Hamburg, 1: Kiel-Gdynia)
    :type route: Int
    :return: The estimated travel time (ett).
    :rtype: Float
    """

    ship_data = [length, breadth, latitude, longitude]

    # Route Rotterdam - Hamburg with Agents
    if int(route) == ROTTERDAM_HAMBURG_AGENT:
        # Agent Germany

        # print(longitude)
        # print(type(longitude))

        if longitude >= 7.0:
            with open('group03_ett/rotterdam_hamburg_agent2_germany.pkl', 'rb') as ag2:
                agent2 = pickle.load(ag2).predict([ship_data])
                ett = agent2[0]
                print('Route Rotterdam - Hamburg')
                print("Agent2 Netherlands -> Hamburg: %1.4f." % agent2[0])
        # Agent Netherlands
        else:

            intermediate_port = [length, breadth, 53.83, 7]

            with open('group03_ett/rotterdam_hamburg_agent1_netherlands.pkl', 'rb') as ag1, open('group03_ett/rotterdam_hamburg_agent2_germany.pkl', 'rb') as ag2:
                agent1 = pickle.load(ag1).predict([ship_data])
                agent2 = pickle.load(ag2).predict([intermediate_port])

            print('Route Rotterdam - Hamburg')
            print("Agent1 Rotterdam -> Netherlands: %1.4f." % agent1[0])
            print("Agent2 Netherlands -> Hamburg: %1.4f." % agent2[0])
            ett = agent1[0] + agent2[0]
    # Route Kiel - Gdynia with Agents
    elif int(route) == KIEL_GDYNIA_AGENT:
        if longitude >= 14.0:
            with open('group03_ett/kiel_gdynia_agent2_poland.pkl', 'rb') as ag2:
                agent2 = pickle.load(ag2).predict([ship_data])
                ett = agent2[0]
                print('Route Kiel - Gdynia')
                print("Agent2 Poland -> Gdynia: %1.4f." % agent2[0])
        # Agent Germany Kiel
        else:

            intermediate_port = [length, breadth, 54.65, 14]

            with open('group03_ett/kiel_gdynia_agent1_germanykiel.pkl', 'rb') as ag1, open('group03_ett/kiel_gdynia_agent2_poland.pkl', 'rb') as ag2:
                agent1 = pickle.load(ag1).predict([ship_data])
                agent2 = pickle.load(ag2).predict([intermediate_port])

            print('Route Kiel - Gdynia')
            print("Agent1 Kiel -> Poland: %1.4f." % agent1[0])
            print("Agent2 Poland -> Gdynia: %1.4f." % agent2[0])
            ett = agent1[0] + agent2[0]
    # Route Rotterdam - Hamburg
    elif int(route) == ROTTERDAM_HAMBURG:
        with open('group03_ett/rotterdam_hamburg_ett_predictor.pkl', 'rb') as f:
            rotterdam_hamburg_predictor = pickle.load(f)
        predictor = rotterdam_hamburg_predictor.predict([ship_data])
        ett = predictor[0]
    # Route Kiel - Gdynia
    elif int(route) == KIEL_GDYNIA:
        with open('group03_ett/kiel_gdynia_ett_predictor.pkl', 'rb') as f:
            kiel_gdynia_predictor = pickle.load(f)
        predictor = kiel_gdynia_predictor.predict([ship_data])
        ett = predictor[0]

    return ett
