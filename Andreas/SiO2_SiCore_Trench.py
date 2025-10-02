import emodeconnection as emc

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 20,10 # [nm] resolution
num_modes = 1 # [-] number of modes
boundary = '00' # boundary condition

## Variables to sweep
trench_depth = 6000
core_thickness = 200

## Connect and initialize EMode
em = emc.EMode()

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 22000, window_height = 14000,
    num_modes = num_modes, background_material = 'Air', boundary_condition = boundary)

## Draw shapes
em.shape(name = 'layer1', material ='SiO2', height = 7500, etch_depth = 7000, mask = 6000, sidewall_angle = 45, tone = "p")
em.shape(name = 'cladd_1', material = 'SiO2', height = 1000, shape_type = "conformal")
em.shape(name = 'core', material = 'Si', height = core_thickness, shape_type = "conformal")
em.shape(name = 'cladd_2', material = 'SiO2', height = 1000, shape_type = "conformal")

## Launch FDM solver
em.FDM()

## Display the effective indices, TE fractions, core confinement, and scattering loss
em.confinement()
em.report()

## Plot the field and refractive index profiles
em.plot()

## Close EMode
em.close()
