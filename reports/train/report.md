# DVC Report

params.yaml

| model      |   batch_size |   batch_per_epoch | frozen   |   frozen_idx | transforms                                                                                                                                         |
|------------|--------------|-------------------|----------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Sequential |           64 |               343 | False    |            0 | [Pipeline: train.<locals>.get_x -> PILBase.create, Pipeline: train.<locals>.get_y -> Categorize -- {'vocab': None, 'sort': True, 'add_na': False}] |

metrics.json

| train                          | eval                             |   error_rate |   step |
|--------------------------------|----------------------------------|--------------|--------|
| {'loss': 0.002702858531847596} | {'loss': 2.1318168364814483e-05} |            0 |      8 |

![static/error_rate](static/error_rate.png)

![static/train/loss](static/train/loss.png)

![static/eval/loss](static/eval/loss.png)
