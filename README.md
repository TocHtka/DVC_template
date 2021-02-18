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

### change branch

```
git checkout featureBranch
dvc repro
```

## Project overview

```
C:.
│   .dvcignore
│   dvc.lock
│   dvc.yaml   <- Here we define the pipeline
│   LICENSE
│   params.yaml <- define the parameters that can be used in the source code
│   README.md
│   requirements.txt <- python packages needed
│
├───.dvc
│   │   .gitignore
│   │   config <- here a remote storage is defined
│   │
│   ├───cache
│   │   ├───15
│   │   │       7d08f4dd92b39488a711a31bdbe15f.dir
...
│   │   └───runs
│   │       ├───09
│   │       │   └───09898e149bb57c34994cbfc803250c2d2843474a55d3f792c959ad07ae85097b
│   │       │           ec4f1e6f280c4d9da93a6c9bb05531a52be18f7f33af030661316f8803855d5e
...
│   ├───plots
│   │       confusion.json
│   │       confusion_normalized.json
│   │       default.json
│   │       linear.json
│   │       scatter.json
│   │       smooth.json
│   │
│   └───tmp
│           lock
│           rwlock
│           state
│           updater.lock
│
├───data  <- put data here. Whenever used as dependency or output in a function (and defined in dvc.yaml) then will be added to .gitignore
│   │   .gitignore
│   │   raw_images.dvc
│   │   statistics.csv
│   │
│   ├───nl-mean
│   │       A_5.jpg
│   │       B_5.jpg
│   │       C_5.jpg
│   │       D_5.jpg
│   │
│   ├───raw_images
│   │       A.jpg
│   │       B.jpg
│   │       C.jpg
│   │       D.jpg
│   │
│   └───resized
│           A.jpg
│           B.jpg
│           C.jpg
│           D.jpg
│
└───src <- put source code here
        .RData
        .Rhistory
        image_statistics.R
        nl_mean.py
        resize.py
```

