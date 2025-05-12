'''
Current clamp demo using Allen Brain's model 472299294.

To run the demo after importing, call the demo function with a list of currents.
e.g.

    mosinit.demo([270, 170, 110])

The demo also runs if this file is run directly, e.g. via

    python -i mosinit.py
'''

from neuron472299294 import Neuron472299294

junction_potential = -14.0

def demo(iapp):
    """demo program performs current clamp experiments"""
    from neuron import h, gui
    h.celsius = 34.0
    cell = Neuron472299294(name='neuron')
    ic = h.IClamp(0.5, sec=cell.soma[0])
    ic.delay = 200
    ic.dur = 1000
    
    # setup recording
    t = h.Vector()
    t.record(h._ref_t)
    v = h.Vector()
    v.record(cell.soma[0](0.5)._ref_v)
    
    # setup plotting
    vbox = h.VBox()
    vbox.intercept(1)
    g = h.Graph()
    g.size(0, 1.5, -100, 50)
    # smaller current graph
    adj = vbox.adjuster(100)
    current = h.Graph()
    current.size(0, 1.5, 0, 300)
    vbox.intercept(0)
    vbox.map('Allen Institute model 472299294; v includes junction potential', 10, 10, 600, 400)

    # procedure for doing and plotting each simulation
    def do_current_clamp_experiment(amp, color):   
        ic.amp = amp / 1000.
        
        h.finitialize(-90.582359314)
        h.fcurrent()

        h.dt = 0.0125
        h.tstop = 1500
        h.continuerun(h.tstop)
        brush = 2                            # 2px line
        
        # plot the voltage (after including junction potential effects)
        g.beginline('%g pA' % amp, color, brush)
        for x, y in zip(t, v):
            g.line(x / 1000., y - junction_potential)
        g.flush()
        
        # plot the current
        current.beginline('%g pA' % amp, color, brush)
        t1 = ic.delay                        # pulse begins
        t2 = ic.delay + ic.dur               # pulse ends
        for x, y in zip([0, t1, t1, t2, t2, h.tstop], [0, 0, amp, amp, 0, 0]):
            current.line(x / 1000., y)
        current.flush()
        return list(t), [mv - junction_potential for mv in v]

    # run the experiments, store the results
    results = []
    for color, amp in enumerate(iapp):
        results.append(do_current_clamp_experiment(amp, color + 1))
    
    return cell, vbox, results

if __name__ == '__main__':
    results = demo([110, 80, 60])
