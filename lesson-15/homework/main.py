import pandas as pd

# 1. Create a DataFrame (like a table) named Roster
# This is our "database" - a DataFrame with Name, Species, and Age columns
roster = pd.DataFrame(columns=['Name', 'Species', 'Age'])

print("✓ Roster DataFrame created")

# 2. Populate the DataFrame with the given values
data = {
    'Name': ['Benjamin Sisko', 'Jadzia Dax', 'Kira Nerys'],
    'Species': ['Human', 'Trill', 'Bajoran'],
    'Age': [40, 300, 29]
}

roster = pd.DataFrame(data)

print("✓ DataFrame populated with initial data")
print("\nInitial Roster:")
print(roster)

# 3. Update the Name of Jadzia Dax to be Ezri Dax
roster.loc[roster['Name'] == 'Jadzia Dax', 'Name'] = 'Ezri Dax'

print("\n✓ Updated Jadzia Dax to Ezri Dax")
print("\nUpdated Roster:")
print(roster)

# 4. Display the Name and Age of everyone classified as Bajoran
print("\n--- Bajoran Crew Members ---")
bajorans = roster[roster['Species'] == 'Bajoran'][['Name', 'Age']]
print(bajorans)

# Optional: Save to CSV file (like saving a database)
roster.to_csv('roster.csv', index=False)
print("\n✓ All exercises completed! Data saved to roster.csv")
