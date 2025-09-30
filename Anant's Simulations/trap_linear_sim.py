import emodeconnection as emc
import numpy as np

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 10,10 # [nm] resolution

# w_core = 1000 # [nm] waveguide core width
# w_trench = 1000 # [nm] waveguide side trench width

# h_core = 500 # [nm] waveguide core height
# h_clad = 1000 # [nm] waveguide top and bottom clad

num_modes = 1 # [-] number of modes
boundary = 'TE' # boundary condition

## Connect and initialize EMode
em = emc.EMode()

# ## View material database
# em.material_explorer()

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 6000, window_height = 6000,
    num_modes = num_modes, background_material = 'Air', boundary_condition = boundary,
    pml_NSEW_bool = [1,1,1,1], num_pml_layers = 20)

Parylene_C = em.add_material(name='Parylene_C', refractive_index_equation = '[1.639, 1.639, 1.639]')
PDMS = em.add_material(name = 'PDMS', refractive_index_equation = '[1.4,1.4,1.4]')

## Draw shapes

em.shape(name = 'cladd_1', material = 'PDMS', height = 1000)

em.shape(name = 'core', material = 'InGaP', height = 200)

em.shape(name = 'cladd_2', material = 'PDMS', height = 1000)

## Solve the first mode
em.FDM()

em.report()

em.plot()

## Close EMode
em.close()
