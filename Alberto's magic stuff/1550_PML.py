import emodeconnection as emc
import numpy as np

# --- Params (keep yours) ---
wavelength = 1550         # [nm]
dx, dy = 20, 20           # [nm]
num_modes = 1
boundary = '00'           # or 'TE' / 'TM' if you want symmetry speedups

em = emc.EMode()

# Add a few microns of buffer from device to PML (3–5 µm is a good start at 1550 nm)
window_w = 22000          # [nm] (your value)
window_h = 14000          # [nm] (your value)

em.settings(
    wavelength = wavelength,
    x_resolution = dx, y_resolution = dy,
    window_width = window_w, window_height = window_h,
    num_modes = num_modes,
    background_material = 'Air',
    boundary_condition = boundary,

    # --- PML controls ---
    pml_NSEW_bool = [1,1,1,1],     # enable PML on all four sides
    num_pml_layers = 14,           # start with 12–16; increase for convergence
    remove_pml_modes_bool = True,

    # (optional) stretch the outer mesh to save time (bigger cells near edges)
    expansion_size = [3000,3000,3000,3000],        # [nm] each side
    expansion_resolution = [40,40,40,40]           # [nm] coarser in the perimeter
)

# --- Your stack ---
em.shape(name='layer1', material='SiO2', height=7500, etch_depth=7000, mask=6000,
         sidewall_angle=45, tone="p")
em.shape(name='cladd_1', material='SiO2', height=1000, shape_type="conformal")
em.shape(name='core',    material='Si',   height=200,  shape_type="conformal")
em.shape(name='cladd_2', material='SiO2', height=1000, shape_type="conformal")

# Solve
em.FDM()

# Read loss and convert to dB/cm + Im(neff)
alpha_dB_per_m = em.get('loss_dB_per_m')          # total propagation loss from the mode solver
alpha_dB_per_cm = alpha_dB_per_m / 100.0
lam_m = wavelength * 1e-9
n_im = alpha_dB_per_m * lam_m / 54.575            # Im(neff) from EMode’s formula

print(f"loss = {alpha_dB_per_cm:.4e} dB/cm,  Im(neff) = {n_im:.3e}")

em.report()
em.plot()
em.close()



