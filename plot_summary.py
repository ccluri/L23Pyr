import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def visualize_data(file_path):
    """
    Reads data from a CSV file and visualizes Rin, tau, and RMP as colormaps.

    The plots are organized in a grid where columns represent the variables
    (Rin, tau, RMP) and rows represent unique e_pas values. The x and y
    axes of each colormap correspond to ena and ek values, respectively.

    Args:
        file_path (str): The path to the input CSV file.
    """
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    # Identify the unique values for the parameters that structure the plot
    e_pas_values = sorted(df['e_pas'].unique())
    ena_values = sorted(df['ena'].unique())
    ek_values = sorted(df['ek'].unique())

    # The variables we want to plot
    variables_to_plot = ['Rin', 'tau', 'RMP']

    # Determine the grid size for the subplots
    n_rows = len(e_pas_values)
    n_cols = len(variables_to_plot)
    cbar_lims_rin = (0.7, 1.3)
    cbar_lims_tau = (50, 90)
    cbar_lims_rmp = (-60, -90)
    cbar_range = [cbar_lims_rin, cbar_lims_tau, cbar_lims_rmp]
    
    # Create a figure and a grid of subplots
    # The figure size is adjusted based on the number of rows to ensure readability
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(5 * n_cols, 4 * n_rows), squeeze=False)

    # Iterate over each unique e_pas value to create a row of plots
    for i, e_pas in enumerate(e_pas_values):
        # Filter the DataFrame for the current e_pas value
        df_subset = df[df['e_pas'] == e_pas]

        # Iterate over the variables to plot (Rin, tau, RMP) to create columns
        for j, var in enumerate(variables_to_plot):
            # Pivot the data to create a 2D grid suitable for a colormap.
            # 'ek' will be the rows (y-axis), 'ena' will be the columns (x-axis).
            pivot_table = df_subset.pivot(index='ek', columns='ena', values=var)

            # Select the appropriate subplot
            ax = axes[i, j]

            # Create the colormap using imshow.
            # 'origin="lower"' places the (0,0) index at the bottom-left corner.
            # 'aspect="auto"' allows the plot to fill the subplot area.
            # 'extent' sets the coordinates of the plot edges.
            im = ax.imshow(
                pivot_table.values,
                extent=[ena_values[0], ena_values[-1], ek_values[0], ek_values[-1]],
                #vmin=cbar_range[j][0], vmax=cbar_range[j][1],
                origin='lower',
                aspect='equal',
                #interpolation='nearest' # Use 'nearest' for sharp, un-blurred pixels
            )

            # Add a colorbar to the subplot to show the scale of the variable
            fig.colorbar(im, ax=ax, label=var)

            # Set the title and labels for the subplot
            ax.set_title(f'{var} (e_pas = {e_pas})')
            ax.set_xlabel('ena (mV)')
            ax.set_ylabel('ek (mV)')

    # Adjust the layout to prevent titles and labels from overlapping
    plt.tight_layout(pad=3.0)

    # Display the final plot
    plt.show()

if __name__ == '__main__':
    # The name of the CSV file.
    # Make sure this file is in the same directory as the script.
    csv_file = 'sweep_reversal.csv'
    visualize_data(csv_file)
