---
theme: seriph
background: https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=2970&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Qeech
mdc: true
---

# Qeech

---
transition: fade-out
---

# Table des matières

<Toc maxDepth="1"></Toc>

---
layout: default
---

# Qu'est-ce que Qeech ?

C'est une application qui recommande des recettes de cuisine en fonction de plusieurs critères.

- Les ingrédients à disposition de l'utilisateur
- Les habitudes alimentaires de l'utilisateur
- La saison
- Le régime alimentaire de l'utilisateur

---
transition: slide-up
level: 1
---

# Calcul du score

Le score est calculé en fonction de plusieurs critères.

La formule utilisée est la suivante :

$$
\begin{align}
    score &= (habits\_score + ingredients\_score + season\_score) * diet\_score
\end{align}
$$

---
transition: slide-up
level: 2
---

## Score des habitudes alimentaires

C'est le score le plus complexe à calculer.

Chaque recette est placée dans un graph à 2 dimensions. Quand un utilisateur a interagi avec une recette, un lien est créé entre l'utilisateur et la recette. Les recettes sont ensuite "raprochées" en fonction des utilisateurs qui ont interagi avec elles.

Quand un utilisateur cherche une recommandation, on cherche les recettes les plus proches de l'utilisateur.

<img
  v-click
  class="absolute -bottom-9 -left-7 w-80"
  src="assets/food_com_graph_500_13_preview.png"
  alt=""
/>

---
transition: slide-up
level: 1
---

# Technologies utilisées

- [React Native](https://reactnative.dev/)
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [NetworkX](https://networkx.org/)

---
transition: slide-up
level: 1
---

# Démo

---
transition: slide-up
level: 1
---

# Le marché des applications de cuisine

- Sous chef : GPT qui donne des recettes en fonction des ingrédients qu'on aime et qu'on a
- Food.com : Une collection de recettes créées par les utilisateurs
- Frigo Magic : Application qui donne des recettes en fonction des ingrédients qu'on a
- Jow : Application qui prépare la liste de courses en fonction du régime alimentaire du foyer

---
transition: slide-up
level: 1
---

# Améliorations possibles

- Finir l'interface utilisateur
- Tri des recettes en fonction de leur qualité
- Amélioration des noms des recettes à l'aide d'une IA générative (Mistral)
- Prise en photo des ingrédients qu'on a pour les ajouter à la liste
- Intégration avec des applications de liste de courses
- Prise en compte des valeurs nutritionnelles des recettes
- Intégration avec des applications de fitness
- Recommander un repas entier (entrée, plat, dessert)
- Grouper les ingrédients par régime alimentaire
