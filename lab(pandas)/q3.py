selected_df = df[df["Marks"] > 60][["Name", "Marks"]]

print("Students with Marks > 60:")
print(selected_df)
