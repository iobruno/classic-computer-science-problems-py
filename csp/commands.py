import click
import matplotlib.pyplot as plt
import networkx as nx

from csp.constraints import ConstraintSatisfactionProblem as CSP
from csp.zookeeper import ZookeeperConstraint
from typing import Dict, Optional


@click.group()
def csp():
    pass


@csp.command("zookeeper")
def zookeeper():
    domain = [1, 2, 3, 4]
    problem = (
        CSP()
        .add_variable(var="Leao", domain=domain)
        .add_variable(var="Antilope", domain=domain)
        .add_variable(var="Hiena", domain=domain)
        .add_variable(var="Tigre", domain=domain)
        .add_variable(var="Pavao", domain=domain)
        .add_variable(var="Suricate", domain=domain)
        .add_variable(var="Javali", domain=domain)
    )

    problem.add_constraint(
        ZookeeperConstraint.Rejects("Leao", "Tigre", reason="Regra #1")
    ).add_constraint(
        ZookeeperConstraint.MustBeTogetherWith("Suricate", "Javali", reason="Regra #2")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Hiena", "Leao", reason="Regra #3")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Hiena", "Antilope", reason="Regra #3")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Hiena", "Pavao", reason="Regra #3")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Hiena", "Suricate", reason="Regra #3")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Hiena", "Javali", reason="Regra #3")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Tigre", "Suricate", reason="Regra #4")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Tigre", "Javali", reason="Regra #4")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Tigre", "Pavao", reason="Regra #4")
    ).add_constraint(
        ZookeeperConstraint.RejectsSameOrAdjacent("Antilope", "Leao", reason="Regra #5")
    ).add_constraint(
        ZookeeperConstraint.RejectsSameOrAdjacent("Antilope", "Tigre", reason="Regra #5")
    ).add_constraint(
        ZookeeperConstraint.Rejects("Pavao", "Leao", reason="Regra #6")
    ).add_constraint(ZookeeperConstraint.MustBeInCageID("Leao", 1, reason="Regra #7"))

    result: Optional[Dict[str, int]] = problem.backtracking_search()

    if result:
        render_layout(result)
    else:
        print("There's no solution for the Problem with the current Constraints")


def render_layout(result):
    g = nx.Graph()
    g.add_edge("Cage 1", "Cage 2")
    g.add_edge("Cage 2", "Cage 3")
    g.add_edge("Cage 3", "Cage 4")
    [g.add_edge(key, f"Cage {value}") for key, value in result.items()]

    position = nx.kamada_kawai_layout(g)
    nx.draw_networkx_nodes(
        g,
        pos=position,
        nodelist=["Cage 1", "Cage 2", "Cage 3", "Cage 4"],
        node_color="#999999",
        node_size=1800,
    )

    nx.draw_networkx_nodes(
        g, pos=position, nodelist=list(result.keys()), node_color="#444444", node_size=1500
    )

    nx.draw_networkx_edges(
        g, pos=position, edgelist=g.edges, width=1, alpha=0.5, edge_color="black"
    )

    nx.draw_networkx_labels(
        g, pos=position, font_size=8, font_family="sans-serif", font_color="white"
    )

    plt.rcParams["figure.figsize"] = [16, 9]
    plt.rcParams["figure.dpi"] = 400
    plt.title("Zookeeper Animal Setup")
    plt.axis("off")
    plt.show()
