# Classic Computer Science Problems in Python

![Python](https://img.shields.io/badge/Python-3.13_|_3.12_|_3.11_|_3.10-4B8BBE.svg?style=flat&logo=python&logoColor=FFD43B&labelColor=306998)
![Pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=E70488&labelColor=150458)
![Jupyter](https://img.shields.io/badge/Jupyter-262A38.svg?style=flat&logo=jupyter&logoColor=F37726&labelColor=262A38)

![License](https://img.shields.io/badge/license-CC--BY--SA--4.0-31393F?style=flat&logo=creativecommons&logoColor=black&labelColor=white)

This project is a collection of various exercises from the book `Classic Computer Science Problems in Python`, plus some more AI assessments from Academia

## Tech Stack
- [Typer](https://typer.tiangolo.com/tutorial/)
- [pandas](https://pandas.pydata.org/docs/user_guide/)
- [uv](https://docs.astral.sh/uv/concepts/projects/dependencies/)

## Up and Running

### Developer Setup

**1.** Install the dependencies on `pyproject.toml`:
```shell
uv sync
```

**2.** Activate the virtualenv created by `uv`:
```shell
source .venv/bin/activate
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

## TODO
- [x] PEP-517: Packaging and dependency management with `uv`
- [x] Build a CLI app with `Typer` (`cspy`)
- [ ] Implement visualization with Streamlit
- [x] Code format/lint with Ruff
