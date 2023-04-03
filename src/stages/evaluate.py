import json

from fastai.vision.all import *
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

from src.utils.get_images import get_images

from box import ConfigBox
from ruamel.yaml import YAML

yaml = YAML(typ="safe")

def get_x(r): return r['img']
def get_y(r): return r['label']


def evaluate():
# Load the trained model
    params = ConfigBox(yaml.load(open("params.yaml", encoding="utf-8")))
    learn = load_learner(params['model']['save_path'])

    test_df = pd.read_csv(params['data_load']['test_data_path'])
    test_df = get_images(test_df)
    
    # Load the evaluation data
    dl = learn.dls.test_dl(list(test_df['img']))
    inp,preds,_,dec_preds = learn.get_preds(dl=dl, with_input=True, with_decoded=True)
    test_df['Label_pred'] = dec_preds



    # Convert the predictions and targets to numpy arrays
    preds = np.asarray(test_df['Label_pred'])
    targets = np.asarray(test_df['label'])
    print(preds, targets)


    # Calculate the evaluation metrics
    acc = accuracy_score(targets, preds)

    # Save the evaluation results to a JSON file
    results = {'accuracy': float(acc)} #, 'classification_report': report}
    with open(params['evaluate']['metrics_file'], 'w') as f:
        json.dump(results, f)

if __name__ == "__main__":
    evaluate()
