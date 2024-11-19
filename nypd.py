import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("./data/nypd.csv")
print(df.head())
print("-" * 100)
print(df.info())
print("-" * 100)
print(df.describe())
print("-" * 100)
print(df.columns)
print("-" * 100)
# Plot as a Bar chart number of INCIDENTs by BORO
incidents_by_boro = df.groupby("BORO")["INCIDENT_KEY"].count()

plt.pie(x=incidents_by_boro.values, labels=incidents_by_boro.index, autopct="%1.1f%%")
plt.title("Number of Incidents by Borough")
plt.show()

# Plot as a Bar chart number of INCIDENTs by BORO by STATISTICAL_MURDER_FLAG
murder_incidents = df.groupby("BORO")["STATISTICAL_MURDER_FLAG"].count()
plt.bar(x=murder_incidents.index, height=murder_incidents.values)
plt.xlabel("Borough")
plt.ylabel("Number of Murder Incidents")
plt.title("Number of Murder Incidents by Borough")
plt.show()

# Plot per capita by population for statistical murder flag
# Fixture from googe search for recent population by borough
borough_population = {
    "MANHATTAN": 1628706,
    "BRONX": 1418207,
    "BROOKLYN": 2559903,
    "QUEENS": 2253858,
    "STATEN ISLAND": 476143,
}
# Most dangerous Boro seems to be Bronx and create a series borogh_population
# Series is a
murder_incidents_per_capita = df.groupby("BORO")[
    "STATISTICAL_MURDER_FLAG"
].count() / pd.Series(borough_population)
plt.bar(x=murder_incidents_per_capita.index, height=murder_incidents_per_capita.values)
plt.xlabel("Borough")
plt.ylabel("Murder Incidents per Capita")
plt.title("Murder Incidents per Capita by Borough")
plt.show()

# Plot all incidents near the empire state building and plot it as a star
# Need to get a fixture from a google search and save it as a tuple
empire_state_loc = (40.7484, -73.9857)

# Filter incidents in Manhattan
manhattan_incidents = df[df["BORO"] == "MANHATTAN"]

# Plot the incidents in Manhattan
plt.figure(figsize=(10, 6))
plt.scatter(
    manhattan_incidents["Longitude"],
    manhattan_incidents["Latitude"],
    alpha=0.3,
    label="Incidents",
)
plt.scatter(
    empire_state_loc[1],
    empire_state_loc[0],
    marker="*",
    color="red",
    label="Empire State Building",
)
plt.annotate(
    "Empire State Building",
    xy=(empire_state_loc[1], empire_state_loc[0]),
    xytext=(empire_state_loc[1] + 0.01, empire_state_loc[0] + 0.01),
    arrowprops=dict(facecolor="orange", shrink=0.05),
)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Incidents in Manhattan and Empire State Building Location")
plt.legend()
plt.show()

# Plot incidents by hour as a bar chart and what is the most dangerous hour
# Most dangerour time seems to night time, and around that time
# Need to convert the OCCUR_TIME to usinng to_datetime (format="%H:%M:%S")
df["OCCUR_TIME"] = pd.to_datetime(df["OCCUR_TIME"], format="%H:%M:%S")
df["Hour"] = df["OCCUR_TIME"].dt.hour

incidents_by_hour = df.groupby("Hour")["INCIDENT_KEY"].count()
plt.bar(x=incidents_by_hour.index, height=incidents_by_hour.values)
plt.xlabel("Hour")
plt.ylabel("Number of Incidents")
plt.title("Number of Incidents by Hour")
plt.show()
# Plot a Seaborn heatmap for the correlation matrix

# Select only numeric columns for the correlation matrix
numeric_df = df.select_dtypes(include=["float", "int"])

# Compute the correlation matrix
correlation_matrix = numeric_df.corr()

# Set up the figure and heatmap
plt.figure(figsize=(12, 8))
heatmap = sns.heatmap(
    correlation_matrix,
    annot=True,                # Display correlation values on the heatmap
    fmt=".2f",                 # Format values to 2 decimal places
    cmap="coolwarm",           # Color map for better aesthetics
    linewidths=0.5,            # Add space between cells
    cbar_kws={"shrink": 0.8},  # Adjust the color bar size
    square=True                # Keep cells square for symmetry
)

# Customize the title and axis labels
plt.title("Correlation Matrix", fontsize=16, pad=20, weight="bold")  # Bold title
plt.xticks(
    ticks=range(len(correlation_matrix.columns)),
    labels=[col.replace("_", " ").title() for col in correlation_matrix.columns],
    rotation=45,
    ha="right",
    fontsize=10
)
plt.yticks(
    ticks=range(len(correlation_matrix.index)),
    labels=[col.replace("_", " ").title() for col in correlation_matrix.index],
    rotation=0,
    fontsize=10
)

# Display the heatmap and the correlation matrix
plt.tight_layout()
plt.show()