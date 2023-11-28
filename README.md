# Classic Computer Science Problems in Python

![Python](https://img.shields.io/badge/Python-3.9%20|%203.10%20|%203.11-3776AB.svg?style=flat&logo=python&logoColor=white)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

This project is a collection my resolutions for the various exercises from the book 
`Classic Computer Science Problems in Python`, plus some more AI assessments from the Academia


## Tech Stack
- pandas, numpy
- [Click](https://click.palletsprojects.com/en/latest/) 
- [Rich CLI](https://github.com/Textualize/rich)
- [PDM](https://pdm-project.org/latest/#installation)
- [Ruff](https://github.com/astral-sh/ruff)


## Up & Running

Pretty much all use-cases here are coded on **Jupyter Notebooks**, so make sure to:

**Create a virtualenv for Python 3.9 / 3.10 / 3.11**
```shell
conda create -n classic-cs-problems-py python=3.11
conda activate classic-cs-problems-py
```

**Install project dependencies**
```shell
pdm sync
```

### Running locally:
 
**Minimax: Chess**
```shell
python run.py minimax chess
```

**Genetic Algorithm: Multi-Vehicle Routing Problem (mVRP)**
```shell
python run.py ga mvrp
```

**Constraint Satisfaction Problems (CSP) - Zookeeper**
```shell
python run.py csp zookeeper
```


## Chapters:

<<<<<<< HEAD
**Recommended**
```
$ make install
$ cs minimax chess
```

### **Constraint Satisfaction Problems (CSP) - Zookeeper**
```
$ make install
$ cs csp zookeeper
```

> For a list of commands available or simply run (currently the only app that is implemented outside of a jupyter notebook)
```
$ cs --help
``` 

## TO-DO List:

### Chapters
=======
>>>>>>> b3f0fd1 (Feat/project structure update (#2))
Ch.3 - Constraint Satisfaction Problems (CSP) 
- [x] The Australian map-coloring problem
- [x] EXTRA: The Zookeeper problem

<<<<<<< HEAD
### Project Setup and Pipelines
=======
Ch.8 - Adversarial Search
- [ ] Tic-Tac-Toe
- [ ] EXTRA: Chess


## TODO
>>>>>>> b3f0fd1 (Feat/project structure update (#2))
- [x] Refactor the CLI apps with click
- [x] PEP-517: Packaging and dependency management with PDM
- [x] Code formatting with Ruff
- [ ] Implement visualization with Streamlit