# DVC_template

## To use this example

```
git clone https://github.com/TocHtka/DVC_template.git
```

If you use conda:

```
conda create --name dvc_example --file requirements.txt
```

Manual installation:
```
pip install dulwich==0.20.18
pip install dvc
pip install scikit-image
```

### Run code

```
dvc repro
```

### Show DAG (graph)

```
dvc dag
```
