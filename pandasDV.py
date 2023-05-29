import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Select the 'Survived' and 'Sex' columns
data = df[['Survived', 'Sex']]

# Group the data by 'Sex' and calculate the survival rate
survival_rate = data.groupby('Sex').mean()

# Plot the survival rate
plt.bar(survival_rate.index, survival_rate['Survived'])
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.title('Survival Rate by Gender')
plt.show()
