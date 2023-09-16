<p align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/LogiscrutPY/master/images/icon.png" width=150 />
</p>

<br>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=release&message=v1.0&color=blue" alt="Release - v1.0" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=version&message=Stable&color=green" alt="Version - Stable" />
  </a>
  <a href="https://choosealicense.com/licenses/mit">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
  </a>
</div>

<h4 align="center">LogiscrutPY</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#usage">Usage</a> •
  <a href="#configuration">Configuration</a>
</p>

<br>
<br>

## Description

**LogiscrutPY** est une application qui permet de traiter des fichiers CSV en convertissant leurs données dans un format spécifique, puis en les enregistrant dans de nouveaux fichiers CSV. Ce fichier README explique comment paramétrer l'application pour l'utiliser avec votre propre configuration.

<br><br>

## Usage

Pour utiliser LogiscrutPY, vous devez suivre ces étapes :

1. Clonez ce dépôt sur votre ordinateur.
2. Assurez-vous d'avoir Python installé sur votre système.
3. Installez les dépendances requises en exécutant la commande suivante :
    ```bash
    pip install -r requirements.txt
    ```
4. Modifiez le fichier `config.yml` avec vos valeurs de configuration personnalisées.
5. Exécutez le fichier `main.py` pour lancer l'application :
    ```bash
    python main.py
    ```
6. L'application sera minimisée dans la barre système, et elle commencera à surveiller le dossier spécifié dans la configuration. Lorsque des fichiers CSV sont détectés dans ce dossier, ils seront convertis et enregistrés dans de nouveaux fichiers CSV.

<br>

## Configuration

La configuration de LogiscrutPY se fait en modifiant le fichier `config.yml`. Voici les paramètres de configuration disponibles :
- `default`: Les valeurs par défaut pour différents paramètres de l'application, tels que les numéros de compte, les poids par défaut, etc.
- `gui`: Les paramètres liés à l'interface graphique, comme la taille des champs de saisie.
- `config`: Les paramètres de configuration généraux de l'application, tels que le chemin du fichier de configuration, l'extension de fichier à surveiller, etc.

Pour que le scan des fichiers fonctionne correctement, assurez-vous d'avoir bien remplacé `<VOTRE-EXTENSION-DE-FICHIER>` par l'extension de votre choix.
