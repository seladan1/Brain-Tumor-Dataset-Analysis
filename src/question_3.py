import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr


def gender_survival_time (df):

    df["Gender_num"] = df["Gender"].map({"Male": 1, "Female": 0})

    # Spearman correlation
    corr, p_value = spearmanr(df["Gender_num"], df["Survival Time (months)"])

    print("Spearman correlation:", round(corr, 3))
    print("p-value:", round(p_value, 4))
    
    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="Gender",
        y="Survival Time (months)",
        hue="Gender",
        palette="Set2",
        legend=False
    )

    plt.title("Distribution of Survival Time by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Survival Time (months)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.show()

