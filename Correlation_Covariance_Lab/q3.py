temperature = np.array([20, 22, 25, 27, 30, 32, 35, 37, 38, 40])
sales = np.array([100, 120, 150, 165, 200, 210, 240, 260, 270, 300])

df_sales = pd.DataFrame({
    "Temperature": temperature,
    "IceCream_Sales": sales
})

cov_temp_sales = df_sales["Temperature"].cov(df_sales["IceCream_Sales"])
print("Covariance (Temperature vs Sales):", cov_temp_sales)

plt.scatter(temperature, sales)
plt.xlabel("Temperature")
plt.ylabel("Ice-Cream Sales")
plt.title("Temperature vs Ice-Cream Sales")
plt.show()
