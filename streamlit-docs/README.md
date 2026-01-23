# docs
## 1. github md viewer

## 2. mkdocs
- reads from `docs` folder
```bash
uv venv
uv add
uv add mkdocs mkdocs-material

mkdocs serve
```
[http://localhost:8000](http://localhost:8000)

## 3. CustomApp 
- Streamlit md view app (py)
- reads from `docs` folder
```bash

uv venv
uv init
uv add streamlit

cd streamlit-docs; 
streamlit run app.py
```
http://localhost:8501
