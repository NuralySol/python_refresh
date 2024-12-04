import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset from Seaborn.
df = sns.load_dataset('titanic')
df.head()
print(df.head())

# What on average is fare difference between first class and third class tickets?
first_class_fare = df[df['class'] == 'First']['fare'].mean()
third_class_fare = df[df['class'] == 'Third']['fare'].mean()
fare_difference = round(first_class_fare - third_class_fare, 2)
print(f"The difference in between first class and third class is: \n ${fare_difference}")

# Plot as a pie people who survived vs who did not.
survivors = df[df['survived'] == 1].shape[0]
non_survivors = df[df['survived'] == 0].shape[0]
survived = [survivors, non_survivors]
labels = ['Survived', 'Did not survive']
plt.pie(survived, labels = labels, autopct='%1.1f%%')
plt.title('Survivors vs Non-Survivors of Titanic')
plt.show()

# Plot the survival rate by genders of the Titanic using countplot.
sns.countplot(x='sex', hue='survived', data=df)
plt.title('Survival Count by Gender')
plt.ylabel('Count')
plt.xlabel('Gender')
plt.legend(title='Survived', loc='upper right', labels=['Did not survive', 'Survived'])
plt.show()

# Survival based on class using countplot.
sns.countplot(x = 'class', hue = 'survived', data = df)
plt.title('Survival Count by Class')
plt.ylabel('Count')
plt.xlabel('Class')
plt.legend(title = 'Survived', loc = 'upper right', labels = ['Did not survive', 'Survived'])
plt.show()

# Survival based on class and gender Male vs Female using countplot.
sns.catplot(x='sex', hue='survived', col='class', data=df, kind='count', palette='Set1', hue_order=[0, 1])
plt.subplots_adjust(top=0.85)
plt.suptitle('Survival Count by Gender and Class')
plt.show()

# Plotting the multiple countplots for various columns. 
column_names = list(df[['sex', 'pclass','adult_male', 'embark_town', 'who', 'deck']].columns)
fig, subplots = plt.subplots(2, 3, figsize=(14, 8))
for row in range (0, 2):
    for col in range (0, 3):
        sns.countplot(x = column_names.pop(0), hue = 'survived', data = df, ax = subplots[row, col])
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.suptitle('Survival Count by Various Columns')
plt.show()

# Plotting the distribution of age of passengers.
sns.histplot(df['age'], bins=30, kde=True)
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.axvline(df['age'].mean(), color='k', linestyle='dashed', linewidth=1)
plt.show()
