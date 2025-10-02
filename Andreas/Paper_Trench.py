import emodeconnection as emc

## Set simulation parameters
wavelength = 470 # [nm] wavelength
dx, dy = 20, 10 # [nm] resolution
num_modes = 1 # [-] number of modes
boundary = '0S' # boundary condition

## Connect and initialize EMode
em = emc.EMode(simulation_name = 'Paper_Trench') # custom file name instead of the default "emode.eph"

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 20000, window_height = 12000,
    num_modes = num_modes, background_material = 'Air',
    boundary_condition = boundary)
    #pml_NSEW_bool = [0,0,1,1], num_pml_layers = 10) # Keep layer count low, or errors happen, bad in general.

## Draw shapes
em.add_material(name= 'PDMS', refractive_index_equation = '[1.4,1.4,1.4]')
em.add_material(name= 'Parylene_C', refractive_index_equation = '[1.639,1.639,1.639]')

em.shape(name = 'mold', material = 'SiO2', height = 4200, etch_depth = 4000, mask = 4000, tone = 'p', sidewall_angle = 45)
em.shape(name = 'cladding1', material = 'PDMS', height = 1000, shape_type = 'conformal')
em.shape(name = 'core', material = 'Parylene_C', height = 200, shape_type = 'conformal')
em.shape(name = 'cladding2', material = 'PDMS', height = 1000, shape_type = 'conformal')

## Launch FDM solver
em.FDM()

## Display the effective indices, TE fractions, core confinement, and scattering loss
em.confinement()
em.report()

## Plot the field and refractive index profiles
em.plot()

## Close EMode
em.close()