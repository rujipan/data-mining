import pandas as pd

# Load the dataset
df = pd.read_csv('world_tourism_economy_data.csv')

# View the original structure
print("Original Data Info:")
print(df.info())
print("\nSample Data:")
print(df.head())

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w_]', '', regex=True)

# Handle missing values
# Drop rows missing the 'country' or 'year'
df = df.dropna(subset=['country', 'year'])

# Fill numeric NaNs with 0
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(0)

# Convert 'year' to integer if needed
df['year'] = pd.to_numeric(df['year'], errors='coerce').astype('Int64')

# Drop duplicates
df = df.drop_duplicates()

# Sort by country and year
df = df.sort_values(by=['country', 'year'])

# Output cleaned structure
print("\nCleaned Data Info:")
print(df.info())
print("\nCleaned Sample:")
print(df.head())

# Optional: Save to cleaned CSV
df.to_csv('cleaned_world_tourism_economy_data.csv', index=False)
