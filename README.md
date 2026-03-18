# A Machine Learning Based Explainability Framework for Interpreting Swarm Intelligence

## 🔑 Highlights

- 🚀 Proposes an interpretability framework for Particle Swarm Optimization (PSO)
- 📊 Uses Exploratory Landscape Analysis (ELA) to characterize problem difficulty
- 🔍 Identifies key landscape features affecting PSO performance
- ⚙️ Develops an explainable benchmarking framework
- 🌐 Analyzes the impact of swarm topologies on information flow, diversity, and convergence
- 🧪 Evaluated on 24 benchmark functions across multiple dimensions
- 📈 Provides practical guidelines for topology selection and parameter tuning
- 🌳 Introduces a decision tree-based approach to explain PSO behavior
- 🧠 Reduces the black-box nature of PSO
- ✨ Enhances transparency and explainability in swarm intelligence systems

# Getting Started
This repository includes all the results of the PSO using three topologies: Star, Ring, and VonNeumann, with a dimensionality of 2 and 5. The experimental settings consisted of two computing platforms: 2d evaluations were performed on an Intel i7 system with 32GB RAM and 8 processing cores, while 5d experiments utilized a more powerful Intel Xeon W-1270P workstation with 96GB RAM and 8 cores to accommodate the increased computational demands of higher-dimensional optimization. The VonNeumann topology took the least time, followed by the Star topology, and the Ring topology took the longest.


This project uses Python 3.11 and requires the libraries listed in the [`requirement.txt`](./requirement.txt) file. The configuration space for the experiment is defined in the [`sample_config.py`](./sample_config.py) file.

The supplementary file contains graph plots for all three topologies — Star, Ring, and Von Neumann.  [`Supplementary.pdf`](./Supplementary.pdf)



