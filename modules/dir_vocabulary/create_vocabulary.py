import pickle

from PCV.localdescriptors import sift
from PCV.tools import imtools

import modules.dir_vocabulary.vocabulary
import settings

settings.init()

imlist = imtools.get_imlist(settings.image_path)
nbr_images = len(imlist)

# extract features
featlist = [imname[:-3] + 'sift' for imname in imlist]
for i, imname in enumerate(imlist):
    sift.process_image(imname, featlist[i])

voc = modules.dir_vocabulary.vocabulary.Vocabulary('ukbenchtest')
voc.train(featlist, 100, 10)

# saving vocabulary
with open(settings.vocabulary_path , 'wb') as f:
    pickle.dump(voc, f)

with open(settings.sift_path,'wb') as f:
    pickle.dump(featlist,f)

print 'vocabulary is:', voc.name, voc.nbr_words
