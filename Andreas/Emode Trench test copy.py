import emodeconnection as emc
import numpy as np

## Set simulation parameters
wavelength = 470 # [nm] wavelength
dx, dy = 20, 20 # [nm] resolution
#w_core = 1000 # [nm] waveguide core width
#w_trench = 1000 # [nm] waveguide side trench width
#h_core = 500 # [nm] waveguide core height
#h_clad = 1000 # [nm] waveguide top and bottom clad
#window_width = w_core + w_trench*2 # [nm]
#window_height = h_core + h_clad*2 # [nm]
num_modes = 1 # [-] number of modes
boundary = 'TE' # boundary condition

## Connect and initialize EMode
em = emc.EMode()

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 18000, window_height = 12000, #13000 by 7000 works for 5x5 resolution, but 13000 is not wide enough...
    num_modes = num_modes, background_material = 'Air',
    boundary_condition = boundary,
    pml_NSEW_bool = [0,0,1,1], num_pml_layers = 40, remove_pml_modes_bool = 0) # Layers should be 1024

#em.material_explorer()

## Draw shapes
em.add_material(name= 'PDMS', refractive_index_equation = '[1.4,1.4,1.4]')
em.add_material(name= 'Parylene_C', refractive_index_equation = '[1.639,1.639,1.639]')

em.shape(name = 'mold', material = 'SiO2', height = 4200, etch_depth = 4000, mask = 4000, tone = 'p', sidewall_angle = 45)
em.shape(name = 'cladding1', material = 'PDMS', height = 1000, shape_type = 'conformal')
em.shape(name = 'core', material = 'Parylene_C', height = 200, shape_type = 'conformal')
em.shape(name = 'cladding2', material = 'PDMS', height = 1000, shape_type = 'conformal')

## Solve
em.FDM()

em.report()

em.plot(component = 'Ex', file_name = 'field_plot', file_type = 'png')

em.plot()

em.save()

## Close EMode
em.close()