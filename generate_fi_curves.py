import matplotlib.pyplot as plt
import test_autism5 as utils


def format_passive_props(R_input, tau_mem, RMP):
    passive_props = ['Rin', 'tau', 'RMP']
    passive_props_vals = [R_input*1000, tau_mem, RMP]
    passive_props_units = ['(Mohms)', '(ms)', '(mV)']
    passive_props_str = ', '.join([ii + ' : '+str(int(jj))+kk for ii, jj, kk in zip(passive_props,
                                                                               passive_props_vals,
                                                                               passive_props_units)])
    return passive_props_str

def fi_save_svg(filename, conductance_vals):
    model_test_currs = [-15, -10, 0, 10, 15, 20, 25, 30, 35]
    cell, results, clp = utils.demo(model_test_currs, conductance_vals)
    R_input, tau_mem, RMP = utils.comp_passive_props(results)
    passive_props_str = format_passive_props(R_input, tau_mem, RMP)
    ax = plt.subplot()
    ax = utils.show_ficurve(ax, results, color='b', label='Simulation', ls='dashed', marker='P')
    ax.set_ylim(-1, 20)
    ax.set_xlim(0, 50)
    ax.set_xlabel('Current clamp (pA)')
    ax.set_ylabel('Firing freq (Hz)')
    ax.set_title(filename + ', ' +  passive_props_str)
    plt.legend()
    plt.savefig(filename + '.svg', dpi=300)
    print('Done for : ', filename)
    plt.close()

def response_save_svg(filename, conductance_vals):
    model_test_currs = [0, 10, 20, 30]
    cell, results, clp = utils.demo(model_test_currs, conductance_vals)
    # R_input, tau_mem, RMP = utils.comp_passive_props(results)
    # passive_props_str = format_passive_props(R_input, tau_mem, RMP)
    ax = plt.subplot() 
    ax = utils.make_plots(ax, results, all_plots=True)
    plt.savefig(filename + '_response.svg', dpi=300)
    plt.close()
    
if __name__ == '__main__':
    # defaults for WT
    filename = 'WT'
    conductance_vals =  {'gbar_NaTs': 1, 
                         'gbar_Nap': 1, 
                         'gbar_K_P': 1,
                         'gbar_K_T': 1,
                         'gbar_Kv_3_1': 1,
                         'gbar_SK': 1,
                         'gbar_Ca_HVA': 1,
                         'gbar_Ca_LVA': 1,
                         'gbar_Ih': 1,
                         'gbar_Im': 1}
    fi_save_svg(filename, conductance_vals)
    response_save_svg(filename, conductance_vals)
    
    # filename = 'HnrnpU_low'
    # conductance_vals =  {'gbar_NaTs': 0.4, 
    #                      'gbar_Nap': 1, 
    #                      'gbar_K_P': 0.7,
    #                      'gbar_K_T': 1,
    #                      'gbar_Kv_3_1': 1,
    #                      'gbar_SK': 1,
    #                      'gbar_Ca_HVA': 0.3,
    #                      'gbar_Ca_LVA': 1,
    #                      'gbar_Ih': 1,
    #                      'gbar_Im': 0.6}
    # fi_save_svg(filename, conductance_vals)

    # filename = 'HnrnpU_upp'
    # conductance_vals =  {'gbar_NaTs': 0.8, 
    #                      'gbar_Nap': 1, 
    #                      'gbar_K_P': 1,
    #                      'gbar_K_T': 1,
    #                      'gbar_Kv_3_1': 1,
    #                      'gbar_SK': 1,
    #                      'gbar_Ca_HVA': 0.8,
    #                      'gbar_Ca_LVA': 1,
    #                      'gbar_Ih': 1,
    #                      'gbar_Im': 1}
    # fi_save_svg(filename, conductance_vals)

    # filename = 'Bckdk_low'
    # conductance_vals =  {'gbar_NaTs': 0.8, 
    #                      'gbar_Nap': 1, 
    #                      'gbar_K_P': 0.6,
    #                      'gbar_K_T': 1,
    #                      'gbar_Kv_3_1': 0.7,
    #                      'gbar_SK': 1,
    #                      'gbar_Ca_HVA': 0.8,
    #                      'gbar_Ca_LVA': 1,
    #                      'gbar_Ih': 1,
    #                      'gbar_Im': 1}
    # fi_save_svg(filename, conductance_vals)

    # filename = 'Bckdk_upp'
    # conductance_vals =  {'gbar_NaTs': 0.9, 
    #                      'gbar_Nap': 1, 
    #                      'gbar_K_P': 0.9,
    #                      'gbar_K_T': 1,
    #                      'gbar_Kv_3_1': 0.9,
    #                      'gbar_SK': 1,
    #                      'gbar_Ca_HVA': 0.9,
    #                      'gbar_Ca_LVA': 0.9,
    #                      'gbar_Ih': 2,
    #                      'gbar_Im': 1}
    # fi_save_svg(filename, conductance_vals)
