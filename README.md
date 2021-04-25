# Introduction -

The Project is related to predicting future stock prices. We give an input data related to time forecasting series and we choose the best fit model and test it on some values. We also predict the future values if the model fits for the test data.
For machine learning algorithms in general, we divide the train and test data to 80% and 20% in general. We cannot do the same for this project or any project related to time forecasting. The reason is this type of data is time dependent. It changes with time, so dividing the data in random would lead the model to erratic behavior. Here data is dependent on time and previous data. the stock price of the today is dependent on previous data or previous behavior of data (In reality, It has much more number of factors). 
In such case, we train the model with first 80% of the data. test it with the 20% of the latest data. Predict the next 5 or 6 values based on the parameter we pass to the forecast function.


# Project Goals and Progress -

The main goal is to make a time forecasting project that include 2 time forecasting strategies. For now, ARIMA is included in the project and working on including LSTMs. 
This project will be open for contributions. Meaning users can upload their own model in a single .py file to git, make changes to the code in main.py and get the results. The whole code is put in github.com and I encourage everyone to download, contribute and make better versions.

github link - https://github.com/8-bit-owl/Not_a_StockPredcitor.git


# Running the Code - 

For running the code, we need to run main.py. It has all the code flow as per current build. For now, only ARIMA algorithm has been implemented and the present goal is to work in integrating LSTM models into the code. Steps to be followes for running the code - 
1. cmd -> python main.py
2. It will ask you to provide the stock file. provide the file path, including the path\filename.csv
3. It will ask you to select the algorithm. Choose ARIMA, by pressing 1 and hit Enter.
4. It will give you plots and also future prediction. 

# Unit Testing -
For unit testing, there are 3 .py files with name starting with "test_"
to run test a module, follow the below steps - 
1. Open command line
2. run the command cd package
3. run the command cd test
4. run the command >>python -m unittest test_filename.py

For this project, the commands would be - 

cd package\test
python -m unittest test_Fetch_StockData.py
python -m unittest test_Plot_Stocks
python -m unittest test_Stock_Predict


More information and tutorial can be found in the Tutorial.ipynb. Happy Investing :)
