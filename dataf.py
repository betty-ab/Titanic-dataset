import pandas as pd
#part1
data = {
    "Name": ["kal", "yabu", "samri", "sifen", "frehiwot", "hiwot", "birhanu", "beza", "eleni", "dagme", "samuel", "surafel", "hana", "haymi", "meski"],
    "Age": [21, 25, 30, 22, 24, 27, 33, 24, 25, 29, 23, 28, 21, 26, 27],
    "Department": ["HR", "IT", "Finance", "Marketing", "IT", "Finance", "HR", "Marketing", "IT", "Finance", "HR", "IT", "Marketing", "Finance", "HR"],
    "salary": [9000, 10500, 8500, 9500, 10500, 9800, 10200, 9400, 9500, 11000, 9300, 10400, 10800, 9700, 9100],
    "Experience_years": [1, 3, 2, 2, 4, 3, 1, 1, 5, 4, 2, 3, 2, 3, 2]
}
custom_index = [f'INV-{i}' for i in range(500, 515)]
df = pd.DataFrame(data, index=custom_index)
print(df)

#part2
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
display(df.head())
df.info()
display(df.describe())

# Step 2: Data Cleaning
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop(columns=['Cabin'], inplace=True)
df = df.drop_duplicates()

print("\n--- STEP 2: CLEANING COMPLETE ---")
print(f"Missing values remaining: {df.isnull().sum().sum()}")

# Step 3: Data Analysis
print("\n--- STEP 3: DATA ANALYSIS ---")
survival_by_gender = df.groupby('Sex')['Survived'].mean()
survival_by_class = df.groupby('Pclass')['Survived'].mean()

print("Survival Rate by Gender:")
display(survival_by_gender)

print("Survival Rate by Class:")
display(survival_by_class)

# Step 4: Filtering
survived_females = df[(df['Sex'] == 'female') & (df['Survived'] == 1)]
survived_children = df[(df['Age'] < 18) & (df['Survived'] == 1)]

print(f"\nFiltered Count: {len(survived_females)} females survived and {len(survived_children)} children survived.")
