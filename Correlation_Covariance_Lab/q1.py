import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataset for 10 students
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
marks = np.array([35, 40, 50, 55, 60, 65, 70, 78, 85, 90])

df_study = pd.DataFrame({
    "Hours_Studied": hours,
    "Marks": marks
})

# Covariance
covariance = df_study["Hours_Studied"].cov(df_study["Marks"])
print("Covariance (Hours vs Marks):", covariance)

# Scatter plot
plt.scatter(hours, marks)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied vs Marks")
plt.show()
