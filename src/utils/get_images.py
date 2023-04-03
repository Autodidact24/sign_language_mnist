import numpy as np
import pandas as pd
from PIL import Image
from fastai.vision.all import PILImage


def get_images(df):
    IMG_WIDTH =28
    IMG_HEIGHT=28
    
    df['img'] = df[df.columns[df.columns.str.startswith('pixel')]].apply(
        lambda x: PILImage(Image.fromarray(np.array(x.values).reshape((IMG_WIDTH,IMG_HEIGHT)).astype(np.uint8))),
        axis=1
    )
    
    return df[df.columns[[not x for x in df.columns.str.startswith('pixel')]]]