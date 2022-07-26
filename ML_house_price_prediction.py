import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
mel_data = pd.read_csv('melb_data.csv')
mel_data = mel_data.dropna(axis=0)
# mel_data.describe()
# target Variable
y = mel_data.Price
# Features 					
feature_list = ['Rooms','Landsize',	'BuildingArea',	'YearBuilt','Bathroom','Distance','Car','Postcode','Bedroom2','Propertycount']
x = mel_data[feature_list]
# x.head()
#splitting data for training and teesting to overcome the issues of overfitting and underfitting
train_x, test_x ,train_y , test_y = train_test_split(x,y,random_state=1)
#making a model
price_model = DecisionTreeRegressor()
price_model.fit(train_x,train_y)
predictions = price_model.predict(test_x)
predictions
# knowing the error through MAE of decision tree
from sklearn.metrics import mean_absolute_error as MAE

model_val_mae = MAE(predictions,test_y)

print("Validation MAE for Decision Tree Model: {:,.0f}".format(model_val_mae))