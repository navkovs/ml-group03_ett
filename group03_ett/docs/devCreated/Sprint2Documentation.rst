Sprint 2 - Documentation
========================

Linear regression in weka
-------------------------

Correlated values can be removed by the setting ``elminatecolinearattributes`` to ``True``
Feature selection only to relevant setting the ``attributeSelectionMethod``
For linear regression the type of attributes must be numerical.
Cleaning the data:

- Delete instances with missing values with applying unsupervized.attribute.ReplaceMissingValues , choosing the attribute index with missing percentage and setting matchMissingValues to “True” then applying the filter
- Removing columns with strings that have other than numerical types(but doesn’t rlly make sense because we need StartTime for example)
- Changing type from string to numerical by using the filter StringToNominal on the attributes.

**General Overview over the Attributes**

- Number of Instances: 1378726
- Attributes: 25

Choosing features: We are still trying to aim for lowest error by adding features or removing them.

- Number of Instances: 1378726
- Attributes: 25

    - TripID (M: 0/ D:980) [numeric]: Identifier for the different trips.
    - MMSI (M: 0/ D:361) [numeric]: Identifier for the different ships.
    - StartLatitude (M: 0/ D:27) [numeric]: StartLat of this instance.
    - StartLongitude (M: 0/ D:57) [numeric]: StartLong of this instance.
    - StartTime (M: 0/ D:898) [date]: StartTime of this instance.
    - EndLatitude (M: 0/ D:18) [numeric]: EndLat of this instance.
    - EndLongitude (M: 0/ D:24) [numeric]: EndLong of this instance.
    - EndTime (M: 0/ D:890) [date]: EndTime of this instance.
    - StartPort (M: 0/ D:1) [string]: Starting Port -> Have to redo into numerical.
    - EndPort (M: 0/ D:1) [string]: End Port -> Have to redo into numerical.
    - ID (M: 0/ D:1118007) [numeric]: Not sure. May have to ask again.
    - time (M: 0/ D:443675) [date]: Actual time of the instance.
    - shiptype (M: 0/ D:17) [numeric]: Type of ship.
    - Length (M: 0/ D:135) [numeric]: Info on ship.
    - Breadth (M: 0/ D:46) [numeric]: Info on ship.
    - Draught (M: 60793/ D:325) [numeric]: Info on ship.
    - Latitude (M: 0/ D:985) [numeric]: Position of ship.
    - Longitude (M: 0/ D:2001) [numeric]: Position of ship.
    - SOG (M: 0/ D:249) [numeric]: Info on ship. Speed over ground.
    - COG (M: 0/ D:3602) [numeric]: Info on ship. Course over ground (angle).
    - TH (M: 0/ D:361) [numeric]: Info on ship.
    - Destination (M: 11800/ D:199) [string]: Have to convert to string.
    - Name (M: 11685/ D:367) [string]: Name of ship. Should be irrelevant.
    - Callsign (M: 11798/ D:387) [string]: Name of ship. Should be irrelevant.
    - AisSourcen (M: 42074/ D:177) [string]: Automatic identification system. May have to convert.


We run the classification of Linear Regression and click start::

    Result of testing (example) :
    === Run information ===

    Scheme:       weka.classifiers.functions.LinearRegression -S 0 -R 1.0E-8 -num-decimal-places 4
    Relation:     AIS_rotham-weka.filters.unsupervised.instance.RemoveWithValues-S0.0-C16-Lfirst-last-M-weka.filters.unsupervised.attribute.Remove-R5,8-10,12,22-25
    Instances:    1317933
    Attributes:   16
                TripID
                MMSI
                StartLatitude
                StartLongitude
                EndLatitude
                EndLongitude
                ID
                shiptype
                Length
                Breadth
                Draught
                Latitude
                Longitude
                SOG
                COG
                TH
    Test mode:    evaluate on training data

    === Classifier model (full training set) ===


    Linear Regression Model

    Draught =

        -0      * TripID +
        0      * MMSI +
        5.8179 * StartLatitude +
        -1.1488 * StartLongitude +
        -4.7498 * EndLatitude +
        1.4095 * EndLongitude +
        -0      * ID +
        -0.0242 * shiptype +
        0.0111 * Length +
        0.0765 * Breadth +
        -0.0668 * Latitude +
        0.0107 * Longitude +
        0.0073 * SOG +
        0.0025 * COG +
        -0.0028 * TH +
        -47.8409

    Time taken to build model: 3.44 seconds

    === Evaluation on training set ===

    Time taken to test model on training data: 0.96 seconds

    === Summary ===

    Correlation coefficient                  0.9136
    Mean absolute error                      0.8427
    Root mean squared error                  1.1273
    Relative absolute error                 37.8281 %
    Root relative squared error             40.6718 %
    Total Number of Instances          1317933


Running algorithm on another test data ``kiel``::

    === Run information ===

    Scheme:       weka.classifiers.functions.LinearRegression -S 0 -R 1.0E-8 -num-decimal-places 4
    Relation:     AIS-weka.filters.unsupervised.instance.RemoveWithValues-S0.0-C16-Lfirst-last-M-weka.filters.unsupervised.attribute.Remove-R5,8-10,12,22-25
    Instances:    743566
    Attributes:   16
                TripID
                MMSI
                StartLatitude
                StartLongitude
                EndLatitude
                EndLongitude
                ID
                shiptype
                Length
                Breadth
                Draught
                Latitude
                Longitude
                SOG
                COG
                TH
    Test mode:    evaluate on training data

    === Classifier model (full training set) ===


    Linear Regression Model

    StartLatitude =

        0      * TripID +
        -0      * MMSI +
        0.544  * StartLongitude +
        -0.011  * EndLatitude +
        -0.0039 * EndLongitude +
        -0      * ID +
        -0.0001 * shiptype +
        -0      * Length +
        0.0002 * Breadth +
        -0.0003 * Draught +
        -0.0014 * Latitude +
        -0.0004 * Longitude +
        0      * SOG +
        0      * COG +
        -0      * TH +
        49.6006

    Time taken to build model: 1.25 seconds

    === Evaluation on training set ===

    Time taken to test model on training data: 0.58 seconds

    === Summary ===

    Correlation coefficient                  0.8607
    Mean absolute error                      0.0033
    Root mean squared error                  0.0088
    Relative absolute error                 88.9783 %
    Root relative squared error             50.9233 %
    Total Number of Instances           743566

    All in all, linear regression takes only a short time to compute but still has a high error rate. If we clean the data more, the error rate should go down.

    k-nearest neighbour in weka
    ---------------------------

The test we ran did not end computation at the moment. We first started with cross-validation with 10 folds which worked fine for linear regression, but this did not finish for hamburg-rotham in reasonable time.

Next we tried percentage split and this computed 25000 instances in 30 min. So it is very slow in relation to linear regression.