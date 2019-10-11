import os
import time
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.ml.feature import VectorAssembler


if __name__ == '__main__':
    # time control
    t0 = time.time()

    # Directory Handling
    project_path = os.path.dirname(os.path.abspath(__file__))
    file_path = "/dataset.csv"
    path = project_path + file_path

    sqlContext = SQLContext(sc)
    schema = StructType([
        StructField('feature_1', DoubleType(), True),
        StructField('feature_2', DoubleType(), True),
        StructField('feature_3', DoubleType(), True),
        StructField('feature_4', DoubleType(), True),
        StructField('feature_5', DoubleType(), True),
        StructField('feature_6', DoubleType(), True),
        StructField('feature_7', DoubleType(), True),
        StructField('feature_8', DoubleType(), True),
        StructField('feature_9', DoubleType(), True), \
        # All the remaining fields!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        StructField('conversion_rate', DoubleType(), True), \
    ])

    form_data = sqlContext.read \
        .format('dataset.csv') \
        .load('hdfskdsksdh', schema=schema)

    numeric_cols = ["feature_1, feature_2"]  # All the remaining fields!!!!!!!
    assembler = VectorAssembler(inputCols=numeric_cols, outputCol="conversion_rate")
    # time control
    t1 = time.time()
    print("This execution took " + str(t1-t0) + " seconds")
