import pytest

from app.csp.constraints import ConstraintSatisfactionProblem as CSP
from app.csp.zookeeper import ZookeeperConstraint


@pytest.fixture
def zoo_organization_problem():
    domain = [1, 2, 3, 4]
    problem = (
        CSP()
        .add_variable(var="Lion", domain=domain)
        .add_variable(var="Deer", domain=domain)
        .add_variable(var="Hyena", domain=domain)
        .add_variable(var="Tiger", domain=domain)
        .add_variable(var="Peacock", domain=domain)
        .add_variable(var="Meerkat", domain=domain)
        .add_variable(var="Wild Boar", domain=domain)
        .add_constraint(ZookeeperConstraint.Rejects("Lion", "Tiger"))
        .add_constraint(ZookeeperConstraint.MustBeTogetherWith("Meerkat", "Wild Boar"))
        .add_constraint(ZookeeperConstraint.Rejects("Hyena", "Lion"))
        .add_constraint(ZookeeperConstraint.Rejects("Hyena", "Deer"))
        .add_constraint(ZookeeperConstraint.Rejects("Hyena", "Peacock"))
        .add_constraint(ZookeeperConstraint.Rejects("Hyena", "Meerkat"))
        .add_constraint(ZookeeperConstraint.Rejects("Hyena", "Wild Boar"))
        .add_constraint(ZookeeperConstraint.Rejects("Tiger", "Meerkat"))
        .add_constraint(ZookeeperConstraint.Rejects("Tiger", "Wild Boar"))
        .add_constraint(ZookeeperConstraint.Rejects("Tiger", "Peacock"))
        .add_constraint(ZookeeperConstraint.RejectsSameOrAdjacent("Deer", "Lion"))
        .add_constraint(ZookeeperConstraint.RejectsSameOrAdjacent("Deer", "Tiger"))
        .add_constraint(ZookeeperConstraint.Rejects("Peacock", "Lion"))
        .add_constraint(ZookeeperConstraint.MustBeInCageID("Lion", 1))
    )
    return problem.backtracking_search()


def test_valid_zoo_configuration(zoo_organization_problem):
    result = zoo_organization_problem
    assert result["Lion"] == 1
    assert result["Meerkat"] == 1
    assert result["Wild Boar"] == 1
    assert result["Tiger"] == 2
    assert result["Peacock"] == 3
    assert result["Deer"] == 4
