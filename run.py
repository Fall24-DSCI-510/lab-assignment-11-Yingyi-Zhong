# Solution code for the Iris Dataset Homework (run.py)

import pandas as pd
from scipy.stats import zscore

# Question 1: Pre-process the data
def preprocess_data(input_filename):
    df = pd.read_csv(input_filename, names=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Species'])

    df['SepalLengthCm_z'] = zscore(df['SepalLengthCm'])
    df['SepalWidthCm_z'] = zscore(df['SepalWidthCm'])


    preprocessed_data = df[
        (df['SepalLengthCm_z'] >= -2) &
        (df['SepalLengthCm_z'] <= 2) &
        (df['SepalWidthCm_z'] >= -2) &
        (df['SepalWidthCm_z'] <= 2)
    ].copy()
    preprocessed_data['ID'] = range(1, len(preprocessed_data)+1)
    return preprocessed_data
#print(preprocess_data('iris.data'))

# Question 2: Descriptive Statistics Functions
def species_count(data):
    preprocessed_data = preprocess_data(data)
    return preprocessed_data['Species'].value_counts().to_dict()
#print(species_count('iris.data'))

def average_sepal_length(data):
    preprocessed_data = preprocess_data(data)
    return round(preprocessed_data['SepalLengthCm'].mean(),1)
#print(average_sepal_length('iris.data'))

def max_petal_width(data):
    preprocessed_data = preprocess_data(data)
    return round(preprocessed_data['PetalWidthCm'].max(),1)
#print(max_petal_width('iris.data'))

def min_petal_length(data):
    preprocessed_data = preprocess_data(data)
    return round(preprocessed_data['PetalLengthCm'].min(),1)
#print(min_petal_length('iris.data'))

def count_sepal_length_above_5(data):
    preprocessed_data = preprocess_data(data)
    sepal_length_above_5 = len(preprocessed_data[preprocessed_data['SepalLengthCm']>5])
    return sepal_length_above_5
#print(count_sepal_length_above_5('iris.data'))

# Question 3: Analysis Functions
def count_petal_length_below_2(data):
    preprocessed_data = preprocess_data(data)
    petal_length_below_2 = (preprocessed_data['PetalLengthCm']<2).sum()
    return petal_length_below_2
#print(count_petal_length_below_2('iris.data'))

def get_sepal_width_above_3_5(data):
    preprocessed_data = preprocess_data(data)
    sepal_width_above_3_5 = preprocessed_data[preprocessed_data['SepalWidthCm']>3.5]
    id_list = sepal_width_above_3_5 ['ID'].tolist()
    return id_list
#print(get_sepal_width_above_3_5('iris.data'))

def species_count_petal_width_above_1_5(data):
    preprocessed_data = preprocess_data(data)
    petal_width_above_1_5 = preprocessed_data[preprocessed_data['PetalWidthCm']>1.5]
    species_count_dict = petal_width_above_1_5['Species'].value_counts().to_dict()
    return species_count_dict
#print(species_count_petal_width_above_1_5('iris.data'))

def get_virginica_petal_length_above_6(data):
    preprocessed_data = preprocess_data(data)
    virginica_petal_length_above_6 = preprocessed_data[(preprocessed_data['PetalLengthCm']>6)&(preprocessed_data['Species']=='Iris-virginica')]
    virginica_id_list = virginica_petal_length_above_6['ID'].tolist()
    return virginica_id_list
#print(get_virginica_petal_length_above_6('iris.data'))

def get_largest_sepal_width(data):
    preprocessed_data = preprocess_data(data)
    largest_sepal_width = preprocessed_data[preprocessed_data['SepalWidthCm'] == preprocessed_data['SepalWidthCm'].max()]
    return largest_sepal_width['ID'].iloc[0]
#print(get_largest_sepal_width('iris.data'))

