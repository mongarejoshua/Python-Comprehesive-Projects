import pandas as pd
from sklearn.feature_extraction import TfidfVectorizer


data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Paris', 'London']}

df = pd.DataFrame(data)
print(df)

ex = pd.read_excel("C:\Users\mogak\OneDrive\Documents\Friday\ALL GRADES.xls")

print(ex)