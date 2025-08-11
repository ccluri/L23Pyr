import ipywidgets as widgets
import numpy as np
from IPython.display import display, clear_output
from IPython.core.display import display, HTML
display(HTML("<style>div.output_scroll { height: 44em; }</style>"))

output = widgets.Output()

def get_passive_range(cm, g_pas, ra):
    min_cell = [cm[0], g_pas[0], ra[0]]
    max_cell = [cm[1], g_pas[1], ra[1]]
    return min_cell, max_cell

def get_active_range(NaT, Nap, K_P, K_T, Kv_3_1, SK, Ca_HVA, Ca_LVA, Im, Ih):
    min_cell =  [NaT[0], Nap[0], K_P[0], K_T[0], Kv_3_1[0], SK[0], Ca_HVA[0], Ca_LVA[0], Im[0], Ih[0]]
    max_cell =  [NaT[1], Nap[1], K_P[1], K_T[1], Kv_3_1[1], SK[1], Ca_HVA[1], Ca_LVA[1], Im[1], Ih[1]]
    return min_cell, max_cell



style = {'description_width': 'initial'}
# Passive!
pick_cm = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                              description='cm:',
                              disabled=False,
                              continuous_update=False,
                              orientation='horizontal',
                              readout=True,
                              style=style,layout=widgets.Layout(width='400px'))
pick_cm_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=5, step=0.1,
                                         description='cm:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

pick_gpas = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                 description='g_pas:',
                                 disabled=False,
                                 continuous_update=False,
                                 orientation='horizontal',
                                 readout=True,
                                 style=style,
                                 layout=widgets.Layout(width='400px'))
pick_gpas_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                           min=0.1, max=5, step=0.1,
                                           description='g_pas:',
                                           disabled=False,
                                           continuous_update=False,
                                           orientation='horizontal',
                                           readout=True,
                                           readout_format='.1f',
                                           style=style,layout=widgets.Layout(width='400px'))

pick_Ra = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                              description='Ra:',
                              disabled=False,
                              continuous_update=False,
                              orientation='horizontal',
                              readout=True,
                              style=style,
                              layout=widgets.Layout(width='400px'))
pick_Ra_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=5, step=0.1,
                                         description='Ra:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))
# Active Na currents
pick_gbar_NaTs = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                     description='gbar_NaTs:',
                                     disabled=False,
                                     continuous_update=False,
                                     orientation='horizontal',
                                     readout=True,
                                     style=style,
                                     layout=widgets.Layout(width='400px'))
pick_gbar_NaTs_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_NaTs:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

pick_gbar_Nap = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Nap:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Nap_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_Nap:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

# Active K currents
pick_gbar_K_P = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                     description='gbar_K_P:',
                                     disabled=False,
                                     continuous_update=False,
                                     orientation='horizontal',
                                     readout=True,
                                     style=style,
                                     layout=widgets.Layout(width='400px'))
pick_gbar_K_P_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_K_P:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

pick_gbar_K_T = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_K_T:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_K_T_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_K_T:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

pick_gbar_SK = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_SK:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_SK_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_SK:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))


pick_gbar_Kv_3_1 = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Kv3_1:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Kv_3_1_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_Kv_3_1:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

# Active Ca 
pick_gbar_Ca_HVA = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Ca_HVA:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Ca_HVA_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_Ca_HVA:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

pick_gbar_Ca_LVA = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Ca_LVA:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Ca_LVA_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_Ca_LVA:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

# Active Other
pick_gbar_Im = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Im:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Im_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_Im:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))

pick_gbar_Ih = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Ih:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Ih_range = widgets.FloatRangeSlider(value=[0.5, 1.5],
                                         min=0.1, max=4, step=0.1,
                                         description='gbar_Ih:',
                                         disabled=False,
                                         continuous_update=False,
                                         orientation='horizontal',
                                         readout=True,
                                         readout_format='.1f',
                                         style=style,layout=widgets.Layout(width='400px'))




