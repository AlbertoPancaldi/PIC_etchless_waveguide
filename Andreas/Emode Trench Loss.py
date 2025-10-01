import emodeconnection as emc

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 5, 5 # [nm] resolution
#w_core = 1000 # [nm] waveguide core width
#w_trench = 1000 # [nm] waveguide side trench width
#h_core = 500 # [nm] waveguide core height
#h_clad = 1000 # [nm] waveguide top and bottom clad
#window_width = w_core + w_trench*2 # [nm]
#window_height = h_core + h_clad*2 # [nm]
num_modes = 1 # [-] number of modes
boundary = '0S' # boundary condition, should probably be TE, but that gives poor results

## Connect and initialize EMode
em = emc.EMode(simulation_name = 'trench')

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 14000, window_height = 7000,
    num_modes = num_modes, background_material = 'Air',
    boundary_condition = boundary)
    #pml_NSEW_bool = [0,0,1,1], num_pml_layers = 10) # Keep layer count low, or errors happen

#em.material_explorer()

# TRY INSTEAD WITH InP CLADDING AND THE CLOSEST THING TO INGAASP CORE

## Draw shapes
em.shape(name = 'mold', material = 'InP', height = 4200, etch_depth = 4000, mask = 4000, tone = 'p', sidewall_angle = 45)
em.shape(name = 'cladding1', material = 'InP', height = 1000, shape_type = 'conformal')
em.shape(name = 'core', material = 'InGaAs', height = 200, shape_type = 'conformal', #There's no InGaAsP, using InGaAs instead
    roughness_rms = [5, 0.2], correlation_length = [100, 80]) #From example
em.shape(name = 'cladding2', material = 'InP', height = 1000, shape_type = 'conformal')

## Solve
em.FDM()


em.confinement(shape_list = 'core')
#em.scattering(shape = 'core')
em.report()

em.plot()

## Display scattering loss details from the core, all this from example
shape_core = em.get('shape_core')
sv = shape_core['metadata']['scattering_vertical_edges']
sh = shape_core['metadata']['scattering_horizontal_edges']
sT = shape_core['metadata']['scattering_sum']
print('Scattering loss from all vertical edges: %0.1f dB/m' % sv[0])
print('Scattering loss from all horizontal edges: %0.1f dB/m' % sh[0])
print('Total scattering loss: %0.1f dB/m\n' % sT[0])
edges = shape_core['metadata']['edges']
sa = shape_core['metadata']['scattering_all_edges']
for kk in range(len(edges)):
    print('From', edges[kk][0], 'to', edges[kk][1])
    print('    scattering loss = %0.1f dB/m\n' % sa[0][kk])


em.plot()

em.save(new_save_path = '.') #Please fucking work

## Close EMode
em.close()