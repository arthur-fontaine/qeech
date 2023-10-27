from __future__ import annotations

import networkx as nx

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from qeech_data.core.entities.recipe import Recipe
    from qeech_data.core.entities.user import User


def habits_score(recipe: Recipe, *, user: User, recipes_graph: nx.Graph) -> float:
    try:
        shortest_path_length = nx.shortest_path_length(recipes_graph, source=user.id, target=recipe.id)
        score = 1 / (1 + shortest_path_length)
        return score
    except nx.NetworkXNoPath:
        return 0
