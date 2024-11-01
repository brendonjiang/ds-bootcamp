import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

df['Date'] = pd.to_datetime(df['Date'])

# Task 1
df['Weekday'] = df['Date'].dt.day_name()
weekdays_df = df[df['Weekday'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]

plt.figure(figsize=(10, 6))
weekdays_df.groupby('Weekday')['Pedestrians'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']).plot(kind='line', marker='o')
plt.title("Pedestrian Counts by Weekday")
plt.xlabel("Day of the Week")
plt.ylabel("Pedestrian Counts")
plt.show()

# Task 2
brooklyn_2019 = df[(df['Bridge'] == 'Brooklyn Bridge') & (df['Date'].dt.year == 2019)]
weather_encoded = pd.get_dummies(brooklyn_2019['Weather Summary'])
weather_pedestrian_df = pd.concat([brooklyn_2019['Pedestrians'], weather_encoded], axis=1)
correlation_matrix = weather_pedestrian_df.corr()

plt.figure(figsize=(12, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.title("Correlation Matrix between Weather Conditions and Pedestrian Counts")
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.show()

# Task 3
df['Hour'] = df['Date'].dt.hour

def categorize_time(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

df['Time of Day'] = df['Hour'].apply(categorize_time)

plt.figure(figsize=(10, 6))
df.groupby('Time of Day')['Pedestrians'].sum().reindex(['Morning', 'Afternoon', 'Evening', 'Night']).plot(kind='bar')
plt.title("Pedestrian Activity by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Total Pedestrian Counts")
plt.show()
