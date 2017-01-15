from flask import Flask, request, render_template, url_for
from modules.dir_search.searcher import *
from modules import settings
from PCV.localdescriptors import sift
from PCV.tools import imtools
from flask_images import *

settings.init()

app = Flask(__name__, static_url_path = "", static_folder = "data")


@app.route('/', methods=['GET'])
def signin_form():
    return render_template('search.html')


@app.route('/', methods=['POST'])
def signin():
    # img_path = str(request.form['image_path'])
    imlist = imtools.get_imlist(settings.image_path[6:])

    with open(settings.vocabulary_path[6:]) as f:
        voc = pickle.load(f)

    # with open(settings.sift_path[3:]) as f:
    #     featlist = pickle.load(f)

    src = Searcher(settings.db_path[6:],voc)
    locs, descr = sift.read_features_from_file('data/image/ukbench00000.sift')
    iw = voc.project(descr)

    k=src.candidates_from_histogram(iw)[:10]

    result_list = [ '<img src=' + url_for('static',filename=str(src.get_filename(x))[10:]) + '>'  for x in src.candidates_from_histogram(iw)[:10]]
    ans_list=''
    for x in result_list:
        ans_list+=x
    return '<h2>Retrieval Ans:</h2><br>'+ans_list



if __name__ == '__main__':
    app.run()
