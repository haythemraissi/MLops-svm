import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_boxplots(data, title):
    plt.figure(figsize=(12, 5))
    sns.boxplot(x='variable', y='value', hue='diagnosis', data=pd.melt(data, id_vars='diagnosis'), palette='Set2')
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
