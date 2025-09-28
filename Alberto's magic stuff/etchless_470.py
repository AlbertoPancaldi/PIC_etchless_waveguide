import emodeconnection as emc
import numpy as np

## Set simulation parameters
wavelength = 470 # [nm] wavelength
dx, dy = 10, 10 # [nm] resolution

num_modes = 1 # [-] number of modes
boundary = 'TE' # boundary condition

## Connect and initialize EMode
em = emc.EMode()

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 13000, window_height = 7000,
    num_modes = num_modes, background_material = 'Air',

    # --- PML boundaries ---
    # order: [North, South, East, West]
    pml_NSEW_bool=[0, 0, 1, 1],      # enable PML on all 4 sides
    num_pml_layers=12,               # 8–16 typical; can also be [N,S,E,W]
    remove_pml_modes_bool=True       # filter out spurious PML modes
)

Parylene_C = em.add_material(name='ParyleneC', refractive_index_equation = '[1.639, 1.639, 1.639]')
PDMS = em.add_material(name = 'PDMS', refractive_index_equation = '[1.4,1.4,1.4]')

## Draw shapes
em.shape(name = 'layer1', material ='PDMS', height = 4500, etch_depth = 4000, mask = 4000, sidewall_angle = 45, tone = "p")
em.shape(name = 'cladd_1', material = 'PDMS', height = 1000, shape_type = "conformal")
em.shape(name = 'core', material = 'ParyleneC', height = 200, shape_type = "conformal")
em.shape(name = 'cladd_2', material = PDMS, height = 1000, shape_type = "conformal")

## Solve the first mode
em.FDM()
em.report()
em.plot()

## Close EMode
em.close()
