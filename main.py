#MapPlot.py
#Name: Olivia Sulzle
#Date: 4/12/26
#Assignment: Lab 10

import csv
import matplotlib.pyplot as plt

# Step 1: Load the Data
# Using lists
trials = []
reaction_times = []

with open('reaction_time_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        trial = int(row[0])
        time = float(row[1])
        trials.append(trial)
        reaction_times.append(time)

# Alternatively, using Pandas
# df = pd.read_csv('reaction_time_data.csv')

# Step 4: Clean the Data
# Remove or ignore problematic data (e.g., non-positive values)
clean_trials = []
clean_times = []
for t, rt in zip(trials, reaction_times):
    if rt > 0:
        clean_trials.append(t)
        clean_times.append(rt)

# Step 2 & 3: Select Data and Create Visualization
# Plot Trial vs ReactionTime_ms as a line graph
plt.figure(figsize=(10, 6))
plt.plot(clean_trials, clean_times, marker='o', linestyle='-')
plt.title('Reaction Time Over Trials')
plt.xlabel('Trial Number')
plt.ylabel('Reaction Time (ms)')
plt.grid(True)
plt.savefig('reaction_time_graph.png')
plt.show()

# Step 5: Interpret the Results
# The graph shows the reaction time decreasing over trials, indicating improvement or learning effect.
# Trend: Negative linear trend, reaction times get faster.
# Visualization helps see the pattern clearly, showing consistent decrease.
