import emodeconnection as emc

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 15,15 # [nm] resolution
num_modes = 1 # [-] number of modes
boundary = '0S' # boundary condition
core_height = 1000 # [nm] waveguide core height

## Connect and initialize EMode
em = emc.EMode()

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 20000, window_height = 10000,
    num_modes = num_modes, background_material = 'Air', boundary_condition = boundary,
    pml_NSEW_bool = [0,1,1,1], num_pml_layers = 4) 

## Draw shapes
em.shape(name = 'layer1', material ='SiO2', height = 6000, etch_depth = 4000, mask = 4000, sidewall_angle = 45, tone = "p")
em.shape(name = 'cladd_1', material = 'SiO2', height = 1000, shape_type = "conformal")
em.shape(name = 'core', material = 'InP', height = core_height, shape_type = "conformal")
em.shape(name = 'cladd_2', material = 'SiO2', height = 1000, shape_type = "conformal")

## Launch FDM solver
em.FDM()

## Display the effective indices, TE fractions, core confinement, and scattering loss
print(f"\nCore height: {core_height} nm")
print(f"Resolution: {dx} nm x {dy} nm")
em.confinement()
em.report()

## Attempt at saving
em.plot(component = 'Ex', plot_function = 'abs^2', file_name = f"InP_SiO2_{core_height}nm", file_type = 'png')

## Plot the field and refractive index profiles
em.plot()

## Close EMode
em.close()
