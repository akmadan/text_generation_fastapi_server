## Create a Virtual Environment
```python -m venv venv```

## Activate the venv
```venv/Scripts/activate```

## Install required libraries
```pip install fastapi uvicorn torch numpy transformers```

## Run the server
```uvicorn main:app --reload```