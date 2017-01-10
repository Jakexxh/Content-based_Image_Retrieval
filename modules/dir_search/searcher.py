from pysqlite2 import dbapi2 as sqlite
from numpy import *
from pylab import *
from PIL import Image


class Searcher(object):
    def __init__(self, db, voc):
        self.con = sqlite.connect(db)
        self.voc = voc

    def __del__(self):
        self.con.close()

    def candidates_from_word(self, imword):
        im_ids = self.con.execute("select distinct imid from imwords where wordid=%d" % imword).fetchall()
        return [i[0] for i in im_ids]

    def candidates_from_histogram(self, imwords):
        words = imwords.nonzero()[0]

        candidates = []
        for word in words:
            c = self.candidates_from_word(word)
            candidates += c

        tmp = [(w, candidates.count(w) for w in set(candidates))]
        tmp.sort(cmp=lambda x, y: cmp(x[1], y[1]))
        tmp.reverse()

        return [w[0] for w in tmp]

    def get_imhistogram(self, imname):
        im_id = self.con.execute("select rowid from imlist where filename='%s'" % imname).fetchone()
        s = self.con.execute("select histogram from imhistograms where rowid='%d'" % im_id).fetchone()
        return pickle.load(str(s[0]))

    def query(self, imname):
        h = self.get_imhistogram(imname)
        candidates = self.candidates_from_histogram(h)

        matchscores = []
        for imid in candidates:
            cand_name = self.con.execute("select filename from imlist where rowid=%d" % imid).fetchone()
            cand_h = self.get_imhistogram(cand_name)
            cand_dist = sqrt(sum((h - cand_h) ** 2))
            matchscores.append((cand_dist, imid))

        matchscores.sort()
        return matchscores


def compute_score(src, imlist):
    nbr_images = len(imlist)
    pos = zeros((nbr_images, 4))
    for i in range(nbr_images):
        pos[i] = [w[1] - 1 for w in src.query(imlist[i])[:4]]

    score = array([(pos[i] // 4) == (i // 4) for i in range(nbr_images)]) * 1.0
    return sum(score) / (nbr_images)


def plot_results(src, res):
    figure()
    nbr_results = len(res)
    for i in range(nbr_results):
        imname = src.get_filename(res[i])
        subplot(1, nbr_results, i + 1)
        imshow(array(Image.open(imname)))
        axis('off')
    show()


"""
    src = imagesearch.Searcher(’test.db’)
    locs, descr = sift.read_features_from_file(featlist[0])
    iw = voc.project(descr)
    print ’ask using a histogram...’
    print src.candidates_from_histogram(iw)[:10]


    src = imagesearch.Searcher(’test.db’)
    print ’try a query...’
    print src.query(imlist[0])[:10]
"""
