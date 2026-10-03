import pandas as pd

df = pd.read_csv(r"E:\6 month roadmap\Day2\students.csv.txt")

print("Number of students:", len(df))

print("Average marks:", df["Marks"].mean())


print("Students with marks greater than 80:")
print(df[df["Marks"] > 80])
print(df)