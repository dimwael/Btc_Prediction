# Bitcoin Prediction
Using Tpot and Skitlearn to predict Bitcoin Value

# My Approach

The Bitcoin Dataset on Quandl contains several data about the development of the famous crypto currency Bitcoin. I chose to study and predict it's behaviour.
I will study as well the monthly average growth. 

I chose to use Quandlto get the data and stock it in the file , btckraken.csv , which contains many information about bitcoin for days, months from 2014-2018 (February 18th). Here is my process:

    I cleaned the data using the script dataCleaning.py,after i've collected them throught Quandl, to produce a .csv file with features that I wanted TPOT to use and no missing data. The main feature I was interested in was the date (dt, in the original data file). I split the date column in to year, month and day. Here, I also renamed the target variable ('Weighted Price') as 'class'. The output is 'cleaned_btc_kraken.csv'.

    I created a "fake" .csv file containing the years and months for which I wanted to make Bitcoin value predictions. This .csv file is called global_test.csv. The original data only runs until the year 2018, so in order to predict weighted value for the next 2 years, my test file contains dates for 2018-2020.

    I wrote the script Genetic_Algo_Prediction.py that read in the cleaned data, and applied the TPOT library to create a machine learning pipeline for predicting temperatures. This script also takes the test file of dates for which the values should be predicted (global_test.csv), and outputs the results file with these predictions. It also outputs the TPOT optimized pipeline.

    I used the outputted, optimized pipeline to see how it would perform when asked to predict monthly value on the original data. I did this in predict_btc.py to produce original_data_predictions.csv.

    With all of the predictions from the optimized pipeline, I created some visualizations to understand TPOT's performance, and the climate data.

#### Please don't forget to put your own Quandl Api Key

# Result
The resulting optimized pipeline from TPOT implemented FeatureAgglomeration and GradientBoostingRegressor, scoring 0.6283690079003942 MSE on the cross-validation portion of the training data.

The original data set (cleaned), shows that the Bitcoin value is gradually decreasing in the first 3 months of the year and then become gradually increasing to attend the maximum growth in the last 2 months of the year 
![alt text](https://github.com/dimwael/Btc_Prediction/blob/master/actualValue.png)

The Predicted model gave the same behaviour 
![alt text](https://github.com/dimwael/Btc_Prediction/blob/master/PredictedValue.png)


#### Prediction for the 2020
![alt text](https://github.com/dimwael/Btc_Prediction/blob/master/Prediction2020.png)
