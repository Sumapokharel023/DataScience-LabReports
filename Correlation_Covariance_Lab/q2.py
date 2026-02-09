correlation = df_study["Hours_Studied"].corr(df_study["Marks"])
print("Correlation Coefficient:", correlation)

sns.regplot(x="Hours_Studied", y="Marks", data=df_study)
plt.title("Regression Plot: Hours Studied vs Marks")
plt.show()
