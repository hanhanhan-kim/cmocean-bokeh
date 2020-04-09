#!/usr/bin/env python3

"""
Utility functions for using cmocean's colourmaps in bokeh. 
cmocean's colourmaps are stored as matplotlib.colors.LinearSegementedColormap
objects. I convert each colour map into a list of hexadecimals for use in bokeh.
"""

import cmocean
from pylab import *

def cmap2hexlist(cmap):
    
    """
    Converts a matplotlib.colors.LinearSegementedColormap object to 
    a list of hex colours. Useful for converting attribute colour maps 
    of cmocean.cm for use with bokeh. 
    
    Parameters:
    -----------
    cmap: a matplotlib.colors.LinearSegmentedColormap object. 
        Attributes of cmocean.cm are these objects and are colour maps. 
        E.g. cmocean.cm.haline
        
    Returns:
    --------
    A list of hexadecimal colour codes. 
    """
    
    hexcolours = []
    for i in range(cmap.N):
        # Returns rgba; take only first 3 to get rgb:
        rgb = cmap(i)[:3] 
        hexcolours.append(matplotlib.colors.rgb2hex(rgb))
    
    return hexcolours


def get_all_cmocean_colours():
    
    """
    Returns a dictionary of the cmocean colour maps.
    Each key in the dictionary is the name of the colourmap and each value 
    in the dictionary is a list of the colourmap's colours in hexadecimal. 
    """
    
    cmocean_attrs = dir(cmocean.cm)

    hexcolourmaps_dict = {}
    for i, cmocean_attr in enumerate(cmocean_attrs):

        attr_instance = getattr(cmocean.cm, cmocean_attrs[i])
        attr_type = type(attr_instance)

        if attr_type is matplotlib.colors.LinearSegmentedColormap:
            
            # Convert val to hexlist and add key-val pair:
            hexcolourmaps_dict[cmocean_attr] = cmap2hexlist(attr_instance)
    
    return hexcolourmaps_dict