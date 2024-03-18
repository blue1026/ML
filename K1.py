import pandas
import matplotlib.pyplot as plt
import seaborn

df = pandas.read_csv("C:\\Users\\bluew\\OneDrive\\桌面\\HW\\dye.csv")
fig, axes = plt.subplots(2, 2)

# barplot for nclass
nclass = df["class"].value_counts().sort_index()
seaborn.barplot(x=nclass.index, y=nclass.values, ax=axes[0, 0])
axes[0, 0].set_title("barplot for nclass")
axes[0, 0].set_xlabel(None)

# boxplot for c1, c2 and c3
seaborn.boxplot(df[["c1", "c2", "c3"]], ax=axes[0, 1], orient="v")
axes[0, 1].set_title("boxplot for c1, c2 and c3")

# Histogram of dye$c1
seaborn.histplot(df["c1"], ax=axes[1, 0], binwidth=0.2)
axes[1, 0].set_title("Histogram of dye$c1")
axes[1, 0].set_xlabel("dye$c1")
axes[1, 0].set_ylabel("Frequency")

# boxplot c3 for each class
seaborn.boxplot(df, x="class", y="c3", ax=axes[1, 1])
axes[1, 1].set_title("boxplot c3 for each class")
axes[1, 1].set_xlabel(None)
axes[1, 1].set_ylabel(None)

plt.show()