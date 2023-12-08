import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("../20_intermediate_files/final_merged_table.csv")

######################### Pre-Post Model Comparison on Morphine Equivalent mg Per Capita #########################
# Calculate Morphine mg per capita for each county
data["morphine_mg_per_capita"] = data["total_morphine_mg"] / data["total_population"]

# Group by year and state to calculate the mean and standard error of Morphine mg per capita across all counties
state_year_avg = (
    data.groupby(["year", "state"])["morphine_mg_per_capita"]
    .agg(["mean", "sem"])
    .reset_index()
)

# Set the policy change year for Florida (FL)
policy_change_year_fl = 2010

# Normalize years relative to the policy change year for FL
state_year_avg_fl = state_year_avg[state_year_avg["state"] == "FL"].copy()
state_year_avg_fl["years_from_policy"] = (
    state_year_avg_fl["year"] - policy_change_year_fl
)

# Sort the dataframe by 'years_from_policy' to ensure the line connects points in the correct order
state_year_avg_fl = state_year_avg_fl.sort_values("years_from_policy")

# Create the Florida (FL) graph
fig, ax_fl = plt.subplots(figsize=(8, 6))

# Define colors for error bars and lines
error_bar_color = "#2B2F42"
line_color_before = "#8D99AE"
line_color_after = "#D80032"

# Separate the data into before and after the policy change
before_policy_change = state_year_avg_fl[state_year_avg_fl["years_from_policy"] < 0]
after_policy_change = state_year_avg_fl[state_year_avg_fl["years_from_policy"] >= 0]

