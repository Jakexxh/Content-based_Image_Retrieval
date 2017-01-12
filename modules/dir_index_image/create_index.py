import pickle
from modules import settings
settings.init()

import sys
from PCV.localdescriptors import sift
from PCV.tools import imtools

from modules.dir_vocabulary import vocabulary
from modules.dir_index_image import indexer

sys.modules['vocabulary'] = vocabulary

with open(settings.vocabulary_path) as f:
    voc = pickle.load(f)

with open(settings.sift_path) as f:
    featlist = pickle.load(f)

imlist = imtools.get_imlist(settings.image_path)
nbr_images = len(imlist)

index = indexer.Indexer(settings.db_path, voc)

index.create_tables()

for i in range(nbr_images)[:100]:
    locs,descr = sift.read_features_from_file(featlist[i])
    index.add_to_index(imlist[i],descr)

index.db_commit()