"""
Module - main.py

Description -
    Contains the entire code flow. taking user inputs and output data
    plots and information related to the stock

Author - Siril Ganjai

Version - 1.0.0

Date 3-25-2021
"""
import package.Fetch_Stock_Data as FS
import package.Stock_Predict as Predict

if __name__ == "__main__":
    #This comment part will be removed in the final submission.
    #Stock_File = r"C:\Users\siril\Desktop\CMSE 802_1\My_CMSE_Git\Stock_Predictor\Data\GOOG.csv"
    Stock_File = input("Input you stock file to be predicted : ")
    stock_raw_data = FS.preprocess_price_data(Stock_File)
    algo = int(input("Choose the Algo you want to use : \n 1. ARIMA \n 2. LSTM \n"))

    print('algo chosen is - ', algo)
    if algo == 1:
        Predict.predict_arima(stock_raw_data)
    else:
        print("Wrong Input Given")
