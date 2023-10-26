Sprint 4 - Documentation
========================

Attribute Selection - Attempt 01
--------------------------------

.. image:: /devCreated/images/attributeSelection00.jpg
    :width: 600
    :alt: AttributeSelection
    :align: center

As documented in the table above, as a first attempt to choose the best attributes to use in the algorithm, the attributes resulting in the highest correlation coefficients and lowest error rates were singled out.

The first step was to document the correlation coefficients and error rates with the ETT for each invidual attribute.

The next step was to combine the attributes to maximize the results. An attribute was chosen if a significant improvement of cc and error rate could be oberseved. E.g., the addition of ``"shiptype"`` had only a slight improvement of the root relative squared error in comparison to the preceding run without the attribute. The other values were unchanged, so the attribute was not chosen.

For the last step, the best run from the second step (highlighted in green) was used as a starting point to reduce the amount of attributes. Each attribute was omitted successively to document the changes in cc and error rates for all the attributes. The ones with the least changes in results were thrown out of the selection (highlighted in blue).

The resulting attribute selection (highlighted in red) were the attributes ``"TripID", "ID", "Latitude" and "Longitude"``, since they showed the highest correlation coefficient with the ETT in these tests.

Attribute Selection - Attempt 02
--------------------------------

.. image:: /devCreated/images/attributeSelection01.jpg
    :width: 600
    :alt: AttributeSelection
    :align: center

After cleaning the data once again and rerunning the tests, we came to the conclusion, that the best combination for this project will be a Decision Tree with the following attributes: ``Longitude, Latitude, Length, Breadth``

Implementation of the algorithm in python
-----------------------------------------
Before implementing the algorithm some research was needed. We decided to make use of the SciKit-learn library as it is widely used in the
domain of machine learning, so we had a more detailed look into it. Some straightforward implementations of decision trees are given in the library, the one that suited
our needs was the class ``sklearn.tree.DecisionTreeRegressor``. After some more cleaning of the data — we realised that some
vessels took quite long detours off the actual route — we started to train the decision tree, one for each route. The training was done using
dedicated Jupyter Notebooks.
|  The class ``sklearn.tree.DecisionTreeRegressor`` features the method ``score(X, Y)`` which returns the coefficient of determination. This coefficient can be used as
measure of the quality of a machine learning model. For the two routes the trained decision trees yielded the following score values:

- Route Rotterdam-Hamburg: ``0.6038089344665416``
- Route Kiel-Gdynia: ``0.7227987292846649``

The trained models were saved into separate ``.pkl`` files using the ``pickle`` library. Finally we created the module ``ett_predictor.py``
which contains the function ``ett_predictor()``. The function is called from the main module with the ship data (latitude, longitude, etc.)
as its arguments. It then opens the ``.pkl`` file with the corresponding decision tree for the route and uses the method ``predict()`` to
make the actual prediction of the ETT. This predicted value is then returned.

Implementating the agents
--------------------------
In order to implement the the predictor with another approach, namely using multiple predictor agents, we decided to split up both routes into
two sections so that one predictor agent is responsible for first section and and the second one is responsible for the second section.
To achieve this we also split the data sets in half. One predictor agent would be trained with the data corresponding to the first section,
the other one with the second half. Therefore the data of the first section needed to be equipped with a new attribute, some kind of
intermediate ETT which denotes the remaining travel time to the border of the section. A prediction for input data that lies in the first
seciton of a route is carried out as follows: The trained predictor estimates the ETT to the border of the first section. Then the predictor
agent for the second section takes data corresponding to the beginning of the section as input. In the end both predicted ETTs are added together.
This solution is kind of hardcoded as the second agent always takes the same input coordinates. We did this because we lacked time to find a
reasonable solution to the problem where the exact route of the vessel in question would go when crossing the border of the sections.

Nevertheless, using the approach of multiple predictor agents we managed to increase the accuracy of the model. The ``score`` values for the
individual agents were:

- Route Kiel-Gdynia, Agent 1: ``0.9569165686751772``
- Route Kiel-Gdynia, Agent 2: ``0.8709330809757087``
- Route Rotterdam-Hamburg, Agent 1: ``0.8743892135061015``
- Route Rotterdam-Hamburg, Agent 2: ``0.7737632680572061``

Decisions on the GUI
--------------------
The attributes we use to predict the ETT are latitude, longitude, length and breadth. Therefore we decided to only display these for historical
trip data.

Put Dots on Map
---------------

- Use Jupiter to delete Columns except Latitude, Longitude, ETT, TripID.
- Filter for unique Values. ``sort -u kiel_gdynia_coords.csv > kiel_gdynia_coords_unique.csv``
- Take random Values from all Values to display. ``sort -R kiel_gdynia_coords_unique.csv | head -n 500 > kiel_gdynia_coords_random.csv``
- Convert to Javascript in be included in index.html. This is done by regex replacement.

    - ``(\d+),(\d+.\d+,\d+.\d+),(\d*)(\.*\d*)`` to ``L.marker([$2], {icon: img_dot}).addTo(routeKiel).bindPopup("<b>Coords: $2</b><br>Trip-ID: $1<br>Travel Time: $3 min");``
