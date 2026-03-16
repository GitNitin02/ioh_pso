# A Machine Learning Based Explainability Framework for Interpreting Swarm Intelligence

# Summary
Swarm based optimization algorithms have demonstrated remarkable success in solving complex optimization
problems. However, their widespread adoption remains sceptical due to limited transparency in how different
algorithmic components influence the overall performance of the algorithm. This work presents a multi-
faceted interpretability related investigations of Particle Swarm Optimization (PSO). Through this work,
we provide a framework that makes the PSO interpretable and explainable using novel machine learning
approach. We first developed a comprehensive landscape characterization framework using Exploratory
Landscape Analysis to quantify problem difficulty and identify critical features in the problem that affects the
optimization performance of PSO. Secondly, we develop an explainable benchmarking framework for PSO.
The work successfully decodes how swarm topologies affect information flow, diversity, and convergence.
Through systematic experimentation across 24 benchmark functions in multiple dimensions, we establish
practical guidelines for topology selection and parameter configuration. A systematic design of decision tree
is developed to identify the decision making inside PSO. These findings uncover the black-box nature of PSO,
providing more transparency and interpretability to swarm intelligence systems. 

# Getting Started
This repository includes all the results of the PSO using three topologies: Star, Ring, and VonNeumann, with a dimensionality of 2 and 5. The experimental settings consisted of two computing platforms: 2d evaluations were performed on an Intel i7 system with 32GB RAM and 8 processing cores, while 5d experiments utilized a more powerful Intel Xeon W-1270P workstation with 96GB RAM and 8 cores to accommodate the increased computational demands of higher-dimensional optimization. The VonNeumann topology took the least time, followed by the Star topology, and the Ring topology took the longest.


This project uses Python 3.11 and requires the libraries listed in the [`requirement.txt`](./requirement.txt) file. The configuration space for the experiment is defined in the [`sample_config.py`](./sample_config.py) file.

The supplementary file contains graph plots for all three topologies — Star, Ring, and Von Neumann.  [`Supplementary.pdf`](./Supplementary.pdf)



