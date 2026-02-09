import pandas as pd

data = {
    "Name": ["Asha", "Ramesh", "Sita", "Hari", "Gita", "Manish"],
    "Age": [20, 21, 19, 22, 20, 23],
    "Marks": [65, 72, 58, 80, 90, 67]
}

df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("Dataset Shape:", df.shape)
