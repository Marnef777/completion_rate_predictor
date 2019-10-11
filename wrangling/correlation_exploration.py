import os
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


if __name__ == '__main__':
    # time control
    t0 = time.time()

    # Directory Handling
    project_path = os.path.dirname(os.path.abspath(__file__))
    file_path = "/dataset.csv"
    path = project_path + file_path

    # Load to df 100 first rows
    df = pd.read_csv(path, nrows=100)

    df = df.drop(['conversion_rate'], axis=1)

    df_corr_spearman = df.corr(method='spearman')
    df_corr_spearman = df_corr_spearman.abs()
    print("SPEARMAN: \n")
    print(df_corr_spearman)

    sb.heatmap(df_corr_spearman,
               xticklabels=df_corr_spearman.columns,
               yticklabels=df_corr_spearman.columns,
               cmap='RdBu_r',
               annot=True,
               linewidth=0.5)
    plt.show()
    # df_corr_pearson = df.corr(method='pearson')
    # df_corr_pearson = df_corr_pearson.abs()
    # print("PEARSON: \n")
    # print(df_corr_pearson)
    # print(type(df_corr_pearson))
    #
    # count_1 = 0
    # for index, row in df_corr_pearson.iterrows():
    #     if (row[index] > 0.1):
    #         count_1 += 1
    #     else:
    #         pass
    # print("count pearson >0.2 = " + str(count_1))

    # time control
    t1 = time.time()
    print("This execution took " + str(t1-t0) + " seconds")
