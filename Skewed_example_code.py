import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
data1 = np.random.normal(1, 1, 1000)
data2 = np.random.gamma(1.5,0.8, 1000)
data3 = np.random.beta(10, 1.7, 1000)

# Plot the data and add summary statistics
fig, axs = plt.subplots(3, 3, figsize=(13, 12))

# Histogram 1
axs[0, 0].hist(data1, bins=30, density=True, 
         stacked=True, 
         edgecolor="#6A9662",
         color="#DDFFDD")
axs[0, 0].set_title('Symmetrically Distributed Histogram')
axs[0, 0].axvline(np.mean(data1), color='red', linestyle='dashed', linewidth=2, label='Mean')
axs[0, 0].axvline(np.median(data1), color='black', linestyle='dashed', linewidth=2, label='Median')
axs[0, 0].legend()
axs[0, 0].set_xlim(-2, 5)
# Boxplot
axs[0, 1].boxplot(data1, vert=False, showmeans=True, meanline=True, notch=True)
axs[0, 1].set_title('Boxplot: Q3-Q2 = Q2-Q1')
axs[0, 1].set_yticklabels([])
axs[0, 1].set_xlim(-2, 4.5)
axs[0, 1].grid(True, linewidth=0.4)
# Q-Q plot
stats.probplot(data1, dist="norm", plot=axs[0, 2])
axs[0, 2].set_title('Q-Q plot: Normally Distributed Data')


# Histogram 2
axs[1, 0].hist(data2, bins=30, density=True, 
         stacked=True, 
         edgecolor="#6A9662",
         color="#DDFFDD")
axs[1, 0].set_title('Positively Skewed Histogram')
axs[1, 0].axvline(np.mean(data2), color='red', linestyle='dashed', linewidth=2, label='Mean')
axs[1, 0].axvline(np.median(data2), color='black', linestyle='dashed', linewidth=2, label='Median')
axs[1, 0].legend()
axs[1, 0].set_xlim(0, 5)
# Q-Q plot
stats.probplot(data2, dist="norm", plot=axs[1, 2])
axs[1, 2].set_title('Right-Skewed Data')
# Boxplot
axs[1, 1].boxplot(data2, vert=False, showmeans=True, meanline=True, notch=True)
axs[1, 1].set_title('Boxplot: Q3-Q2 > Q2-Q1')
axs[1, 1].set_yticklabels([])
axs[1, 1].set_xlim(-0.1, 5)
axs[1, 1].grid(True, linewidth=0.4)

# Histogram 3
axs[2, 0].hist(data3, bins=30, density=True, 
         stacked=True, 
         edgecolor="#6A9662",
         color="#DDFFDD")
axs[2, 0].set_title('Negatively Skewed Histogram')
axs[2, 0].axvline(np.mean(data3), color='red', linestyle='dashed', linewidth=2, label='Mean')
axs[2, 0].axvline(np.median(data3), color='black', linestyle='dashed', linewidth=2, label='Median')
axs[2, 0].legend()
axs[2, 0].set_xlim(0.5, 1)
# Boxplot
axs[2, 1].boxplot(data3, vert=False, showmeans=True, meanline=True, notch=True)
axs[2, 1].set_title('Boxplot: Q2-Q1 > Q3-Q2 ')
axs[2, 1].set_yticklabels([])
axs[2, 1].set_xlim(0.5, 1.011)
axs[2, 1].grid(True, linewidth=0.4)
# Q-Q plot
# Q-Q plot
stats.probplot(data3, dist="norm", plot=axs[2, 2])
axs[2, 2].set_title('Left-Skewed Data')
fig.subplots_adjust(hspace=0.3)
plt.savefig('manuscript.png', dpi=200)
plt.show()