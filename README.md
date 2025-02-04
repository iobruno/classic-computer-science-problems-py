# Classic Computer Science Problems in Python

![Python](https://img.shields.io/badge/Python-3.13_|_3.12-4B8BBE.svg?style=flat&logo=python&logoColor=FFD43B&labelColor=306998)
[![Typer](https://img.shields.io/badge/Typer-262A38?style=flat&logo=typer&logoColor=FFFFFF&labelColor=262A38)](https://typer.tiangolo.com/tutorial/)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=E70488&labelColor=150458)](https://pandas.pydata.org/docs/user_guide/)
[![Jupyter](https://img.shields.io/badge/Jupyter-262A38?style=flat&logo=jupyter&logoColor=FF6849&labelColor=262A38)](https://docs.jupyter.org/en/stable/projects/kernels.html)
[![uv](https://img.shields.io/badge/astral/uv-261230?style=flat&logo=uv&logoColor=DE5FE9&labelColor=261230)](https://docs.astral.sh/uv/getting-started/installation/)


![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-31393F?style=flat&logo=creativecommons&logoColor=black&labelColor=white)

This project is a collection of various exercises from the book `Classic Computer Science Problems in Python`, plus some more AI assessments from Academia


## Getting Started

Install dependencies from pyproject.toml and activate the created virtualenv:
```shell
uv sync && source .venv/bin/activate
```
 
Genetic Algorithm: Multi-Vehicle Routing Problem (mVRP)
```shell
cspy ga mvrp
```

Constraint Satisfaction Problems (CSP) - Zookeeper
```shell
cspy csp zookeeper
```

## Chapters
Ch.3 - Constraint Satisfaction Problems (CSP) 
- [x] The Australian map-coloring problem
- [x] EXTRA: The Zookeeper problem

Ch.8 - Adversarial Search
- [ ] Tic-Tac-Toe
- [ ] EXTRA: Chess

## TODO's:
- [x] PEP-517: Packaging and dependency management with `uv`
- [x] Build a CLI app with `Typer` (`cspy`)
- [ ] Implement visualization with Streamlit
- [x] Code format/lint with Ruff
