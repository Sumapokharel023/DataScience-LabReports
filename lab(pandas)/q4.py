print("Missing Values:")
print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nAfter Filling Missing Values:")
print(df.isnull().sum())
