import networkx as nx

from qeech_data.core.entities.recipe import Recipe
from qeech_data.core.entities.user import User


def create_recipes_graph(recipes: list[Recipe], users: list[User]) -> nx.Graph:
    graph = nx.Graph()

    graph.add_nodes_from(users, label="user")
    graph.add_nodes_from(recipes, label="recipe")

    for user in users:
        for interaction in user.interactions:
            graph.add_edge(user, interaction.recipe, label="interaction")

    return graph
