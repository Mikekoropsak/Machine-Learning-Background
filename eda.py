import pandas as pd 
import numpy as np
import matplotlib.pylot as plt
import seaborn as sns

### Check for empty rows ###
if len(df.isna().any()[df.isna().any()]) == 0:
    print('There are no empty columns')
else: 
    print(f'Columns with na: {df.columns[df.isna().any()].to_list()}')

### Creat histogram and box plots for numerical columns ###
def create_plots_num(df):

    num_cols = df.select_dtypes(include=np.number).columns
    plt.figure(figsize=(10,6))
    for i, col in enumerate(num_cols, 1):
        plt.subplot(4, 4, i)
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.show()
    
    num_cols = df.select_dtypes(include=np.number).columns
    plt.figure(figsize=(10,6))
    for i, col in enumerate(num_cols, 1):
        plt.subplot(4, 4, i)
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.show()

create_plots_num(df)

### Create countplots for categorical columns ###
def create_plots_cat(df):
    num_cols = df.select_dtypes(include=object).columns
    plt.figure(figsize=(10,8))
    for i, col in enumerate(num_cols, 1):
        plt.subplot(4, 4, i)
        sns.countplot(x=df[col])
        plt.title(f"Distribution of {col}")
        plt.tick_params(axis='x', labelrotation=90)
    plt.tight_layout()
    plt.show()

create_plots_cat(df)
