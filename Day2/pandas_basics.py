import pandas as pd

marks = pd.Series([85, 75, 90, 65, 88])

print("marks:")
print(marks)
print(marks.mean())
print(marks.max())
print(marks.min())



data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 28],
        "marks": [85, 75, 90, 65, 88]}

df = pd.DataFrame(data)

#print(df)
#print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
#print(df.describe())


print(df[df["marks"] > 80])