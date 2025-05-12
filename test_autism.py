'''
Current clamp demo using Allen Brain's model 472299294.

To run the demo after importing, call the demo function with a list of currents.
e.g.

    mosinit.demo([270, 170, 110])

The demo also runs if this file is run directly, e.g. via

    python -i mosinit.py
'''

import sys
import argparse
import ast
import numpy as np
from neuron472299294 import Neuron472299294
import matplotlib.pyplot as plt


def arg_as_list(s):                                                            
    v = ast.literal_eval(s)                                                    
    if type(v) is not list:                                                    
        raise argparse.ArgumentTypeError("Argument \"%s\" is not a list" % (s))
    return v

junction_potential = -14.0

def demo(iapp, update_dict={}):
    """demo program performs current clamp experiments"""
    from neuron import h
    h.celsius = 34.0
    cell = Neuron472299294(name='neuron')
    #update values
    cell.update_factors(update_dict)
    
    # clamp
    ic = h.IClamp(0.5, sec=cell.soma[0])
    ic.delay = 200
    ic.dur = 1000
    
    # setup recording
    t = h.Vector()
    t.record(h._ref_t)
    v = h.Vector()
    v.record(cell.soma[0](0.5)._ref_v)
    
    t_vals = []
    v_vals = []
    curr_vals = []
    
    # procedure for doing and plotting each simulation
    def do_current_clamp_experiment(amp):   
        ic.amp = amp / 1000.
        h.finitialize(-90.582359314)
        h.fcurrent()
        h.dt = 0.0125
        h.tstop = 1500
        h.continuerun(h.tstop)
        return t / 1000, v - junction_potential, [ic.delay, ic.dur, h.tstop]

    # run the experiments, store the results
    results = []
    for ii, amp in enumerate(iapp):
        tt, vv, clamp = do_current_clamp_experiment(amp)
        results.append([tt, vv, amp])
    return cell, results, clamp

def make_plots(ax, results):
    for res in results:
        tt, vv, amp = res
        ax.plot(tt, vv, label=str(amp)+' pA')
    ax.set_ylim(-80, 50)
    ax.legend()
    ax.set_xlabel('Time (second)')
    ax.set_ylabel('Membrane potential')
    return ax


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Default conditions of the protocol')
    # clamp
    parser.add_argument('-IC', type=arg_as_list, help = 'list of currents in pA to test', default=[110, 80, 60])
    # passive
    parser.add_argument('-Ra', type=float, help = 'Ra factor', default=1)
    parser.add_argument('-g_pas', type=float, help = 'g_pas factor', default=1)
    parser.add_argument('-cm', type=float, help = 'cm factor', default=1)
    # active Na currensts
    parser.add_argument('-gbar_NaTs', type=float, help = 'gbar_NaTs factor', default=1)
    parser.add_argument('-gbar_Nap', type=float, help = 'gbar NaP factor', default=1)
    # active K currents 
    parser.add_argument('-gbar_K_P', type=float, help = 'gbar_K_P factor', default=1)
    parser.add_argument('-gbar_K_T', type=float, help = 'gbar_K_T factor', default=1)
    parser.add_argument('-gbar_Kv3_1', type=float, help = 'gbar_Kv3_1', default=1)
    parser.add_argument('-gbar_SK', type=float, help = 'gbar_SK', default=1)
    # active Ca
    parser.add_argument('-gbar_Ca_HVA', type=float, help = 'gbar_Ca_HVA', default=1)
    parser.add_argument('-gbar_Ca_LVA', type=float, help = 'gbar_Ca_LVA', default=1)
    # active other
    parser.add_argument('-gbar_Ih', type=float, help = 'gbar_Ih', default=1)
    parser.add_argument('-gbar_Im', type=float, help = 'gbar_Im', default=1)
    args = parser.parse_args()
    all_vals = vars(args)
    iclamps = all_vals.pop('IC')
    print(all_vals)
    cell, results, clamp = demo(iclamps, update_dict=all_vals)
    ax = plt.subplot(111)
    make_plots(ax, results)
    plt.show()
    
