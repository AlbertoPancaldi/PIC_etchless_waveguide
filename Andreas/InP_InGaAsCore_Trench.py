import emodeconnection as emc

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 20,10 # [nm] resolution
num_modes = 1 # [-] number of modes
boundary = '0S' # boundary condition

## Variables to sweep
trench_depth = 6000
core_thickness = 200

## Connect and initialize EMode
em = emc.EMode()

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 20000, window_height = 7000,
    num_modes = num_modes, background_material = 'Air', boundary_condition = boundary,
    pml_NSEW_bool = [0,0,1,1], num_pml_layers = 8) # Layers should be 1024, though nearing 20 makes it stop working

## Draw shapes
em.shape(name = 'layer1', material ='InP', height = 4500, etch_depth = 4000, mask = 4000, sidewall_angle = 45, tone = "p")
em.shape(name = 'cladd_1', material = 'InP', height = 1000, shape_type = "conformal")
em.shape(name = 'core', material = 'InGaAs', height = 150, shape_type = "conformal")
em.shape(name = 'cladd_2', material = 'InP', height = 1000, shape_type = "conformal")

# Try for both InP/InGaAs and SiO2/SiN (or just Si), copy the table

## Launch FDM solver
em.FDM()

## Display the effective indices, TE fractions, core confinement, and scattering loss
em.confinement()
em.report()

## Attempt at saving
em.plot(component = 'Ex', plot_function = 'abs^2', file_name = 'InPE2', file_type = 'png')
#print('Core Thickness' + core_thickness)

## Plot the field and refractive index profiles
em.plot()

## Close EMode
em.close()
