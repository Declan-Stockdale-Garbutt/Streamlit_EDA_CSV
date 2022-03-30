import pandas as pd

csv_file = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'
df = pd.read_csv(csv_file, sep=',').select_dtypes(include=['float64'])


print('Return name of selected column')
print(df.columns)

print('Return full list of details')
print(df.describe())

print('Return number of unique values for selected column')
print(df[df.columns].nunique())

print('Return number of missing values for selected column')
print(df.isnull().sum())

print('Return number of occurrence of 0 value for selected column')
print((df== 0).sum())

print('Return number of negative values for selected column')
print((df< 0).sum())

print('Return the average value for selected column')
print(df.mean())

print('Return the standard deviation value for selected column')
print(df.std())

print('Return the minimum value for selected column')
print(df.min())

print('Return the maximum value for selected column')
print(df.max())

print('Return the median value for selected column')
print(df.median())

print('Return the generated histogram for selected column')
print('???')

print("#occurrences and percentage of the top 20 most frequent values")
freq = df['Lat'].value_counts().reset_index()
print(freq.head(20))