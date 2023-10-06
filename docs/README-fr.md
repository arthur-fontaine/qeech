<h1 align="center">
  Qeech
</h1>

<p align="center">
  Application de recommendation de recettes de cuisine.
</p>

<p align="center">
  <a href="../README.md">🇺🇸🇬🇧 English</a>
</p>

## Comment fonctionne la recommendation de recettes ?

Le dataset utilisé pour la recommendation de recettes est [Food.com Recipes and User interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions).

Un score est appliqué pour chaque recette en fonction de l'utilisateurs. Plusieurs facteurs sont pris en compte pour déterminer ce score :
- [Les ingrédients à disposition de l'utilisateur](#les-ingrédients-à-disposition-de-lutilisateur)
- [Les habitudes alimentaires de l'utilisateur](#les-habitudes-alimentaires-de-lutilisateur)
- [La saison](#la-saison)
- [Le régime alimentaire de l'utilisateur (allergies, végétarien, halal, etc.)](#le-régime-alimentaire-de-lutilisateur-allergies-végétarien-halal-etc)

De manière arbitraire, le score d'une recette est calculé de la manière suivante :

```
score = (ingredients_score + habits_score + season_score) * diet_score
```

> **Note**
> `ingredients_score` pourrait être le pourcentage d'ingrédients de la recette que l'utilisateur a à disposition.
> `diet_score` serait égal à 0 si la recette contient un ingrédient que l'utilisateur ne souhaite pas consommer. Sinon, il serait égal à 1.

### Les ingrédients à disposition de l'utilisateur

L'utilisateur peut renseigner les ingrédients qu'il a à disposition.

### Les habitudes alimentaires de l'utilisateur

Différents clusters de recettes sont créés selon les interactions des utilisateurs avec les recettes.

L'utilisateur peut renseigner les recettes qu'il aime lors de l'onboarding de l'application. Ces recettes sont utilisées pour déterminer les recettes qui sont susceptibles de plaire à l'utilisateur.

*Graph représentant les clusters de recettes*

<img src="./assets/food_com_graph_500_13_preview.png" alt="Graph représentant les clusters de recettes" width="500"/>

### La saison

Les interactions des utilisateurs étant datées, il est possible de déterminer la période moyenne et/ou médiane de l'année où chaque recette est le plus cuisinée.

### Le régime alimentaire de l'utilisateur (allergies, végétarien, halal, etc.)

L'utilisateur indique simplement lors de l'onboarding de l'application les ingrédients qu'il ne souhaite pas consommer.

## Quelles futures fonctionnalités pourraient être ajoutées ?

- Normalisation du nom des recettes (à l'aide d'une IA générative)
- Grouper les ingrédients par régime alimentaire
- Reconnaissance d'image pour ajouter des ingrédients à disposition de l'utilisateur
