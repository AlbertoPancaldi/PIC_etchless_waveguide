import emodeconnection as emc

## Set simulation parameters
wavelength = 470 # [nm] wavelength
dx, dy = 15, 15 # [nm] resolution
w_core = 2240 # [nm] waveguide core width
w_trench = 2250 # [nm] waveguide side trench width
h_core = 200 # [nm] waveguide core height
h_clad = 2250 # [nm] waveguide top and bottom clad
window_width = w_core + w_trench*2 # [nm]
window_height = h_core + h_clad*2 # [nm]
num_modes = 1 # [-] number of modes
boundary = 'TE' # boundary condition

bend_radius = 100e3 # [nm] bend radius
x_off = 500 # [nm] waveguide x-offset for applying the bend radius at the center of the waveguide core rather than the center of the window

## Connect and initialize EMode
em = emc.EMode()

## Add custom material
equation = '(1 + 0.6961663/(1 - (0.0684043/x)^2) + 0.4079426/(1 - (0.1162414/x)^2) + 0.8974794/(1 - (9.896161/x)^2))^0.5'
em.add_material(name = 'custom_SiO2',
    refractive_index_equation = equation, wavelength_unit = 'um')

em.add_material(name = 'PDMS', refractive_index_equation = '[1.4,1.4,1.4]')
em.add_material(name='Parylene_C', refractive_index_equation = '[1.639, 1.639, 1.639]')


## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = window_width, window_height = window_height,
    num_modes = num_modes, background_material = 'Air',
    boundary_condition = boundary,
    pml_NSEW_bool = [0,0,1,1], num_pml_layers = 20)

## Draw shapes

em.shape(name = 'layer1', material ='SiO2', width = w_trench, height = 6500, etch_depth = 4000,  mask = 1000, sidewall_angle = 45, tone = "p")

em.shape(name = 'cladd_1', shape_type = 'conformal', material = 'PDMS', height = 1000)

em.shape(name = 'core', shape_type = 'conformal', material = 'Parylene_C', height = 200)

em.shape(name = 'cladd_2', shape_type = 'conformal', material = 'PDMS', height = 1000)

# em.shape(name = 'cladd_1', width = w_trench, material = 'PDMS', height = 1000)

# em.shape(name = 'core', width = w_core,  material = 'Parylene_C', height = 200)

# em.shape(name = 'cladd_2', width = w_trench, material = 'PDMS', height = 1000)


## Launch FDM solver
em.FDM()

## Display the effective indices, loss, and core confinement
em.confinement()
em.report()

# ## Save the field and refractive index profiles plots
# em.plot(component = 'Ex', file_name = 'field_plot', file_type = 'png')
# em.plot(component = 'Index', file_name = 'index_plot', file_type = 'png')

## Plot the field and refractive index profiles
em.plot()

## Collect all variable names and close EMode
variables = em.inspect()
em.close()