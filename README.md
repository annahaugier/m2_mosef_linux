# Statistiques du crime en France

Ce repository contient plusieurs modules téléchargeant les données de la gendarmerie concernant le crime en France par département et propose une application web permettant de visualiser différentes statistiques. Entre autres, il est possible de visualiser le nombre de crimes classés par type de crime par département mais aussi par année.

---

## Utilisation

Pour lancer cette application, il faut construire l'image Docker grâce au Dockerfile à l'aide de la commande suivante:

```sh
docker build -t crime_en_france .
```

puis la lancer grâce à:

```sh
docker run crime_en_france
```

## Utilisation sans docker

Il est possible de lancer l'application sans docker grâce aux scripts disponibles à la racine du projet **install.sh** et **launch.sh**. Attention, ces scripts nécessitent un OS basé sur Unix.

Il faut tout d'abord lancer le script **install.sh** pour pré-installer et préparer l'environnement puis **launch.sh** qui lancera les modules de récupération/gestion de données avant de lancer l'application web.

## Accéder à l'application

Pour accéder à l'application après avoir lancé le container ou la plateforme web sans container, il faut lancer un navigateur puis accéder à l'url suivante: [http://localhost:8050](http://localhost:8050)
