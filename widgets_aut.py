import ipywidgets as widgets
import numpy as np
from IPython.display import display, clear_output
from IPython.core.display import display, HTML
display(HTML("<style>div.output_scroll { height: 44em; }</style>"))

output = widgets.Output()

style = {'description_width': 'initial'}
# Passive!
pick_cm = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                              description='cm:',
                              disabled=False,
                              continuous_update=False,
                              orientation='horizontal',
                              readout=True,
                              style=style,layout=widgets.Layout(width='400px'))
pick_gpas = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                 description='g_pas:',
                                 disabled=False,
                                 continuous_update=False,
                                 orientation='horizontal',
                                 readout=True,
                                 style=style,
                                 layout=widgets.Layout(width='400px'))
pick_Ra = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                              description='Ra:',
                              disabled=False,
                              continuous_update=False,
                              orientation='horizontal',
                              readout=True,
                              style=style,
                              layout=widgets.Layout(width='400px'))


# Active Na currents
pick_gbar_NaTs = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                     description='gbar_NaTs:',
                                     disabled=False,
                                     continuous_update=False,
                                     orientation='horizontal',
                                     readout=True,
                                     style=style,
                                     layout=widgets.Layout(width='400px'))
pick_gbar_Nap = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Nap:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
# Active K currents
pick_gbar_K_P = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                     description='gbar_K_P:',
                                     disabled=False,
                                     continuous_update=False,
                                     orientation='horizontal',
                                     readout=True,
                                     style=style,
                                     layout=widgets.Layout(width='400px'))
pick_gbar_K_T = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_K_T:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_SK = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_SK:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Kv_3_1 = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Kv3_1:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
# Active Ca 
pick_gbar_Ca_HVA = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Ca_HVA:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Ca_LVA = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Ca_LVA:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
# Active Other
pick_gbar_Im = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Im:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))
pick_gbar_Ih = widgets.FloatSlider(value=1, min=0.1, max=2, step=0.1,
                                    description='gbar_Ih:',
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    style=style,
                                    layout=widgets.Layout(width='400px'))






