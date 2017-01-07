import pickle

from modules.dir_vocabulary.vocabulary import *

import modules.index_image.indexer

# image_path = '/Users/Jake/Daily-Projects/Python/Homework/Content-based_Image_Retrieval/data/image'
# imlist = imtools.get_imlist(image_path)
# nbr_imagess = len(imlist)
# # extract features
# featlist = [imname[:-3]+'visual_word_vocabulary' for imname in imlist]
# for i,imname in enumerate(imlist):
#     visual_word_vocabulary.process_image(imname, featlist[i])

with open('../dir_vocabulary/vocabulary.pkl') as f:
    voc = pickle.load(f)

index = modules.index_image.indexer.Indexer('test.db', voc)

index.create_tables()

# for i in range(nbr_imagess)[:100]:
#     locs,descr = visual_word_vocabulary.read_features_from_file(featlist[i])
#     index.add_to_index(imlist[i],descr)

index.db_commit()