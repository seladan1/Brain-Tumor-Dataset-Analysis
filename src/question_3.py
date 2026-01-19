import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr


def calc_spearman_gender_survival (df):
    # Calculates Spearman correlation and p-value between gender and survival time.
    
    df["Gender_num"] = df["Gender"].map({"Male": 1, "Female": 0})
    corr, p_value = spearmanr(df["Gender_num"], df["Survival Time (months)"])
    
    # Final conclusion.
    if abs(corr) < 0.2:
        strength = "very weak"
    elif abs(corr) < 0.4:
        strength = "weak"
    else:
        strength = "moderate to strong"

    significance = "statistically significant" if p_value < 0.05 else "not statistically significant"

    print(
        f"Conclusion: There is a {strength} relationship between gender and survival time, "
        f"and the result is {significance}."
    )
    
    print(f"Spearman correlation: {corr:.4f}")
    print(f"p-value: {p_value:.4f}")
    
    return corr, p_value


def plot_survival_by_gender(df):
    # Creates a box plot of survival time by gender.
    
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
    
    # Fix the window position to avoid visual jumping on screen.
    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+200+100")

    plt.show()

# checking the impact of the outliers that were found in the graph.
def spearman_outlier_impact(df, threshold=72):
    # Encode gender
    df = df.copy()
    df["Gender_num"] = df["Gender"].map({"Male": 1, "Female": 0})

    # Spearman with all data
    corr_all, p_all = spearmanr(
        df["Gender_num"],
        df["Survival Time (months)"]
    )

    # Remove long-survival outliers
    df_no_outliers = df[df["Survival Time (months)"] < threshold]

    corr_no, p_no = spearmanr(
        df_no_outliers["Gender_num"],
        df_no_outliers["Survival Time (months)"]
    )

    print("Effect of long-survival outliers (≥ 72 months):\n")
    print(f"With outliers    → Spearman: {corr_all:.4f}, p-value: {p_all:.4f}")
    print(f"Without outliers → Spearman: {corr_no:.4f}, p-value: {p_no:.4f}")

    return {
        "with_outliers": (corr_all, p_all),
        "without_outliers": (corr_no, p_no),
        "n_outliers": len(df) - len(df_no_outliers)
    }



