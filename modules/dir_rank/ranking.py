import pickle

import PCV.geometry.homography as homog
from PCV.localdescriptors import sift
from PCV.tools import imtools
import sys
from modules import settings
from modules.dir_search import searcher
from modules.dir_vocabulary import vocabulary

sys.modules['vocabulary'] = vocabulary

settings.init()

imlist = imtools.get_imlist(settings.image_path)
nbr_images=len(imlist)

with open(settings.sift_path, 'rb') as f:
    featlist = pickle.load(f)

with open(settings.vocabulary_path, 'rb') as f:
    voc = pickle.load(f)

src = searcher.Searcher(settings.db_path, voc)

q_ind =2
nbr_results=2

res_reg = [w[1] for w in src.query(imlist[q_ind])[:nbr_results]]
print 'top matches (regular):', res_reg

q_locs,q_descr=sift.read_features_from_file(featlist[q_ind])
fp= homog.make_homog(q_locs[:,:2].T)

model =homog.RansacModel()

rank={}

for ndx in res_reg:
    locs,descr=sift.read_features_from_file(featlist[ndx])

    matches=sift.match(q_descr,descr)
    ind=matches.nonzero()[0]
    ind2=matches[ind]
    tp=homog.make_homog(locs[:,:2].T)

    try:
        H,inliners= homog.H_from_ransac(fp[:,ind],tp[:ind2],model,match_theshold=4)
    except:
        inliners=[]

    rank[ndx]=len(inliners)

sorted_rank=sorted(rank.items(),key=lambda t:t[1],reverse=True)
res_geom=[res_reg[0]+s[0] for s in sorted_rank]
print 'top matches (homography):',res_geom

searcher.plot_results(src,res_reg[:8])
searcher.plot_results(src,res_geom[:8])
