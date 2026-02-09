x_linear = np.arange(1, 11)
y_linear = x_linear * 5

y_random = np.random.randint(10, 60, 10)

print("Linear Correlation:", np.corrcoef(x_linear, y_linear)[0][1])
print("Random Correlation:", np.corrcoef(x_linear, y_random)[0][1])

plt.scatter(x_linear, y_linear)
plt.title("Linear Relationship")
plt.show()

plt.scatter(x_linear, y_random)
plt.title("Random Relationship")
plt.show()
