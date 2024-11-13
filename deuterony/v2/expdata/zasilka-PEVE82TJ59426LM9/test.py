import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 4, 2, 5, 1])
y_error = np.array([0.5, 0.2, 0.8, 0.4, 0.6])
box_error = np.array([1, 0.5, 2, 1.5, 0.8])

# Plotting
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=y_error, fmt='o', color='black', capsize=3, label='Data')
ax.errorbar(x, y, yerr=box_error, fmt='none', ecolor='red', elinewidth=2, capsize=0, label='Box error')

# Labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Errorbar plot with box error')
ax.legend()

plt.show()
