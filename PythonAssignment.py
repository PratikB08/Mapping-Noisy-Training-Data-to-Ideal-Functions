import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import os
from sklearn.metrics import mean_squared_error
from math import sqrt
import uuid

train_df = pd.read_csv("train.csv")
ideal_df = pd.read_csv("ideal.csv")
test_df = pd.read_csv("test.csv")

best_matches = {}
max_deviations = {}

for train_col in train_df.columns[1:]:
    min_error = float('inf')
    best_func = None
    max_dev = 0
    for ideal_col in ideal_df.columns[1:]:
        error = mean_squared_error(train_df[train_col], ideal_df[ideal_col])
        deviation = np.max(np.abs(train_df[train_col] - ideal_df[ideal_col]))
        if error < min_error:
            min_error = error
            best_func = ideal_col
            max_dev = deviation
    best_matches[train_col] = best_func
    max_deviations[train_col] = max_dev

conn = sqlite3.connect("mapping_project.db")
train_df.to_sql("training_data", conn, index=False)
ideal_df.to_sql("ideal_functions", conn, index=False)

mapped_results = []

for idx, row in test_df.iterrows():
    x, y = row['x'], row['y']
    for train_col, ideal_col in best_matches.items():
        ideal_y = ideal_df.loc[ideal_df['x'] == x, ideal_col]
        if not ideal_y.empty:
            delta = abs(y - ideal_y.values[0])
            if delta <= max_deviations[train_col] * sqrt(2):
                mapped_results.append([x, y, delta, ideal_col])
                break

mapped_df = pd.DataFrame(mapped_results, columns=["x", "y", "delta_y", "ideal_function"])
mapped_df.to_sql("test_mapping", conn, index=False)

for i, (train_col, ideal_col) in enumerate(best_matches.items()):
    plt.figure()
    plt.plot(train_df["x"], train_df[train_col], label=f"Training: {train_col}")
    plt.plot(ideal_df["x"], ideal_df[ideal_col], label=f"Ideal: {ideal_col}", linestyle="--")
    plt.legend()
    plt.title(f"{train_col} vs {ideal_col}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(f"plot_train_vs_ideal_{i+1}.png")
    plt.close()

plt.figure()
for name, group in mapped_df.groupby("ideal_function"):
    plt.scatter(group["x"], group["y"], label=name, s=10)
plt.legend()
plt.title("Mapped Test Points to Ideal Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("plot_test_mapping.png")
plt.close()