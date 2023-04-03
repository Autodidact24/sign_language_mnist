from pathlib import Path

from src.utils.get_images import get_images
from box import ConfigBox
from dvclive.fastai import DVCLiveCallback
from fastai.vision.all import *


from ruamel.yaml import YAML

yaml = YAML(typ="safe")



def train():
    params = ConfigBox(yaml.load(open("params.yaml", encoding="utf-8")))
    print(params)

    train_df = pd.read_csv(params['data_load']['train_data_path'])
    train_df = get_images(train_df)

    test_df = pd.read_csv(params['data_load']['test_data_path'])
    test_df = get_images(test_df)

    def get_x(r): return r['img']
    def get_y(r): return r['label']

    dblock = DataBlock(blocks=(ImageBlock, CategoryBlock), get_x = get_x, get_y=get_y)
    dls = dblock.dataloaders(train_df)

    learn = vision_learner(dls, resnet34, metrics=error_rate).to_fp16()

    learn.fine_tune(
        **params.train.fine_tune_args,
        cbs=[DVCLiveCallback(dir="reports/train", report="md")],
    )
    learn.export(fname=(Path("models") / "model.h5").absolute())


if __name__ == "__main__":
    train()