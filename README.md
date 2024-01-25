# End-to-end-ML-with-mlflow
Mlops

# How to Run ?

### STEPS:

Clone the repository

```bash
https://github.com/hsiebenou/End-to-end-ML-with-mlflow/tree/master
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```

### STEP 02- Install the requirements
```bash
pip install -r requirements.txt
```

```bash
python app.py
```
now,
```bash
open up you local host and port
```

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


#### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/hsiebenou/End-to-end-ML-with-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=hsiebenou \
MLFLOW_TRACKING_PASSWORD=3dc1a66a800fb4c1281035c85ddf9375e8282b39 \
python script.py


Run this to export as env variables

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/hsiebenou/End-to-end-ML-with-mlflow.mlflow \
export MLFLOW_TRACKING_USERNAME=hsiebenou \
export MLFLOW_TRACKING_PASSWORD=3dc1a66a800fb4c1281035c85ddf9375e8282b39 \

```


### STEP 03
