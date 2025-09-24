import emodeconnection as emc
import numpy as np

## Set simulation parameters
wavelength = 470 # [nm] wavelength
dx, dy = 10, 10 # [nm] resolution

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
    window_width = 13000, window_height = 7000,
    num_modes = num_modes, background_material = 'Air',
    boundary_condition = boundary, pml_NSEW_bool = [0,0,1,1], num_pml_layers = 50)

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
