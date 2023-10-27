from __future__ import annotations

import networkx as nx

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qeech_data.core.entities.recipe import Recipe
    from qeech_data.core.entities.user import User


def create_recipes_graph(*, recipes: list[Recipe], users: list[User]) -> nx.Graph:
    graph = nx.Graph()

    graph.add_nodes_from(map(lambda x: x.id, users), label="user")
    graph.add_nodes_from(map(lambda x: x.id, recipes), label="recipe")

    for user in users:
        for interaction in user.interactions:
            graph.add_edge(user.id, interaction.recipe.id, label="interaction")

    return graph
