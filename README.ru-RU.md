# Jupyter

*Прочитайте это на других языках: [English](README.md), [Español](README.es-ES.md), [Português](README.pt-BR.md), [Русский](README.ru-RU.md)*

Метапакет Jupyter для установки и документации.

## Локальный запуск документов
Сначала перейдите в каталог `/docs` и создайте среду `conda`:

```bash
conda env create -f environment.yml  
```  

Активация среды:

```bash
source activate jupyter_docs  
```

Сборка документов:

```bash
make clean  
make html
```

Документы будут встроены в `build/html`. Их можно просмотреть, открыв `build/html/index.html` или запустив HTTP-сервер и перейдя к `0.0.0.0:8000` в вашем веб-браузере.
```bash
python3 -m http.server
```
