import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pickle

#load the dataset
data=pd.read_csv("Salary Data.csv")

print(data.head())


# plot the salary 
plt.scatter(data['YearsExperience'] , data["Salary"])
plt.xlabel("years of experience")
plt.ylabel("Salary")
plt.title("EXP VS SALARY")
plt.show()



# will Build the model 





#train test split

x= data[["YearsExperience"]]
y=data["Salary"]

x_train, x_test , y_train, y_test  =train_test_split(x, y, test_size=0.2, random_state=42)

#train the mode 

model = LinearRegression()
model.fit(x_train, y_train)

# model predictions
y_pred=model.predict(x_test)

#evaluation Mean squared error 
mse= mean_squared_error(y_test , y_pred)

print(f"MEAN SQUARED ERROR : {mse}")



# save the pickle file 

with open ('salary_model.pkl', "wb") as f:
    pickle.dump(model, f)

