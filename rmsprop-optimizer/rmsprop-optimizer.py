import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    s = np.asarray(s, dtype = float)
    w = np.asarray(w, dtype = float)
    g = np.asarray(g, dtype = float)
    
    new_s =  beta * s + (1-beta)*g*g
    new_w =  w - (lr / (np.sqrt(new_s + eps)))*g

    return new_w, new_s
    pass