import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Sklearn imports for the model building and evaluation (trying to incorporate Data Science)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans  
gym_data = pd.read_csv('./data/gym_members_exercise_tracking.csv')

# rename the column 'Weight (kg)' to 'Weight_kg' for better access
gym_data.rename(columns={'Weight (kg)': 'Weight_kg'}, inplace=True)

# Display the first few rows of the data set and get the general info for the data set
print(gym_data.head())
print(gym_data.info())
print(gym_data.describe())
print(gym_data.columns)
print(gym_data.shape)
print("-" * 100)

# Check for missing values in the data set, there are no missing values in the data set
print(gym_data.isnull().sum())
print("-" * 100)

# What is the average age of the gym goers in the data set?
gym_goers_avg_age = gym_data['Age'].mean()
print(f"The average age of the gym goers in the data set is: {gym_goers_avg_age:.2f}")
print("-" * 100)

# What is percentage of Male vs Female gym goers in the data set?
male_vs_female_gym_goers = gym_data['Gender'].value_counts(normalize=True) * 100
male_vs_female_gym_goers = male_vs_female_gym_goers.astype(float).round(2).astype(str) + '%'
print(f"Percentage of Male vs Female gym goers:\n{male_vs_female_gym_goers}")
print("-" * 100)

# What is the most popular workout type in the data set?
most_popular_workout_type = gym_data["Workout_Type"].value_counts().idxmax()
print(f"The most popular workout type in the data set is: {most_popular_workout_type}")
print("-" * 100)

# Which workout type burns the most calories per hour?
burns_most_calories = gym_data.groupby('Workout_Type')['Calories_Burned'].mean().idxmax()
print(f"The workout type that burns the most calories: {burns_most_calories}")

# Plot the workout type and the most calories burned per workout?
plt.figure(figsize=(12, 8))
sns.barplot(x='Workout_Type', y='Calories_Burned', data=gym_data, estimator=lambda x: sum(x) / len(x))
plt.title('Calories Burned per Workout Type')
plt.xlabel('Workout Type')
plt.ylabel('Average Calories Burned per Hour')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("-" * 100)

# Do women prefer Yoga to other workout types?
yoga_vs_other_workouts = gym_data[gym_data['Gender'] == 'Female']['Workout_Type'].value_counts(normalize=True) * 100
yoga_vs_other_workouts = yoga_vs_other_workouts.round(2).astype(str) + '%'
print(f"Percentage of Female gym goers preferring Yoga vs other workout types:\n{yoga_vs_other_workouts}")
print("-" * 100)
#! The answer to the above question is no.
print(f"Women in general prefer -> {yoga_vs_other_workouts.idxmax()} to other workout types")
print("-" * 100)

# Which workout type has the highest average BPM (Beats per Minute)?
highest_avg_bpm = gym_data.groupby('Workout_Type')['Avg_BPM'].mean().idxmax()
print(f"The workout type with the highest average BPM is: {highest_avg_bpm}")
print("-" * 100)

# Plot the average weight to the workout type and Male vs Female!
plt.figure(figsize=(12, 8))
sns.barplot(x='Workout_Type', y='Weight_kg', hue='Gender', data=gym_data)
plt.title('Average Weight per Workout')
plt.xlabel('Workout Type')
plt.ylabel('Average Weight in Kilograms')
plt.xticks(rotation=45)
plt.show()

# Only select the numeric columns from the data set
numeric_columns = gym_data.select_dtypes(include=['float64', 'int64'])

# Correlation matrix
correlation_matrix = numeric_columns.corr()

print("Correlation Matrix (Top 5 rows):")
print(correlation_matrix.head())
print("-" * 100)
plt.figure(figsize=(14, 10))  
sns.set(style="whitegrid")  

heatmap = sns.heatmap(
    correlation_matrix,
    annot=True,             
    fmt=".2f",              
    cmap="coolwarm",        
    linewidths=0.5,         
    cbar_kws={"shrink": 0.8, "aspect": 30},  
    square=True,            
    mask=None               
)

plt.title("Correlation Matrix Heatmap", fontsize=18, pad=20)
plt.xticks(fontsize=12, rotation=45, ha="right")
plt.yticks(fontsize=12, rotation=0)
plt.tight_layout()  
plt.show()

#! Calorie burn prediction model
features = ['Age', 'Gender', 'Weight_kg', 'Height (m)', 'Workout_Type', 'Session_Duration (hours)']
target = 'Calories_Burned'

X = gym_data[features]
y = gym_data[target]

X = X.fillna(method='ffill')  
y = y.fillna(y.mean())        

# Train test split 80/20 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Age', 'Weight_kg', 'Height (m)', 'Session_Duration (hours)']),
        ('cat', OneHotEncoder(), ['Gender', 'Workout_Type'])
    ]
)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train the model that is given
pipeline.fit(X_train, y_train)

