import matplotlib.pyplot as plt

# Example data
ages = [22, 25, 30, 25, 26, 32, 35, 40, 23, 21, 30, 31, 33, 36, 38, 25, 29, 28, 27]

# Create histogram
plt.hist(ages, bins=5, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')

# Show the chart
plt.grid(True)
plt.show()
