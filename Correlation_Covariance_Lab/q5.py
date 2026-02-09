np.random.seed(42)

x = np.random.rand(50)
y = np.random.rand(50)

cov_random = np.cov(x, y)[0][1]
corr_random = np.corrcoef(x, y)[0][1]

print("Covariance (Random Data):", cov_random)
print("Correlation (Random Data):", corr_random)

plt.scatter(x, y)
plt.xlabel("Random X")
plt.ylabel("Random Y")
plt.title("Random Data Scatter Plot")
plt.show()

