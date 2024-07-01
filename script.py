import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('Lok_Sabha_Election_Results_2024.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# Data information
print("\nData information:")
print(df.info())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Count of seats/votes by region/constituency
print("\nCount of seats/votes by region/constituency:")
region_counts = df['Region/Constituency'].value_counts()
print(region_counts)

# Plotting the count of seats by party
plt.figure(figsize=(14, 8))
sns.countplot(data=df, y='Party/Candidate', order=df['Party/Candidate'].value_counts().index, palette='coolwarm')
plt.title('Count of Seats by Party/Candidate')
plt.xlabel('Count')
plt.ylabel('Party/Candidate')
plt.show()

# Plotting the total votes by constituency
constituency_votes = df.groupby('Region/Constituency')['Seats/Votes'].sum().reset_index()
plt.figure(figsize=(14, 8))
sns.barplot(data=constituency_votes, x='Seats/Votes', y='Region/Constituency', palette='viridis')
plt.title('Total Votes by Constituency')
plt.xlabel('Total Votes')
plt.ylabel('Constituency')
plt.show()

# Distribution of votes
plt.figure(figsize=(12, 6))
sns.histplot(df['Seats/Votes'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Votes')
plt.xlabel('Votes')
plt.ylabel('Frequency')
plt.show()

# Boxplot of votes by party/candidate
plt.figure(figsize=(14, 8))
sns.boxplot(data=df, x='Seats/Votes', y='Party/Candidate', palette='Set3')
plt.title('Boxplot of Votes by Party/Candidate')
plt.xlabel('Votes')
plt.ylabel('Party/Candidate')
plt.show()

# Top 5 regions/constituencies by votes
top_regions = constituency_votes.sort_values(by='Seats/Votes', ascending=False).head(5)
plt.figure(figsize=(14, 8))
sns.barplot(data=top_regions, x='Seats/Votes', y='Region/Constituency', palette='Blues_r')
plt.title('Top 5 Regions/Constituencies by Votes')
plt.xlabel('Total Votes')
plt.ylabel('Region/Constituency')
plt.show()
print("\nTop 5 regions/constituencies by votes:")
print(top_regions)

# Bottom 5 regions/constituencies by votes
bottom_regions = constituency_votes.sort_values(by='Seats/Votes').head(5)
plt.figure(figsize=(14, 8))
sns.barplot(data=bottom_regions, x='Seats/Votes', y='Region/Constituency', palette='Reds_r')
plt.title('Bottom 5 Regions/Constituencies by Votes')
plt.xlabel('Total Votes')
plt.ylabel('Region/Constituency')
plt.show()
print("\nBottom 5 regions/constituencies by votes:")
print(bottom_regions)

# Party-wise total votes
party_votes = df.groupby('Party/Candidate')['Seats/Votes'].sum().reset_index().sort_values(by='Seats/Votes', ascending=False)
plt.figure(figsize=(14, 8))
sns.barplot(data=party_votes, x='Seats/Votes', y='Party/Candidate', palette='Spectral')
plt.title('Total Votes by Party/Candidate')
plt.xlabel('Total Votes')
plt.ylabel('Party/Candidate')
plt.show()
