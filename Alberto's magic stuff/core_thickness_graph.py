#!/usr/bin/env python3
"""Plot trench waveguide metrics from a CSV.

Generates TWO figures:
  1) Leakage loss (left y) and effective index n_eff (right y) vs core thickness.
     -> scatter points with DIFFERENT colors + connecting lines for both series.
  2) Passive loss and leakage loss vs core thickness (both left y).
     -> scatter points with DIFFERENT colors + connecting lines for both series.
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==== Inputs ====
csv_path = "/Users/albertopancaldi/Documents/Python/PIC/PIC_etchless_waveguide/Alberto's magic stuff/trench_data.csv"
output_1 = "core_thickness_leakage_neff.png"      # Figure 1: leakage + n_eff
output_2 = "core_thickness_passive_leakage.png"   # Figure 2: passive + leakage

# Assumed material absorption (dB/cm) for passive-loss estimate
alpha_core_dBcm = 3*10**4   # Core absorption (dB/cm)
alpha_clad_dBcm = 0.4     # Cladding absorption (dB/cm)

# ==== Load & compute ====
df = pd.read_csv(csv_path)
df = df.sort_values("core_thickness_nm")  # ensure ascending x

# Compute passive absorption loss (dB/cm) from confinement
gamma = df["core_confinement_percent"] / 100.0
df["passive_loss_dB_per_cm"] = gamma * alpha_core_dBcm + (1.0 - gamma) * alpha_clad_dBcm
df["leakage_loss_dB_per_cm"] = df["leakage_loss_dB_per_cm"] / 100.0 

x = df["core_thickness_nm"]
y_leak = df["leakage_loss_dB_per_cm"]
y_pass = df["passive_loss_dB_per_cm"]
y_neff = df["n_eff"]

# Colors (user requested different colors)
c_leak = "tab:blue"
c_pass = "tab:green"
c_neff = "tab:orange"

# ==== Figure 1: Leakage loss (left) + n_eff (right) ====
fig1, ax_left_1 = plt.subplots()
ax_right_1 = ax_left_1.twinx()

# Scatter + connecting line for leakage (left axis)
ax_left_1.scatter(x, y_leak, marker="o", color=c_leak)
ax_left_1.plot(x, y_leak, color=c_leak, linewidth=0.8, label="Leakage loss (dB/cm)")

# Scatter + connecting line for n_eff (right axis)
ax_right_1.scatter(x, y_neff, marker="s", color=c_neff)
ax_right_1.plot(x, y_neff, color=c_neff, linewidth=0.8, label="n_eff")

ax_left_1.set_xlabel("Core thickness (nm)")
ax_left_1.set_ylabel("Leakage loss (dB/cm)")
ax_right_1.set_ylabel("Effective index $n_\\mathrm{eff}$")
ax_left_1.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)

# Combined legend (use the line handles to avoid duplicate entries from scatter)
h_left_1, l_left_1 = ax_left_1.get_legend_handles_labels()
h_right_1, l_right_1 = ax_right_1.get_legend_handles_labels()
ax_left_1.legend(h_left_1 + h_right_1, l_left_1 + l_right_1, loc="best")

fig1.tight_layout()
fig1.savefig(output_1, dpi=200)

# ==== Figure 2: Passive loss + Leakage loss (both left axis) ====
fig2, ax_left_2 = plt.subplots()

# Scatter + connecting line for leakage
ax_left_2.scatter(x, y_leak, marker="o", color=c_leak)
ax_left_2.plot(x, y_leak, color=c_leak, linewidth=0.8, label="Leakage loss (dB/cm)")

# Scatter + connecting line for passive
ax_left_2.scatter(x, y_pass, marker="^", color=c_pass)
ax_left_2.plot(x, y_pass, color=c_pass, linewidth=0.8, label="Passive loss (dB/cm)")

ax_left_2.set_xlabel("Core thickness (nm)")
ax_left_2.set_ylabel("Loss (dB/cm)")
ax_left_2.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
ax_left_2.legend(loc="best")

fig2.tight_layout()
fig2.savefig(output_2, dpi=200)

plt.show()