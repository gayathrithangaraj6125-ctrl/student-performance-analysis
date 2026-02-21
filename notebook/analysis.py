import pandas as pd

data = pd.read_csv("data/student.csv")
print(data.head())
print(data.info())
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.figure(figsize=(8,5))
sns.histplot(data["math score"], bins=20)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.show()
numeric_data = data.select_dtypes(include=['int64'])
correlation = numeric_data.corr()
plt.figure(figsize=(8,6))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Student Scores")
plt.show()