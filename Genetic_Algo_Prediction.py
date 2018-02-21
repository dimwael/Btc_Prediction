import pandas as pd
import numpy as np
from tpot import TPOTRegressor
from sklearn.model_selection import train_test_split

# open files
test = np.genfromtxt('global_test.csv',delimiter=',',skip_header=1)
train = np.genfromtxt('cleaned_btc_kraken.csv',delimiter=',',skip_header=1)

#Create a copy of training without class
train_new = np.delete(train,0,1)

#Get list of class variables
train_class = train[:,0]

#Split the data inti training and testing sets
x_train,x_test, y_train ,y_test = train_test_split(train_new, train_class, train_size=0.75, test_size=0.25)

#Instantiate tpot instance
tpot = TPOTRegressor(verbosity=3, generations=10, population_size=50)

#call fit function
tpot.fit(x_train, y_train)

#call the score function on cv data
print('TPOT score: {}'.format(tpot.score(x_test, y_test)))

#Predict temps for each month for next 5 years
submission = tpot.predict(test)

#create dataframe of results for each month/years
final = pd.DataFrame ({'year': test[:,0],'month':test[:,1],'Pred':submission})

#export pipeline
export_filename = 'BTC Pipeline.py'
tpot.export(export_filename)

#export predicted values
final_filename = 'btc_pred.csv'
final.to_csv(final_filename, index=False)
