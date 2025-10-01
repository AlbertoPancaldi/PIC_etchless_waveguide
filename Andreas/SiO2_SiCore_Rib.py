import emodeconnection as emc

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 10,10 # [nm] resolution
num_modes = 1 # [-] number of modes
boundary = '00' # boundary condition

## Connect and initialize EMode
em = emc.EMode()

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 22000, window_height = 14000,
    num_modes = num_modes, background_material = 'Air',
    boundary_condition = boundary)

## Draw shapes
em.shape(name = 'BOX', material = 'SiO2', height = 4000)
em.shape(name = 'core', material = 'Si', height = 400,
    mask = 4000, etch_depth = 200, fill_material = 'Air')

## Launch FDM solver
em.FDM()

## Display the effective indices, TE fractions, core confinement, and scattering loss
em.confinement()
em.report()

## Plot the field and refractive index profiles
em.plot()

## Close EMode
em.close()
