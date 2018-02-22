# Jupyter

*Leer en otros idiomas: [English](README.md), [Español](README.es-ES.md)*

Meta paquete de Jupyter para su instalación y documentación.

## Ejecutando los documentos localmente
Primero navega al directorio `/docs` y crea un entorno en `conda`:

```bash
conda env create -f environment.yml  
```  

Activa el entorno:

```bash
source activate jupyter_docs  
```

Genera los documentos:

```bash
make clean  
make html
```

Los documentos se crearán en `build/html`. Éstos pueden ser vistos abriendo `build/html/index.html` o iniciando un servidor HTTP y navegando hasta `0.0.0.0:8000` en tu explorador web.

```bash
python3 -m http.server
```
