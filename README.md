To run the program type "python main.py" in the terminal.

All library files are in "include" folder. As of 12 October 2020 only data_management.py is working perfectly. data_management.py contains all the modules needed for data management. It is meant to be run as an independent process--so it is run on a different terminal.


All the data is stored in "data" folder. Data is stored in csv files. data folder has a "snapshots" subfolder which contains all the information at that given time only. Each csv file in snapshots folder's name is a precise time denoting the time at which the snapshot was taken. The data folder maintains two other csv files namely current.csv and all_data.csv. As the name suggests current.csv contains the latest snapshot and all_data.csv contains all the dataframe containing all the snaphosts since the server was started. There should be about 1609 columns in dataframe

The "test" folder contains files that are useful for testing different python modules and APIs before integrating them into the main modules. 
