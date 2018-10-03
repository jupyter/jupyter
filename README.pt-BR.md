# Jupyter

*Ler em outros idiomas: [English](README.md), [Español](README.es-ES.md)*

Metapacote de Jupyter para instalação e documentação.

## Executando os documentos localmente
Primeiro navegue até o diretório `/ docs` e crie um ambiente `conda`:

```bash
conda env create -f environment.yml  
```  

Ative o ambiente:

```bash
source activate jupyter_docs  
```

Construa a documentação:

```bash
make clean  
make html
```

A documentação será construida em `build/html`. Pode ser vista em `build/html/index.html` ou inicando um servidor HTTP e navegando para `0.0.0.0:8000` no seu navegador web.
```bash
python3 -m http.server
```
