import os
import time
import pandas as pd
import json
import collections


if __name__ == '__main__':
    # time control
    t0 = time.time()

    feat = False
    conv_rate = True

    # Directory Handling
    project_path = os.path.dirname(os.path.abspath(__file__))
    file_path = "/dataset.csv"
    path = project_path + file_path

    if (feat):
        exploratory_dict_path = project_path + "/exploratory_feat.json"
        # Load df
        df = pd.read_csv(path)

        # List of features and exploratory analysis of feature values
        features = []
        for i_f in range(1, 48):
            features.append("feature_"+str(i_f))
        feature_count_dict = {}
        for feature in features:
            feature_count_dict[feature] = df[feature].value_counts().to_dict()

        with open(exploratory_dict_path, mode='w') as w:
            json.dump(feature_count_dict, w, sort_keys=False, indent=4)

    elif (conv_rate):
        exploratory_dict_path = project_path + "/exploratory_conv_rate.json"
        # Load df
        df = pd.read_csv(path, nrows=100)

        feature_count_dict = {}
        feature_count_list = df["conversion_rate"].tolist()
        sort_list = sorted(feature_count_list)
        print(sort_list)
        # feature_count_dict["conversion_rate"] = df["conversion_rate"].value_counts().to_dict()
        #
        # od = collections.OrderedDict(sorted(feature_count_dict.items()))
        # with open(exploratory_dict_path, mode='w') as w:
        #     json.dump(od, w, sort_keys=False, indent=4)

    else:
        pass

    # time control
    t1 = time.time()
    print("This execution took " + str(t1-t0) + " seconds")
