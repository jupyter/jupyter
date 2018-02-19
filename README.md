# Jupyter

Meta paquetes de Jupyter para su instalacion y documentos.

## Ejecutando los documentos localmente
Primero navega al directorio `/docs` y crea un entorno en `conda`:

```bash
conda env create -f environment.yml  
```  

Activa el entorno:

```bash
source activate jupyter_docs  
```

Construye los documentos:

```bash
make clean  
make html
```

Los documentos se crearan en `build/html`. Ellos pueden ser vistos iniciando un servidor HTTP y navegando hasta `0.0.0.0:8000` en tu explorador web.

```bash
python3 -m http.server
```
