df = pd.read_csv("students.csv")

print("Column Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nBasic Statistics:")
print(df.describe())
