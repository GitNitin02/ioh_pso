import numpy as np
import pandas as pd
import pyswarms as ps
from pyswarms.backend.topology import VonNeumann, Ring, Star
from ConfigSpace import ConfigurationSpace
from iohxplainer import explainer
import traceback
import time  # Import the time module
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display


# Define the configuration space for PSO
confSpace = ConfigurationSpace(
    {
        "c1": [0.3,0.5,0.7,0.9],  # Cognitive coefficient
        "c2": [0.2,0.4,0.6,0.7],  # Social coefficient
        "w": [0.9,1.2, 0.4],   # Inertia weight
        "n_particles": [50,100,150],
        'k': [1,2,3],
        'p':[1,2],
        'r':[1,2], 
          
         
    }
)
my_topology = Star()       #Use another Topology for another module
features = ["c1", "c2", "w", "n_particles","k", "p", "r"  ]


# Define the PSO run function for paricular Topology such as Star, Ring and Von Neumann
def run_pso(func, config, budget, dim, *args, **kwargs):
    # Setting bounds for the optimization (here as an example: -5 to 5 for each dimension)
    bounds = (-5 * np.ones(dim), 5 * np.ones(dim))

    c1 = config.get("c1")
    c2 = config.get("c2")
    k = config.get("k")
    p = config.get("p")
    r = config.get("r")
    w = config.get("w")
    n_particles = config.get("n_particles")
    
    # Define the options for PSO based on the configuration
    options = {
        'c1': c1,
        'c2': c2,
        'w': w,
        'p':p,
        'k':k,
        'r':r
    }

    # Create the PSO optimizer
    optimizer = ps.single.GeneralOptimizerPSO(
        n_particles=config.get("n_particles"),
        dimensions=dim,
        options=options,
        bounds=bounds,
        topology=my_topology

    )

    # Perform the optimization
    cost, pos = optimizer.optimize(func, iters=budget)
    return cost, pos  # Return the best cost and position found



'''We also use topology as module on configuration '''

confSpace = ConfigurationSpace(
    {
        "c1": [0.3,0.5,0.7,0.9],  # Cognitive coefficient
        "c2": [0.2,0.4,0.6,0.7],  # Social coefficient
        "w": [0.9,1.2, 1.4],   # Inertia weight
        "n_particles": [50,100,150],
        'k': [1,2,3],
        'p':[1,2],
        'r':[0,1], 
        "my_topology" : ["VonNeumann", "Ring", "Star"]   
         
    }
)

features = ["c1", "c2", "w", "n_particles","k", "p", "r", "my_topology"  ]


def run_pso(func, config, budget, dim, *args, **kwargs):
    
    bounds = (-5 * np.ones(dim), 5 * np.ones(dim))

    # Extract the PSO parameters from the configuration
    topology_name = config.get("my_topology")
    c1 = config.get("c1")
    c2 = config.get("c2")
    k = config.get("k")
    p = config.get("p")
    r = config.get("r")
    w = config.get("w")
    n_particles = config.get("n_particles")
    my_topology = config.get("my_topology")

    # Map string to actual topology object
    if my_topology == "VonNeumann":
        topology = VonNeumann()
    elif my_topology == "Ring":
        topology = Ring()
    elif my_topology == "Star":
        topology = Star()
    else:
        raise ValueError("Invalid topology specified")
