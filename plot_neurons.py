import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_line_between_3d_points(ax, point1, point2, color='k'):
    """
    Draws a line between two 3D points using Matplotlib.

    Args:
        point1 (tuple or list): A tuple or list representing the first 3D point (x, y, z).
        point2 (tuple or list): A tuple or list representing the second 3D point (x, y, z).
    """
    if len(point1) != 3 or len(point2) != 3:
        raise ValueError("Both points must be 3D points (i.e., have 3 coordinates).")
    x_coords = [point1[0], point2[0]]
    y_coords = [point1[1], point2[1]]
    z_coords = [point1[2], point2[2]]
    ax.plot(x_coords, y_coords, z_coords, linestyle='-', color=color)
    return ax


def each_pair(fname, skiprows=3):
    point_list = []
    data = pd.read_csv(fname, names=['id', 'type', 'x', 'y', 'z', 'r', 'pid'],
                       skiprows=skiprows, delimiter=' ')
    for index, row in data.iterrows():  # not the best way, but okay for now
        if row['pid'] == -1:
            pass
        else:
            pid = np.int16(row['pid'])
            parent_df = data[data['id'] == pid]
            parent = parent_df.iloc[0, :]
            p1 = [parent['x'], parent['y'], parent['z']]
            p2 = [row['x'], row['y'], row['z']]
            point_list.append([p1, p2])
    return point_list
    
if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    fname = 'Rorb-IRES2-Cre-D_Ai14_IVSCC_-168052.03.02.01_397999191_m.swc'
    #fname = 'test.swc'
    nfname = fname[:-4] + '_shrinked.swc'
    point_list = each_pair(fname)
    for pts in point_list:
        pt1, pt2 = pts
        ax = plot_line_between_3d_points(ax, pt1, pt2)
    point_list = each_pair(nfname, skiprows=4)
    for pts in point_list:
        pt1, pt2 = pts
        ax = plot_line_between_3d_points(ax, pt1, pt2, color='r')
        
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # plt.savefig('3d_line_plot.png')
    # #plt.close(fig)
    plt.show()
