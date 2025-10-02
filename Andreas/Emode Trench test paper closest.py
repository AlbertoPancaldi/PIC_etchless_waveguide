import emodeconnection as emc

## Set simulation parameters
wavelength = 470 # [nm] wavelength
dx, dy = 20, 10 # [nm] resolution
num_modes = 1 # [-] number of modes
boundary = '0S' # boundary condition, should probably be TE, but that gives poor results

## Connect and initialize EMode
em = emc.EMode(simulation_name = 'Paper_Trench')

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 16000, window_height = 7000, #13000 by 7000 works for 5x5 resolution, but 13000 is not wide enough...
    num_modes = num_modes, background_material = 'Air', # If it stops working, it's probs because I changed this from air
    boundary_condition = boundary, simulation_name = 'Paper_Trench',
    pml_NSEW_bool = [0,0,1,1], num_pml_layers = 20) # Layers should be 1024, though nearing 20 makes it stop working

#em.material_explorer()

## Draw shapes
em.add_material(name= 'PDMS', refractive_index_equation = '[1.4,1.4,1.4]', simulation_name = 'Paper_Trench')
em.add_material(name= 'Parylene_C', refractive_index_equation = '[1.639,1.639,1.639]', simulation_name = 'Paper_Trench')

em.shape(name = 'mold', material = 'SiO2', height = 4200, etch_depth = 4000, mask = 4000,
         tone = 'p', sidewall_angle = 45, simulation_name = 'Paper_Trench')
em.shape(name = 'cladding1', material = 'PDMS', height = 1000, shape_type = 'conformal', simulation_name = 'Paper_Trench')
em.shape(name = 'core', material = 'Parylene_C', height = 150, shape_type = 'conformal', simulation_name = 'Paper_Trench')
em.shape(name = 'cladding2', material = 'PDMS', height = 1000, shape_type = 'conformal', simulation_name = 'Paper_Trench')

## Solve
em.FDM(simulation_name = 'Paper_Trench')

## Display the effective indices, TE fractions, core confinement, and scattering loss
em.confinement(simulation_name = 'Paper_Trench')
em.report(save = True, file_name = 'Paper_Trench_report', simulation_name = 'Paper_Trench')

#em.plot(component = 'Ex', file_name = 'field_plot', file_type = 'png', simulation_name = 'Paper_Trench')

em.plot(simulation_name = 'Paper_Trench')

em.save(simulation_name = 'Paper_Trench') #Please fucking work

## Close EMode
em.close(simulation_name = 'Paper_Trench')