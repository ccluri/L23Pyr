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
from scipy.optimize import curve_fit
from threshold_crossing import count_spikes
from neuron472299294_250812 import Neuron472299294
import matplotlib.pyplot as plt


def arg_as_list(s):                                                            
    v = ast.literal_eval(s)                                                    
    if type(v) is not list:                                                    
        raise argparse.ArgumentTypeError("Argument \"%s\" is not a list" % (s))
    return v

ichs = [u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P',
        u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK', u'pas']
ichs_k = ['K_P', 'K_T', 'Kv3_1', 'SK', 'Im']
ichs_na = ['NaTs', 'Nap']
ichs_ca = ['Ca_HVA', 'Ca_LVA']
ichs_ih = ['Ih']
ichs_pas = ['pas']

junction_potential = -14.0

def demo(iapp, update_dict={}, all_rev=False):
    """demo program performs current clamp experiments"""
    from neuron import h
    h.initnrn()
    h.celsius = 34.0
    cell = Neuron472299294(name='neuron', shrink_by=0.7)
    #update values
    cell.update_factors(update_dict, all_rev=all_rev)
    
    # clamp
    ic = h.IClamp(0.5, sec=cell.soma[0])
    ic.delay = 200
    ic.dur = 1000
    
    # setup recording
    t = h.Vector()
    t.record(h._ref_t)
    v = h.Vector()
    v.record(cell.soma[0](0.5)._ref_v)

    ich_currs = {}
    for ich in ichs:
        ich_currs[ich] = h.Vector()
        if ich in ichs_k:
            curr_str = 'ik'
        elif ich in ichs_na:
            curr_str = 'ina'
        elif ich in ichs_ca:
            curr_str = 'ica'
        elif ich in ichs_ih:
            curr_str = 'ihcn'
        else: # passive
            curr_str = 'i'
        ich_currs[ich].record(eval('cell.soma[0](0.5).' + ich
                                   + '._ref_' + curr_str))
    
    # procedure for doing and plotting each simulation
    def do_current_clamp_experiment(amp):   
        ic.amp = amp / 1000.
        h.finitialize(-80.582359314)
        h.fcurrent()
        h.dt = 0.0125
        h.tstop = 1500
        h.continuerun(h.tstop)
        return t / 1000, v - junction_potential, ich_currs, [ic.delay, ic.dur, h.tstop]

    # run the experiments, store the results
    results = []
    for ii, amp in enumerate(iapp):
        tt, vv, ich_currs, clamp = do_current_clamp_experiment(amp)
        results.append([tt, vv, ich_currs, amp])
    return cell, results, clamp

def comp_passive_props(results, ax=None):
    # xx, yy, tt, y_tau = comp_passive_props(results)
    xx = []
    yy = []
    y_tau = []
    for res in results[:3]:
        tt, vv, ich, amp = res
        xx.append(amp)
        t_arr = np.array(tt)
        v_arr = np.array(vv)
        yy.append(np.mean(v_arr[(t_arr>1) & (t_arr<1.2)]))
        y_tau.append(v_arr[(t_arr>0.2) & (t_arr<=0.3)])

    tt_ref = t_arr[(t_arr>0.2) & (t_arr<=0.3)]
    popt, pcov = curve_fit(exp_fit, tt_ref-0.2, y_tau[1])
    coef = np.polyfit(xx, yy, 1)
    poly1d_fn = np.poly1d(coef)
    print('Rin, tau', coef[0], popt[1])
    print('RMP (mV)', np.mean(np.array(results[2][1])))
    if ax:
        ax.plot(tt_ref, y_tau[1])
        ax.plot(tt_ref, exp_fit(tt_ref-0.2, *popt), 'g--')
    return coef[0], popt[1], np.mean(np.array(results[2][1]))


def exp_fit(x, a, b, c):
    return a*np.exp(-b*x) + c


def make_curr_plots(ax, results, curr='all'):
    for res in results[-1:]:
        tt, vv, ich, amp = res
        if curr == 'all':
            for ic in ichs: 
                ax.plot(tt, ich[ic], label=ic)
        elif curr == 'nak':
            for ic in ichs_na + ichs_k + ichs_pas:
                ax.plot(tt, ich[ic], label=ic)
        elif curr == 'ca':
            for ic in ichs_ca: 
                ax.plot(tt, ich[ic], label=ic)
                    
    #ax.set_ylim(-80, 50)
    ax.legend(frameon=False, ncols=5)
    ax.set_xlabel('Time (second)')
    ax.set_ylabel('Current')
    ax.set_xlim(0.1, 1.3)
    return ax


def show_ficurve(ax, results, defs=None, defs_ff=None, color='k', label='Simulation', label_add='', ls='dashed', marker='P'):
    ffs = []
    cur_vals = []
    for res in results:
        tt, vv, ichs, amp = res
        cur_vals.append(amp)
        ffs.append(count_spikes(np.array(vv)))
    if defs:
        ax.plot(defs, defs_ff, label='Recording', c='k',
                marker='o')
    ax.plot(cur_vals, ffs, label=label+label_add, c=color,
            linestyle=ls, marker=marker)
    ax.set_ylim(-1, 20)
    ax.set_xlim(0, 50)
    #print('Current clamps: ', cur_vals)
    #print('Firing freq:', ffs)
    return ax

def show_ficurve_special(ax, color='g', label='hnrnpu'):
    if label == 'hnrnpu':
        hnrnpu = [0,0,0.25,1.83333333333333,3.91666666666667,6.25,9.33333333333333,11.9166666666667] #,13.5, 14.4166666666667, 15.3333333333333]
        currs_hnrnpu = [0,5,10,15,20,25,30,35] # ,40,45,50]
        ax.plot(currs_hnrnpu, hnrnpu, c=color, label=label)
    elif label == 'bckdk':
        bckdk = [0, 0.0714285714285714, 2.78571428571429 ,7
                 ,10.2142857142857 ,12.1428571428571 ,12.2142857142857, 12.5,] 
                 #,11.5 ,10.7142857142857 ,8.07142857142857]
        currs_bckdk = [0,5,10,15,20,25,30,35] # ,40,45,50]
        ax.plot(currs_bckdk, bckdk, c=color, label=label)
    elif label == 'trip12':
        trip12 = [0,0.3, 1.5, 3.7, 6.25, 9.1, 10.8, 11.85] #,
                  #12.2, 12.15, 11.8]
        currs_trip12 = [0,5,10,15,20,25,30,35] # ,40,45,50]
        ax.plot(currs_trip12, trip12, c=color, label=label)
    elif label == 'usp7':
        usp7 = [0, 0.166666666666667, 1.27777777777778,
                4.16666666666667, 7.72222222222222, 10.3333333333333,
                12.2222222222222, 13.8888888888889] # , 
                # 15.2777777777778, 15.8333333333333, 16.6666666666667,]
        currs_usp7 = [0,5,10,15,20,25,30,35] # ,40,45,50]
        ax.plot(currs_usp7, usp7, c=color, label=label)
    elif label == 'wt':
        wt_rec = [0, 0, 1, 4, 7, 9, 11, 12]
        curr_wt = [0, 5, 10, 15, 20, 25, 30, 35]
        ax.plot(curr_wt, wt_rec, c=color, label=label)
    else:
        pass
    return ax


def make_plots(ax, results, all_plots=False):
    if all_plots:
        new_results = results
    else:
        new_results = results[3:]
    for res in new_results:
        tt, vv, ichs, amp = res
        ax.plot(tt, vv, label=str(amp)+' pA')
    ax.set_ylim(-80, 50)
    ax.legend()
    ax.set_xlabel('Time (second)')
    ax.set_ylabel('Membrane potential (mV)')
    return ax




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Default conditions of the protocol')
    # clamp
    parser.add_argument('-IC', type=arg_as_list, help = 'list of currents in pA to test', default=[])
    # reversal potential e_pas=-90.582359314, ena=53.0, ek=-107.0
    parser.add_argument('-e_pas', type=float, help = 'Rev. Pot E passive', default=-75)
    parser.add_argument('-ena', type=float, help = 'Rev. Pot Na', default=30)
    parser.add_argument('-ek', type=float, help = 'Rev. Pot K', default=-110.0)
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
    print(all_vals)
    iclamps = all_vals.pop('IC')
    iclamps_rev = [-15, -10, 0]
    iclamps = iclamps_rev + iclamps   # add for computing inp resistance
    cell, results, clamp = demo(iclamps, update_dict=all_vals, all_rev=True)

    fig = plt.figure(figsize=(40, 20))
    ax1 = plt.subplot(231)
    make_plots(ax1, results, all_plots=False)

    ax2 = plt.subplot(232)
    R_input, tau_mem, RMP = comp_passive_props(results, ax2)

    ax3 = plt.subplot(233)
    #ax3.plot(xx, yy, 'yo', xx, poly1d_fn(xx), '--k')
    #ax3 = show_ficurve(ax3, results[3:])
    # model_test_currs = [10, 15, 20, 25]
    cur_vals = [0, 5, 10, 15, 20, 25, 30, 35]                                                                                                                                           
    ffs = [0, 0, 1, 4, 7, 9, 11, 12]
    
    ax3 = show_ficurve(ax3, results, defs=cur_vals, defs_ff=ffs)
    
    ax4 = plt.subplot(234)
    make_curr_plots(ax4, results)

    ax5 = plt.subplot(235)
    make_curr_plots(ax5, results, curr='nak')

    ax6 = plt.subplot(236)
    make_curr_plots(ax6, results, curr='ca')
    #plt.get_current_fig_manager().full_screen_toggle()
    plt.show()
    