# Evaluate the model
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

"""
Print the metrics and Mean Squared Error and R-squared Score for the model. 
The closer the R-squared score is to 1, the better the model is at predicting the target variable.
The closer the Mean Squared Error is to 0, the better the model is at predicting the target variable.

Source: sklearn Documentation (https://scikit-learn.org/stable/modules/model_evaluation.html#mean-squared-error)

"""

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Predict the calories burned for age 25 person given the following data
new_data = pd.DataFrame({
    'Age': [25],
    'Gender': ['Male'],
    'Weight_kg': [70],
    'Height (m)': [1.75],
    'Workout_Type': ['Cardio'],
    'Session_Duration (hours)': [1.5]
})

predicted_calories = pipeline.predict(new_data)
print(f"Predicted Calories Burned: {predicted_calories[0]:.2f}")
print("-" * 100)

# plot the above data for the model
plt.figure(figsize=(12, 8))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6, label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label='Perfect Prediction Line')
plt.xlabel('Actual Calories Burned', fontsize=14)
plt.ylabel('Predicted Calories Burned', fontsize=14)
plt.title('Actual vs Predicted Calories Burned', fontsize=16)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Plotting feature importance for numerical features with try and except.
try:
    feature_importance = pipeline.named_steps['regressor'].coef_
    feature_names = preprocessor.transformers_[0][2] + list(preprocessor.transformers_[1][1].get_feature_names_out())
    importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
    importance_df.sort_values(by='Importance', ascending=False, inplace=True)

    plt.figure(figsize=(12, 8))
    sns.barplot(data=importance_df, x='Importance', y='Feature', palette='viridis')
    plt.title('Feature Importance', fontsize=16)
    plt.xlabel('Importance', fontsize=14)
    plt.ylabel('Feature', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
except AttributeError:
    print("Feature importance not available for the model.")
    
print("-" * 100)

#! Plot distributive analysis for continuous variables
sns.set_theme(style="whitegrid")

# save the continuous variables in a list
continuous_variables = ['Calories_Burned', 'BMI', 'Session_Duration (hours)']

# Plot distributive analysis for continuous variables
for var in continuous_variables:
    plt.figure(figsize=(10, 6))
    sns.histplot(gym_data[var], kde=True, bins=30, color='blue', alpha=0.7)
    plt.title(f'Distribution of {var}', fontsize=16)
    plt.xlabel(var, fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
    
print("-" * 100)

# Process the data for clustering
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Age', 'BMI']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Gender', 'Experience_Level'])
    ],
    remainder='drop'
)

# KMeans clustering model is used to cluster the data.
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('kmeans', KMeans(n_clusters=5, random_state=42))  # Choose 5 clusters
])

# Train the clustering model
pipeline.fit(gym_data.drop('Workout_Type', axis=1))

# Assign clusters to the original data
gym_data['Cluster'] = pipeline.named_steps['kmeans'].labels_

# Find the most common workout type for each cluster
cluster_recommendations = gym_data.groupby('Cluster')['Workout_Type'].agg(lambda x: x.mode()[0])
print("Cluster Workout Recommendations:")
print(cluster_recommendations)

# Function to recommend workout based on user input
def recommend_workout(age, gender, bmi, experience_level):
    new_user = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'BMI': [bmi],
        'Experience_Level': [experience_level]
    })
    cluster = pipeline.predict(new_user)[0]
    recommended_workout = cluster_recommendations[cluster]
    return recommended_workout

# Test the recommendation system
age = 25
gender = 'Male'
bmi = 22.5
experience_level = 'Intermediate'

recommendation = recommend_workout(age, gender, bmi, experience_level)
print(f"Recommended Workout for Age {age}, Gender {gender}, BMI {bmi}, Experience Level {experience_level}: {recommendation}")

# Visualization of Clusters with Recommendations
plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'purple', 'orange']  

for cluster in sorted(gym_data['Cluster'].unique()):
    cluster_data = gym_data[gym_data['Cluster'] == cluster]
    plt.scatter(cluster_data['Age'], cluster_data['BMI'], label=f'Cluster {cluster} ({cluster_recommendations[cluster]})', alpha=0.7)

plt.title('Cluster Analysis for Workout Recommendation')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.legend()
plt.show()

"""
Cluster recommendation refers to a method of recommending items or actions 
to users based on the grouping (or clustering) of similar data points. 

It leverages the results of a clustering algorithm like KMeans to:
- Find patterns in the data
- Assign users to a cluster

Recommendations are then made based on the common characteristics 
or behaviors of that cluster.

Source: 
https://scikit-learn.org/stable/unsupervised_learning.html
"""