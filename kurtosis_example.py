import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta
import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.rcParams['figure.figsize'] = [9, 4]
fig, ax1 = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
# Generate beta pdfs
x = np.linspace(0, 1, 100000)
y1 = beta.pdf(x, 1,1)
y2 = beta.pdf(x, 3,3)
y3 = beta.pdf(x, 15, 15)
'''
# Calculate and display kurtosis value for first subplot
kurtosis1 = stats.beta.stats( 0.85, 0.85, moments='k')
ax1[0].text(0.05, 0.9, f"Kurtosis: {kurtosis1:.2f}", transform=ax1[0].transAxes)
'''
# First subplot
ax1[0].plot(x, y1, linewidth=1, color='firebrick')
ax1[0].set_title("Beta(2,2)")
ax1[0].set_xlabel("X")
ax1[0].set_ylabel("Probability Density")

'''
# Calculate and display kurtosis value for second subplot
kurtosis2 = stats.beta.stats(2, 2, moments='k')
ax1[1].text(0.05, 0.9, f"Kurtosis: {kurtosis2:.2f}", transform=ax1[1].transAxes)
'''
# Second subplot
ax1[1].plot(x, y2, linewidth=1, color='burlywood')
ax1[1].set_title("Beta(5,5)")
ax1[1].set_xlabel("X")
ax1[1].set_ylabel("Probability Density")
'''
# Calculate and display kurtosis value for third subplot
kurtosis3 = stats.beta.stats( 15, 15, moments='k')
ax1[2].text(0.05, 0.9, f"Kurtosis: {kurtosis3:.2f}", transform=ax1[2].transAxes)
'''
# Third subplot
ax1[2].plot(x, y3, linewidth=1, color='dodgerblue')
ax1[2].set_title("Beta(8,8)")
ax1[2].set_xlabel("X")
ax1[2].set_ylabel("Probability Density")

# Plot histograms for each beta distribution
ax1[0].hist(beta.rvs(1,1, size=1000), bins=30, density=True, color='firebrick',alpha=0.5, edgecolor='black')
ax1[0].set_title('Platykurtic', fontsize=16)
ax1[1].hist(beta.rvs(3,3, size=1000), bins=30, density=True, color='burlywood',alpha=0.5, edgecolor='black')
ax1[1].set_title('Mesokurtic', fontsize=16)
ax1[2].hist(beta.rvs(15, 15, size=1000), bins=30, density=True, color='dodgerblue',alpha=0.5, edgecolor='black')
ax1[2].set_title('Leptokurtic', fontsize=16)

'''
q1, q3 = np.percentile(y1, [25, 75])
iqr = q3 - q1
ax1[0].annotate(f"IQR = {iqr:.2f}", xy=(0.05, 0.9), xycoords='axes fraction', fontsize=12)

q1, q3 = np.percentile(y2, [25, 75])
iqr = q3 - q1
ax1[1].annotate(f"IQR = {iqr:.2f}", xy=(0.05, 0.9), xycoords='axes fraction', fontsize=12)

q1, q3 = np.percentile(y3, [25, 75])
iqr = q3 - q1
ax1[2].annotate(f"IQR = {iqr:.2f}", xy=(0.05, 0.9), xycoords='axes fraction', fontsize=12)
'''
plt.tight_layout()
plt.savefig('kurtosis_example.png', dpi=300)
plt.show()