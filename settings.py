import os
def init():
#     # global project_path = path.dirname()
    global project_path
    project_path= os.path.dirname(os.path.realpath('..'))
    # print project_path
    global image_path
    image_path = os.path.join(project_path,'data/image')
    global vocabulary_path
    vocabulary_path = os.path.join(project_path,'data/visual_word_vocabulary')
