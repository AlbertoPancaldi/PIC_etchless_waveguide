import emodeconnection as emc
import numpy as np

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 20,10 # [nm] resolution

num_modes = 1 # [-] number of modes
boundary = '00' # boundary condition

## Connect and initialize EMode
em = emc.EMode()

width = 22000

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = width, window_height = 14000,
    num_modes = num_modes, background_material = 'Air', boundary_condition = boundary)

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
