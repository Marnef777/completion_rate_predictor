import os
import time
import pandas as pd


if __name__ == '__main__':

    # time control
    t0 = time.time()

    # Directory Handling
    project_path = os.path.dirname(os.path.abspath(__file__))
    full_file_path = "/original_dataset.csv"
    full_file = project_path + full_file_path
    new_full_file_path = "/dataset.csv"
    new_full_file = project_path + new_full_file_path

    # Header for df
    header_i = 0
    header_list = []
    for header_i in range(0, 50):
        if (header_i == 2):
            header_list.append("form_id")
            header_list.append("views")
            header_list.append("submissions")
        elif (header_i > 2):
            header_list.append("feature_"+str(header_i-2))
        else:
            pass
        header_i += 1

    # Df reading, wrangling and writing in new csv
    df = pd.read_csv(full_file, sep='[-]|[,]', engine='python', header=None)
    df = df.replace(['\(', '\)'], ['', ''], regex=True)
    df.columns = header_list

    df["conversion_rate"] = df["submissions"]/df["views"]
    df.drop(["form_id", "submissions", "views"], axis=1, inplace=True)

    df.to_csv(new_full_file, index=False)

    # time control
    t1 = time.time()
    print("This execution took " + str(t1-t0) + " seconds")
