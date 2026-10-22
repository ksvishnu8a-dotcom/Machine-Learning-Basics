
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

screen_time = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]
battery_used = [3, 6, 9, 13, 16, 20, 23, 27, 30, 34]

# Input feature and target
X = [[value] for value in screen_time]
y = battery_used

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on test data
predictions = model.predict(X_test)

print("Predicted battery use:", predictions.round(2))
print("Actual battery use:", y_test)
print(f"Mean squared error: {mean_squared_error(y_test, predictions):.2f}")

# Plot real data
plt.scatter(screen_time, y, label="Real data")

# Plot the regression line
plt.plot(
    screen_time,
    model.predict(X),
    color="tomato",
    label="Model prediction"
)

plt.xlabel("Screen time (minutes)")
plt.ylabel("Battery used (%)")
plt.title("Screen Time vs. Battery Use")
plt.legend()
plt.show()
