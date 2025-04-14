import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

# Simulated performance comparison between FireDucks and Pandas
data_sizes = ['100K', '500K', '1M', '5M', '10M']
pandas_times = [0.4, 1.8, 3.2, 16.5, 34.0]     # in seconds (simulated)
fireducks_times = [0.15, 0.6, 1.0, 4.2, 7.9]   # in seconds (simulated)

# Bar chart
x = np.arange(len(data_sizes))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, pandas_times, width, label='Pandas', color='steelblue')
bars2 = ax.bar(x + width/2, fireducks_times, width, label='FireDucks', color='orange')

# Labels and titles
ax.set_xlabel('Dataset Size')
ax.set_ylabel('Processing Time (s)')
ax.set_title('Performance Comparison: FireDucks vs Pandas')
ax.set_xticks(x)
ax.set_xticklabels(data_sizes)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()
