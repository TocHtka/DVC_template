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

Change to another branch. On this branch the parameter height was adapted. After using dvc repro the output data should have changed without having recomputed anything.

```
git checkout changedImageSize
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

## Set up your own project

Create folder and use `git init`.

Initialize dvc:

```
dvc init
```

Define your pipeline in **dvc.yaml**:

```
stages:
  resize: 							<- stage name
    cmd: python src/resize.py data/raw_images data/resized 	<- command to be executed
    deps: <- dependencies
    - data/raw_images 						<- data
    - src/resize.py 						<- code
#   - K:/DVC_external_dependency				<- external dependency on Helbling Drive.
#   - s3://mybucket/data.txt					<- external dependency on S3.
    params: 							<- parameters
    - resize.height
    - resize.width
    outs:							<- output file/folder
    - data/resized
  nl-mean:
...
```

Define parameters in **params.yaml**

```
resize:
  width: 200
  height: 210
nl-mean:
resize:
  width: 200
  height: 210

nl-mean:
  patch_size: 5
```

Define a remote storage for data versioning and sharing with other colleagues:

```
dvc remote add -d projectRemote R:/HTK_Allgemein/Austausch_HTKA_HTKW/dvc_example
```
or 
```
dvc remote add -d storage s3://mybucket/dvcstore
```




