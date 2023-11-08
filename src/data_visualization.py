import pandas as pd
import random
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv('dataset.csv')

# Visualize the data
count_data = df.groupby(['app_name', 'review_score']).size().unstack().fillna(0)

# Step 5: Visualize the data
count_data.plot(kind='barh', stacked=True)
plt.ylabel('App Name')
plt.xlabel('Count of Review Scores')
plt.title('Review Scores by App Name')
plt.legend(title='Review Score', labels=['-1', '1'])

# Show the plot
plt.show()