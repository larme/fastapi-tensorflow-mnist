train the model:

```
python train.py
```

run server with single process:

```
uvicorn main_sync:app --host 0.0.0.0 --port 3000
```

or run server with multiple workers:

```
uvicorn main_sync:app --host 0.0.0.0 --port 3000 --workers n
```
