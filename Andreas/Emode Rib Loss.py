import emodeconnection as emc

## Set simulation parameters
wavelength = 1550 # [nm] wavelength
dx, dy = 5, 5 # [nm] resolution
w_core = 600 # [nm] waveguide core width
w_trench = 800 # [nm] waveguide side trench width
h_core = 500 # [nm] waveguide core height
h_clad = 800 # [nm] waveguide top and bottom clad
window_width = w_core + w_trench*2 # [nm]
window_height = h_core + h_clad*2 # [nm]
num_modes = 1 # [-] number of modes
boundary = '0S' # boundary condition

## Connect and initialize EMode
em = emc.EMode(simulation_name = 'rib') # custom file name instead of the default "emode.eph"

## Settings
em.settings(
    wavelength = wavelength, x_resolution = dx, y_resolution = dy,
    window_width = 10000, window_height = 7000,
    num_modes = num_modes, background_material = 'Air',
    boundary_condition = boundary)

## Draw shapes
em.shape(name = 'BOX', material = 'InP', height = h_clad)
em.shape(name = 'core', material = 'InGaAs', height = 400,
    mask = 4000, etch_depth = 200, fill_material = 'Air',
    roughness_rms = [5, 0.2], correlation_length = [100, 80]) #From example

## Launch FDM solver
em.FDM()

## Display the effective indices, TE fractions, core confinement, and scattering loss
em.confinement(shape_list = 'core')
em.scattering(shape = 'core')
em.report()

## Display scattering loss details from the core
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

## Plot the field and refractive index profiles
em.plot()

## Close EMode
em.close()