from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from pathlib import Path
from mlProject.pipeline.prediction import PredictionPipeline
from mlProject.utils.common import read_yaml
from mlProject import logger


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def training():
    os.system('python main.py')
    return "Training Successful ! "


@app.route('/predict', methods=['GET'])
def predict():
    try:
        data = pd.read_csv(Path('artifacts/data_transformation/test.csv'))
        y_column = read_yaml(path_to_yaml = Path("schema.yaml")).get('TARGET_COLUMN').get('name')
        data.drop(columns=y_column, axis = 1, inplace=True)
        obj = PredictionPipeline()
        predict = obj.predict(data)
        pred = pd.DataFrame(predict)
        os.makedirs('artifacts/prediction', exist_ok=True)
        pred.to_csv('artifacts/prediction/pred.csv')
        return render_template('results.html')
    except Exception as e:
        print('The Exception message is: ', e)
        return 'something is wrong'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)