<h1 align="center">
  Qeech
</h1>

<p align="center">
  Cooking recipe recommendation application.
</p>

<p align="center">
  <a href="/docs/README-fr.md">🇫🇷 Français</a>
</p>

## How does the recipe recommendation work?

The dataset used for recipe recommendation is [Food.com Recipes and User interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions).

A score is applied for each recipe based on the user. Several factors are taken into account to determine this score:
- [The ingredients available to the user](#the-ingredients-available-to-the-user)
- [The user's eating habits](#the-user's-eating-habits)
- [The season](#the-season)
- [The user's diet (allergies, vegetarian, halal, etc.)](#the-user's-diet-allergies-vegetarian-halal-etc)

Arbitrarily, the score of a recipe is calculated as follows:

```
score = (ingredients_score + habits_score + season_score) * diet_score
```

> **Note**
> `ingredients_score` could be the percentage of ingredients in the recipe that the user has available.
> `diet_score` would be equal to 0 if the recipe contains an ingredient that the user does not wish to consume. Otherwise, it would be equal to 1.

### The ingredients available to the user

The user can enter the ingredients he has available.

### The user's eating habits

Different clusters of recipes are created according to the users' interactions with the recipes.

The user can enter the recipes he likes during the application's onboarding. These recipes are used to determine which recipes are likely to appeal to the user.

*Graph representing the clusters of recipes*

<img src="./docs/assets/food_com_graph_500_13_preview.png" alt="Graph representing the clusters of recipes" width="500"/>

### The season

As the users' interactions are dated, it is possible to determine the average and/or median period of the year when each recipe is most cooked.

### The user's diet (allergies, vegetarian, halal, etc.)

The user simply indicates during the application's onboarding the ingredients he does not wish to consume.

## What future features could be added?

- Normalization of the name of the recipes (using a generative AI)
- Grouping ingredients by diet
- Image recognition to add ingredients available to the user
