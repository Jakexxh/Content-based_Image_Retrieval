import os
def init():

    global project_path
    project_path= os.path.dirname(os.path.dirname(__file__))

    global image_path
    image_path = '../../data/image'

    global vocabulary_path
    vocabulary_path= '../../data/visual_word_vocabulary/vocabulary.pkl'

    global sift_path
    sift_path =  '../../data/sift/sift.pkl'

    global db_path
    db_path ='../../data/db/test.db'