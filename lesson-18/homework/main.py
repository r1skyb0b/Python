import pandas as pd

# ============================================================================
# HOMEWORK 2: StackOverflow Q&A Dataset
# ============================================================================


df = pd.read_csv('task/stackoverflow_qa.csv')

# 1. Find all questions that were created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'])
q1 = df[df['creationdate'] < '2014-01-01']
print("1. Questions created before 2014:")
print(q1.shape)
print()

# 2. Find all questions with a score more than 50
q2 = df[df['score'] > 50]
print("2. Questions with score > 50:")
print(q2.shape)
print()

# 3. Find all questions with a score between 50 and 100
q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print("3. Questions with score between 50 and 100:")
print(q3.shape)
print()

# 4. Find all questions answered by Scott Boston
q4 = df[df['ans_name'] == 'Scott Boston']
print("4. Questions answered by Scott Boston:")
print(q4.shape)
print()

# 5. Find all questions answered by the following 5 users
users = ['Scott Boston', 'Unutbu', 'Mike Pennington', 'doug', 'Demitri']
q5 = df[df['ans_name'].isin(users)]
print("5. Questions answered by the 5 specified users:")
print(q5.shape)
print()

# 6. Find all questions that were created between March, 2014 and October 2014
#    that were answered by Unutbu and have score less than 5
q6 = df[(df['creationdate'] >= '2014-03-01') & 
        (df['creationdate'] < '2014-11-01') & 
        (df['ans_name'] == 'Unutbu') & 
        (df['score'] < 5)]
print("6. Questions created Mar-Oct 2014, answered by Unutbu, score < 5:")
print(q6.shape)
print()

# 7. Find all questions that have score between 5 and 10 OR have a view count > 10,000
q7 = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]
print("7. Questions with score 5-10 OR viewcount > 10,000:")
print(q7.shape)
print()

# 8. Find all questions that are not answered by Scott Boston
# This includes questions with no answer (NaN) and questions answered by others
q8 = df[df['ans_name'] != 'Scott Boston']
print("8. Questions NOT answered by Scott Boston:")
print(q8.shape)
print()


# ============================================================================
# HOMEWORK 3: Titanic Dataset
# ============================================================================

titanic_df = pd.read_csv("task/titanic.csv")

# 1. Select Female Passengers in Class 1 with Ages between 20 and 30
t1 = titanic_df[(titanic_df['Sex'] == 'female') & 
                (titanic_df['Pclass'] == 1) & 
                (titanic_df['Age'] >= 20) & 
                (titanic_df['Age'] <= 30)]
print("\n1. Female passengers in Class 1, ages 20-30:")
print(t1.shape)
print()

# 2. Filter Passengers Who Paid More than $100
t2 = titanic_df[titanic_df['Fare'] > 100]
print("2. Passengers who paid > $100:")
print(t2.shape)
print()

# 3. Select Passengers Who Survived and Were Alone
t3 = titanic_df[(titanic_df['Survived'] == 1) & 
                (titanic_df['SibSp'] == 0) & 
                (titanic_df['Parch'] == 0)]
print("3. Passengers who survived and were alone:")
print(t3.shape)
print()

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50
t4 = titanic_df[(titanic_df['Embarked'] == 'C') & 
                (titanic_df['Fare'] > 50)]
print("4. Passengers embarked from 'C' and paid > $50:")
print(t4.shape)
print()

# 5. Select Passengers with Siblings or Spouses AND Parents or Children
t5 = titanic_df[(titanic_df['SibSp'] > 0) & 
                (titanic_df['Parch'] > 0)]
print("5. Passengers with siblings/spouses AND parents/children:")
print(t5.shape)
print()

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive
t6 = titanic_df[(titanic_df['Age'] <= 15) & 
                (titanic_df['Survived'] == 0)]
print("6. Passengers aged ≤15 who didn't survive:")
print(t6.shape)
print()

# 7. Select Passengers with Cabins and Fare Greater Than $200
t7 = titanic_df[(titanic_df['Cabin'].notna()) & 
                (titanic_df['Fare'] > 200)]
print("7. Passengers with known cabin and fare > $200:")
print(t7.shape)
print()

# 8. Filter Passengers with Odd-Numbered Passenger IDs
t8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print("8. Passengers with odd PassengerId:")
print(t8.shape)
print()

# 9. Select Passengers with Unique Ticket Numbers
t9 = titanic_df[~titanic_df['Ticket'].duplicated(keep=False)]
print("9. Passengers with unique ticket numbers:")
print(t9.shape)
print()

# 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1
t10 = titanic_df[(titanic_df['Name'].str.contains('Miss', case=False)) & 
                 (titanic_df['Pclass'] == 1)]
print("10. Passengers with 'Miss' in name and in Class 1:")
print(t10.shape)
print()
