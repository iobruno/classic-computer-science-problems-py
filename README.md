# Classic Computer Science Problems in Python

This project is a collection my resolutions for the various exercises from the book 
`Classic Computer Science Problems in Python`, plus some more AI assessments from the Academia

## Tech Stack
- Python 3.9+
- Pytest
- [Poetry](https://python-poetry.org/docs/)  (packaging and dependecy management)
- Conda (virtual env)

## Up & Running

Pretty much all use-cases/problems here are coded on **Jupyter Notebooks**, so make sure to:
- **Create a virtualenv for Python 3.9**
- **Install poetry**, and then:

## Build and Run locally:

### **Genetic Algorithm: Multi-Vehicle Routing Problem (mVRP)**
 
**Local run (Without Poetry)**
```
$ pip install -r requirements.txt
$ python run.py ga mvrp
```

**Recommended (Poetry required)**
``` 
$ make install
$ cs ga mvrp
```


### **Minimax: Chess**

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
Ch.3 - Constraint Satisfaction Problems (CSP) 
- [x] The Australian map-coloring problem
- [x] EXTRA: The Zookeeper problem

### Project Setup and Pipelines
- [x] Refactor the CLI apps with click
- [ ] Set up a template for code formatting (yapf)
- [x] PEP-517: Packaging and dependency management with Poetry
- [ ] Implement a CI pipeline with GitHub Actions
