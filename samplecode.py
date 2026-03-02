## sample code, requires numpy as np, matplotlib.pyplot as plt and pandas as pd

# correlation between two columns

import pandas as pd
df = pd.read_csv()
correlation = df[].corr(df[])
print(correlation)

# correlation matrix

plt.imshow(corr)
plt.colorbar()

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(j, i, round(corr.iloc[i, j], 2),
                 ha="center", va="center")

plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Heatmap")
plt.show()

# scatter plot

plt.scatter(df[], df[], color='blue')

slope, intercept = np.polyfit(df[], df[], 1)
plt.plot(df[], slope * df[] + intercept, color='red')

plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Scatter Plot with Trend Line")

plt.show()
