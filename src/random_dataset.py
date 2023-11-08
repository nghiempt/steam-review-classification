import pandas as pd
import random
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv('dataset_big.csv')

# Step 2: Select 10 random app_name values
random_app_names = random.sample(df['app_name'].unique().tolist(), 10)

# Initialize an empty DataFrame to store the selected data
selected_data = pd.DataFrame()

# Step 3: Select up to 10,000 rows with the same app_name for each random app_name
max_rows_per_app = 50000

for app_name in random_app_names:
    app_data = df[df['app_name'] == app_name]
    if len(app_data) < max_rows_per_app:
        app_data = app_data.sample(n=max_rows_per_app, replace=True, random_state=1)  # Sample up to 10,000 rows with replacement
    selected_data = pd.concat([selected_data, app_data])

# Truncate to exactly 10,000 rows if it's larger
selected_data = selected_data.sample(n=50000, random_state=1)

# Step 4: Calculate the count of review_score values (-1 or 1) for each app_name
count_data = selected_data.groupby(['app_name', 'review_score']).size().unstack().fillna(0)

# Step 5: Visualize the data
count_data.plot(kind='bar', stacked=True)
plt.xlabel('App Name')
plt.ylabel('Count of Review Scores')
plt.title('Review Scores by App Name')
plt.legend(title='Review Score', labels=['-1', '1'])

# Step 6: Save the selected data to a new CSV file
selected_data.to_csv('dataset.csv', index=False)

# Show the plot
plt.show()
