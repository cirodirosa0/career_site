import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io


class Testing:
    def __init__(self):
        self.test_data = pd.read_csv("./static/assets/test.csv")
        self.train_data = pd.read_csv("./static/assets/train.csv")
        self.train_dict = self.train_data.to_dict(orient="index")
        self.test_dict = self.test_data.to_dict(orient="index")

    def otherinfo(self):
        dotenv_path = '/home/cirodirosa0/career_site/.env'
        load_dotenv(dotenv_path)

        secret_key = os.getenv("SECRET_KEY")
        print(secret_key)

    def plot_me(self, threshold, figsize=(5, 3.33)):
        self.train_data['Sex'] = self.train_data['Sex'].replace({'male': 1, 'female': 0})
        self.train_data['Embarked'] = self.train_data['Embarked'].replace({'S': 0, 'C': 1, 'Q': 2})

        combined_data = pd.DataFrame({
            'Combined_Column': self.train_data['Sex'] + self.train_data['Pclass'] + self.train_data['Embarked'],
            'Survived': self.train_data['Survived']
        })

        exclude_columns = ['Name', 'Ticket', 'Cabin', 'Fare', 'Unnamed: 0']
        # Filter out non-numeric columns
        numeric_columns = self.train_data.select_dtypes(include=[np.number]).columns.tolist()
        numeric_columns = [col for col in numeric_columns if col not in exclude_columns]

        correlation_matrix = self.train_data[numeric_columns].corr()

        # Exclude correlations below the threshold
        correlation_matrix = correlation_matrix[correlation_matrix.abs() >= threshold]

        # Set the size of the Matplotlib figure
        fig, ax = plt.subplots(figsize=figsize)

        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        plt.xticks(rotation=45)
        plt.title('Correlation Heatmap')

        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)

        plt.close()

        return img
