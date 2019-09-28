import os
import time
import pandas as pd


if __name__ == '__main__':
    # time control
    t0 = time.time()

    # Directory Handling
    project_path = os.path.dirname(os.path.abspath(__file__))
    file_path = "/dataset.csv"
    path = project_path + file_path

    # Load to df 100 first rows
    df = pd.read_csv(path, nrows=100)

    # time control
    t1 = time.time()
    print("This execution took " + str(t1-t0) + " seconds")
