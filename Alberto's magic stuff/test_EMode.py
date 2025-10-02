import emodeconnection as emc

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 10, 10 # [nm] resolution
w_core = 600 # [nm] waveguide core width
w_trench = 800 # [nm] waveguide side trench width
h_core = 200 # [nm] waveguide core height
h_clad = 300 # [nm] waveguide top and bottom clad
num_modes = 3 # [-] number of modes
boundary = 'TE' # boundary condition

## Connect and initialize EMode
em = emc.EMode()

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 2000, window_height = h_core + h_clad*2,
    num_modes = num_modes, background_material = 'Air',boundary_condition = boundary,
    pml_NSEW_bool = [0,0,1,1], num_pml_layers = 5
    )

## Draw shapes
em.shape(name = 'BOX', material = 'SiO2', height = 200, width = 2000)
em.shape(name = 'cladd_1', material = 'SiO2', height = 100, width = 2000)
#em.shape(name = 'core', material = 'Si', height = 200, width = 600)
em.shape(name = 'core', material = 'Si', height = 100, shape_type = "conformal")
#em.shape(name = 'cladd_2', material = 'SiO2', height = 100, width = 600)

## Launch FDM solver
em.FDM()

## Display the effective indices, TE fractions, and core confinement
em.confinement()
em.report()

## Plot the field and refractive index profiles
em.plot()

## Close EMode
em.close()