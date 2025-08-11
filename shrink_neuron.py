import pandas as pd
import numpy as np

shrink_by = 0.75
fname = 'Rorb-IRES2-Cre-D_Ai14_IVSCC_-168052.03.02.01_397999191_m.swc'
#fname = 'test.swc'
nfname = fname[:-4] + '_shrinked_' + str(shrink_by) + '.swc'
data = pd.read_csv(fname, names=['id', 'type', 'x', 'y', 'z', 'r', 'pid'],
                   skiprows=3, delimiter=' ')

# new_data = pd.DataFrame(columns=['id', 'type', 'x', 'y', 'z', 'r', 'pid'])
# new_data = pd.concat([data[data['pid']==-1]])  # Immediately add SOMA

soma = data[data['pid']==-1]
new_data = {np.int16(soma['id'][0]) : [soma['x'][0], soma['y'][0], soma['z'][0]]}


def interpolate_points(p1, p2, fraction):
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    # Vector from p1 to p2
    v = p2 - p1
    # Calculate the new point using linear interpolation/extrapolation
    new_point = p1 + fraction * v
    return new_point


def shrink_surfarea(data, new_data, factor):
    # factor = np.sqrt((100-percent)/100.)
    print('Shrinking lenght and diam by: ', factor)
    lines = ['# Generated with a script to shrink the dims of neuron by %s \n' % factor]
    with open(fname, 'r') as ff:
        meta_data = ff.readlines()
    lines.extend(meta_data[:3])
    for index, row in data.iterrows():  # not the best way, but okay for now
        if row['pid'] == -1:
            new_line = [np.int16(row['id']), np.int16(row['type']),
                        row['x'], row['y'], row['z'],
                        row['r']*factor, np.int16(row['pid'])]
            pass
        else:
            xx, yy, zz, rr = row['x'], row['y'], row['z'], row['r']  # current row
            parent_id = np.int16(row['pid']) # its parent id
            px, py, pz = new_data[parent_id] # its transitioned point

            parent_df = data[data['id'] == parent_id]
            parent_or = parent_df.iloc[0, :]
            pxx, pyy, pzz = parent_or['x'], parent_or['y'], parent_or['z'] # parents orignal point
            new_point = interpolate_points([px, py, pz],
                                           [xx-(pxx-px), yy-(pyy-py), zz-(pzz-pz)],
                                           factor)
            nx, ny, nz = new_point.tolist()
            dx, dy, dz = nx, ny, nz
            new_data[np.int16(row['id'])] = [np.float64(dx),
                                             np.float64(dy),
                                             np.float64(dz)]
            new_line = [np.int16(row['id']), np.int16(row['type']),
                        dx, dy, dz,
                        row['r']*factor, np.int16(row['pid'])]
        lines.append(" ".join(str(x) for x in new_line) + '\n')
    with open(nfname, 'w') as f:
        f.writelines(lines)
    return new_data

new_data = shrink_surfarea(data, new_data, shrink_by)

