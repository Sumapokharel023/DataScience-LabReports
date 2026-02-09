print("Duplicate Rows:")
print(df.duplicated())

df = df.drop_duplicates()

print("Duplicates After Removal:", df.duplicated().sum())
