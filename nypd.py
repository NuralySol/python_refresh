import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("./data/nypd.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
# Plot as a Bar chart number of INCIDENTs by BORO
incidents_by_boro = df.groupby("BORO")["INCIDENT_KEY"].count()

plt.pie(x = incidents_by_boro.values, labels = incidents_by_boro.index, autopct = "%1.1f%%")
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
	"STATEN ISLAND": 476143
}
# Most dangerous Boro seems to be Bronx and create a series borogh_population 
# Series is a 
murder_incidents_per_capita = df.groupby("BORO")["STATISTICAL_MURDER_FLAG"].count() / pd.Series(borough_population)
plt.bar(x=murder_incidents_per_capita.index, height=murder_incidents_per_capita.values)
plt.xlabel("Borough")
plt.ylabel("Murder Incidents per Capita")
plt.title("Murder Incidents per Capita by Borough")
plt.show()