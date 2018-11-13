# Jupyter

*Lisez ceci dans d'autres idiomes: [English](README.md), [Español](README.es-ES.md), [Português](README.pt-BR.md)*

Jupyter metapackage pour installation et docs.

## Faire tourner les docs localement
D'abord naviguer dans le repertoire `/docs` et creer un environment `conda` :

```bash
conda env create -f environment.yml  
```  

Activer l'environment:

```bash
source activate jupyter_docs  
```

Construire les docs:

```bash
make clean  
make html
```

Les docs seront construit dans `build/html`. Ils peuvent etre vus dans `build/html/index.html` ou en demarrant le serveur HTTP puis en naviguamt sur `0.0.0.0:8000` dans votre navigateur web.
```bash
python3 -m http.server
```

