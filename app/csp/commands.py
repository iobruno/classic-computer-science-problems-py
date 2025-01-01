import click
import matplotlib.pyplot as plt
import networkx as nx

from app.csp.constraints import ConstraintSatisfactionProblem as CSP
from app.csp.zookeeper import ZookeeperConstraint as Constraint


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
    (
        problem.add_constraint(Constraint.Rejects("Leao", "Tigre", reason="Regra #1"))
        .add_constraint(Constraint.MustBeTogetherWith("Suricate", "Javali", reason="Regra #2"))
        .add_constraint(Constraint.Rejects("Hiena", "Leao", reason="Regra #3"))
        .add_constraint(Constraint.Rejects("Hiena", "Antilope", reason="Regra #3"))
        .add_constraint(Constraint.Rejects("Hiena", "Pavao", reason="Regra #3"))
        .add_constraint(Constraint.Rejects("Hiena", "Suricate", reason="Regra #3"))
        .add_constraint(Constraint.Rejects("Hiena", "Javali", reason="Regra #3"))
        .add_constraint(Constraint.Rejects("Tigre", "Suricate", reason="Regra #4"))
        .add_constraint(Constraint.Rejects("Tigre", "Javali", reason="Regra #4"))
        .add_constraint(Constraint.Rejects("Tigre", "Pavao", reason="Regra #4"))
        .add_constraint(Constraint.RejectsSameOrAdjacent("Antilope", "Leao", reason="Regra #5"))
        .add_constraint(Constraint.RejectsSameOrAdjacent("Antilope", "Tigre", reason="Regra #5"))
        .add_constraint(Constraint.Rejects("Pavao", "Leao", reason="Regra #6"))
        .add_constraint(Constraint.MustBeInCageID("Leao", 1, reason="Regra #7"))
    )

    result = problem.backtracking_search()

    if result:
        render_layout(result)
    else:
        print("There's no solution for the Problem with the current Constraints")


def render_layout(result):
    graph = nx.Graph()
    graph.add_edge("Cage 1", "Cage 2")
    graph.add_edge("Cage 2", "Cage 3")
    graph.add_edge("Cage 3", "Cage 4")
    [graph.add_edge(key, f"Cage {value}") for key, value in result.items()]

    position = nx.kamada_kawai_layout(graph)
    nx.draw_networkx_nodes(
        graph,
        pos=position,
        nodelist=["Cage 1", "Cage 2", "Cage 3", "Cage 4"],
        node_color="#999999",
        node_size=1800,
    )

    nx.draw_networkx_nodes(
        graph,
        pos=position,
        nodelist=list(result.keys()),
        node_color="#444444",
        node_size=1500,
    )

    nx.draw_networkx_edges(
        graph,
        pos=position,
        edgelist=graph.edges,
        width=1,
        alpha=0.5,
        edge_color="black",
    )

    nx.draw_networkx_labels(
        graph,
        pos=position,
        font_size=8,
        font_family="sans-serif",
        font_color="white",
    )

    plt.rcParams["figure.figsize"] = [16, 9]
    plt.rcParams["figure.dpi"] = 400
    plt.title("Zookeeper Animal Setup")
    plt.axis("off")
    plt.show()
