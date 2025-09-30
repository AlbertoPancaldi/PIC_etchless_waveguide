import emodeconnection as emc
import numpy as np

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 20,10 # [nm] resolution

# w_core = 1000 # [nm] waveguide core width
# w_trench = 1000 # [nm] waveguide side trench width

# h_core = 500 # [nm] waveguide core height
# h_clad = 1000 # [nm] waveguide top and bottom clad

num_modes = 1 # [-] number of modes
boundary = '00' # boundary condition

## Connect and initialize EMode
em = emc.EMode()

# ## View material databas
# em.material_explorer()

width = 22000
# width_core = 12000

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = width, window_height = 14000,
    num_modes = num_modes, background_material = 'Air', boundary_condition = boundary)
    # pml_NSEW_bool = [0,0,1,1], num_pml_layers = 20)

Parylene_C = em.add_material(name='ParyleneC', refractive_index_equation = '[1.639, 1.639, 1.639]')
PDMS = em.add_material(name = 'PDMS', refractive_index_equation = '[1.4,1.4,1.4]')
Si3N4 = em.add_material(name = 'Si3N4', refractive_index_equation = '[1.99608,1.99608,1.99608]')

## Draw shapes
em.shape(name = 'layer1', material ='SiO2', height = 7500, etch_depth = 7000, mask = 6000, sidewall_angle = 45, tone = "p")

em.shape(name = 'cladd_1', material = 'SiO2', height = 1000, shape_type = "conformal")

em.shape(name = 'core', material = 'Si', height = 200, shape_type = "conformal")

em.shape(name = 'cladd_2', material = 'SiO2', height = 1000, shape_type = "conformal")

## Solve the first mode
em.FDM()

em.confinement()
em.report()

em.plot()

## Close EMode
em.close()
