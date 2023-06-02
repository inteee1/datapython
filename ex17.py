import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
tips = sns.load_dataset("tips")
print(tips)
sns.relplot(data=tips, x="total_bill", y = "tip", col="time", hue="smoker", style="smoker", size="size")
#plt.show()

print(tips.head(10))