# Plot the mean with error bars for each period
ax_fl.errorbar(
    before_policy_change["years_from_policy"],
    before_policy_change["mean"],
    yerr=before_policy_change["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_before,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2006-2010",
)
ax_fl.errorbar(
    after_policy_change["years_from_policy"],
    after_policy_change["mean"],
    yerr=after_policy_change["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_after,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2011-2015",
)

# Set y-axis to start from 0
ax_fl.set_ylim(bottom=0)

# Additional plot formatting
ax_fl.axvline(x=0, color="black", linestyle="--", label="Policy Change (2010)")
ax_fl.set_title(
    "The Effect of Policy on Morphine Milligram Equivalent Per Capita in FL"
)
ax_fl.set_xlabel("Years from Policy Change")
ax_fl.set_ylabel("Morphine Milligram Equivalent Per Capita")
ax_fl.legend()

# Define the directory to save the graphs
result_directory = "../30_results"  # Replace with your actual path
os.makedirs(result_directory, exist_ok=True)

# Save the Florida (FL) graph as a PNG file in the result directory
fl_graph_filename = os.path.join(result_directory, "FL_MEE_Change_Avg.png")
plt.tight_layout()
plt.savefig(fl_graph_filename, dpi=300)
plt.close()  # Close the figure to avoid display

# Now, let's create a similar plot for Washington (WA)
policy_change_year_wa = 2012  # Set the policy change year for Washington (WA)

# Normalize years relative to the policy change year for WA
state_year_avg_wa = state_year_avg[state_year_avg["state"] == "WA"].copy()
state_year_avg_wa["years_from_policy"] = (
    state_year_avg_wa["year"] - policy_change_year_wa
)

# Sort the dataframe by 'years_from_policy' to ensure the line connects points in the correct order
state_year_avg_wa = state_year_avg_wa.sort_values("years_from_policy")

# Create the Washington (WA) graph
fig, ax_wa = plt.subplots(figsize=(8, 6))

# Separate the data into before and after the policy change
before_policy_change_wa = state_year_avg_wa[state_year_avg_wa["years_from_policy"] < 0]
after_policy_change_wa = state_year_avg_wa[state_year_avg_wa["years_from_policy"] >= 0]

# Plot the mean with error bars for each period
ax_wa.errorbar(
    before_policy_change_wa["years_from_policy"],
    before_policy_change_wa["mean"],
    yerr=before_policy_change_wa["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_before,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2006-2012",
)
ax_wa.errorbar(
    after_policy_change_wa["years_from_policy"],
    after_policy_change_wa["mean"],
    yerr=after_policy_change_wa["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_after,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2013-2015",
)

# Set y-axis to start from 0
ax_wa.set_ylim(bottom=0)

# Additional plot formatting
ax_wa.axvline(x=0, color="black", linestyle="--", label="Policy Change (2012)")
ax_wa.set_title(
    "The Effect of Policy on Morphine Milligram Equivalent Per Capita in WA"
)
ax_wa.set_xlabel("Years from Policy Change")
ax_wa.set_ylabel("Morphine Milligram Equivalent Per Capita")
ax_wa.legend()

# Save the Washington (WA) graph as a PNG file in the result directory
wa_graph_filename = os.path.join(result_directory, "WA_MEE_Change_Avg.png")
plt.tight_layout()
plt.savefig(wa_graph_filename, dpi=300)
plt.close()  # Close the figure to avoid display

###################################### Pre-Post Model Comparison on Mortality Rate ######################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("../20_intermediate_files/final_merged_table.csv")

# Group by year and state to calculate the mean and standard error of Morphine mg per capita across all counties
state_year_avg = (
    data.groupby(["year", "state"])["filled_mortality_rate"]
    .agg(["mean", "sem"])
    .reset_index()
)

# Set the policy change year for Florida (FL)
policy_change_year_fl = 2010

# Normalize years relative to the policy change year for FL
state_year_avg_fl = state_year_avg[state_year_avg["state"] == "FL"].copy()
state_year_avg_fl["years_from_policy"] = (
    state_year_avg_fl["year"] - policy_change_year_fl
)

# Sort the dataframe by 'years_from_policy' to ensure the line connects points in the correct order
state_year_avg_fl = state_year_avg_fl.sort_values("years_from_policy")

# Create the Florida (FL) graph
fig, ax_fl = plt.subplots(figsize=(8, 6))

# Define colors for error bars and lines
error_bar_color = "#2B2F42"
line_color_before = "#8D99AE"
line_color_after = "#D80032"

# Separate the data into before and after the policy change
before_policy_change = state_year_avg_fl[state_year_avg_fl["years_from_policy"] < 0]
after_policy_change = state_year_avg_fl[state_year_avg_fl["years_from_policy"] >= 0]

# Plot the mean with error bars for each period
ax_fl.errorbar(
    before_policy_change["years_from_policy"],
    before_policy_change["mean"],
    yerr=before_policy_change["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_before,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2006-2010",
)
ax_fl.errorbar(
    after_policy_change["years_from_policy"],
    after_policy_change["mean"],
    yerr=after_policy_change["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_after,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2011-2015",
)

# Set y-axis to start from 0
ax_fl.set_ylim(bottom=0)

# Additional plot formatting
ax_fl.axvline(x=0, color="black", linestyle="--", label="Policy Change (2010)")
ax_fl.set_title(
    "The Effect of Policy on Unintentional Drug Poisoning Mortality Rate in FL"
)
ax_fl.set_xlabel("Years from Policy Change")
ax_fl.set_ylabel("Unintentional Drug Poisoning Mortality Rate")
ax_fl.legend()

# Define the directory to save the graphs
result_directory = "../30_results"  # Replace with your actual path
os.makedirs(result_directory, exist_ok=True)

# Save the Florida (FL) graph as a PNG file in the result directory
fl_graph_filename = os.path.join(result_directory, "FL_MortalityRate_Change_Avg.png")
plt.tight_layout()
plt.savefig(fl_graph_filename, dpi=300)
plt.close()  # Close the figure to avoid display

# Now, let's create a similar plot for Washington (WA)
policy_change_year_wa = 2012  # Set the policy change year for Washington (WA)

# Normalize years relative to the policy change year for WA
state_year_avg_wa = state_year_avg[state_year_avg["state"] == "WA"].copy()
state_year_avg_wa["years_from_policy"] = (
    state_year_avg_wa["year"] - policy_change_year_wa
)

# Sort the dataframe by 'years_from_policy' to ensure the line connects points in the correct order
state_year_avg_wa = state_year_avg_wa.sort_values("years_from_policy")

# Create the Washington (WA) graph
fig, ax_wa = plt.subplots(figsize=(8, 6))

# Separate the data into before and after the policy change
before_policy_change_wa = state_year_avg_wa[state_year_avg_wa["years_from_policy"] < 0]
after_policy_change_wa = state_year_avg_wa[state_year_avg_wa["years_from_policy"] >= 0]

# Plot the mean with error bars for each period
ax_wa.errorbar(
    before_policy_change_wa["years_from_policy"],
    before_policy_change_wa["mean"],
    yerr=before_policy_change_wa["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_before,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2006-2012",
)
ax_wa.errorbar(
    after_policy_change_wa["years_from_policy"],
    after_policy_change_wa["mean"],
    yerr=after_policy_change_wa["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_after,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2013-2015",
)

# Set y-axis to start from 0
ax_wa.set_ylim(bottom=0)

# Additional plot formatting
ax_wa.axvline(x=0, color="black", linestyle="--", label="Policy Change (2012)")
ax_wa.set_title(
    "The Effect of Policy on Unintentional Drug Poisoning Mortality Rate in WA"
)
ax_wa.set_xlabel("Years from Policy Change")
ax_wa.set_ylabel("Unintentional Drug Poisoning Mortality Rate")
ax_wa.legend()

# Save the Washington (WA) graph as a PNG file in the result directory
wa_graph_filename = os.path.join(result_directory, "WA_MortalityRate_Change_Avg.png")
plt.tight_layout()
plt.savefig(wa_graph_filename, dpi=300)
plt.close()  # Close the figure to avoid display


# Now, let's create a similar plot for Texas (TX)
policy_change_year_tx = 2007  # Set the policy change year for Texas (TX)

# Normalize years relative to the policy change year for TX
state_year_avg_tx = state_year_avg[state_year_avg["state"] == "TX"].copy()
state_year_avg_tx["years_from_policy"] = (
    state_year_avg_tx["year"] - policy_change_year_tx
)

# Sort the dataframe by 'years_from_policy' to ensure the line connects points in the correct order
state_year_avg_tx = state_year_avg_tx.sort_values("years_from_policy")

# Create the Texas (TX) graph
fig, ax_tx = plt.subplots(figsize=(8, 6))

# Separate the data into before and after the policy change
before_policy_change_tx = state_year_avg_tx[state_year_avg_tx["years_from_policy"] < 0]
after_policy_change_tx = state_year_avg_tx[state_year_avg_tx["years_from_policy"] >= 0]

# Plot the mean with error bars for each period
ax_tx.errorbar(
    before_policy_change_tx["years_from_policy"],
    before_policy_change_tx["mean"],
    yerr=before_policy_change_tx["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_before,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2006-2007",
)
ax_tx.errorbar(
    after_policy_change_tx["years_from_policy"],
    after_policy_change_tx["mean"],
    yerr=after_policy_change_tx["sem"],
    fmt="o-",  # 'o' for circular markers, '-' for a solid line
    color=line_color_after,
    ecolor=error_bar_color,
    capsize=3,  # Set the size of the caps on the error bars
    label="2008-2015",
)

# Set y-axis to start from 0
ax_tx.set_ylim(bottom=0)

# Additional plot formatting
ax_tx.axvline(x=0, color="black", linestyle="--", label="Policy Change (2012)")
ax_tx.set_title(
    "The Effect of Policy on Unintentional Drug Poisoning Mortality Rate in TX"
)
ax_tx.set_xlabel("Years from Policy Change")
ax_tx.set_ylabel("Unintentional Drug Poisoning Mortality Rate")
ax_tx.legend()

# Save the Texas (TX) graph as a PNG file in the result directory
tx_graph_filename = os.path.join(result_directory, "TX_MortalityRate_Change_Avg.png")
plt.tight_layout()
plt.savefig(tx_graph_filename, dpi=300)
plt.close()  # Close the figure to avoid display
