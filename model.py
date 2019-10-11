import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

if __name__ == '__main__':
    # time control
    t0 = time.time()

    # Directory Handling
    project_path = os.path.dirname(os.path.abspath(__file__))
    file_path = "/dataset.csv"
    path = project_path + file_path

    # Load to df 100 first rows
    df = pd.read_csv(path, nrows=100)
    print(df.head())

    X = df.iloc[:, 0:47].values
    y = df.iloc[:, 47].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # print("\n X_train")
    # print(X_train)
    # print("\nX_test")
    # print(X_test)
    # print("\ny_train")
    # print(y_train)
    # print("\ny_test")
    # print(y_test)

    regressor = XGBRegressor()
    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)
    loss = y_test - y_pred
    print(loss)
    # time control
    t1 = time.time()
    print("This execution took " + str(t1-t0) + " seconds")
