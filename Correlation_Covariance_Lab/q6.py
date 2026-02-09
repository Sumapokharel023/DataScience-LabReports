height = np.array([150, 155, 160, 165, 170, 175, 180, 185])
weight = np.array([50, 53, 58, 60, 65, 70, 75, 80])

df_hw = pd.DataFrame({
    "Height": height,
    "Weight": weight
})

print("Mean:\n", df_hw.mean())
print("Variance:\n", df_hw.var())
print("Covariance:\n", df_hw.cov())
print("Correlation:\n", df_hw.corr())

sns.jointplot(x="Height", y="Weight", data=df_hw, kind="reg")
plt.show()
