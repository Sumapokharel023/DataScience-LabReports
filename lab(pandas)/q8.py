df["Marks_out_of_10"] = df["Marks"] / 10

df.rename(columns={
    "Name": "Student_Name",
    "Age": "Student_Age"
}, inplace=True)

df.to_csv("cleaned_students.csv", index=False)

print("Cleaned dataset saved successfully")
