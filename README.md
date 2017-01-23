# Content Based Image Retrieval

​											Xiaohe Xue          	Jan 14th, 2016

## Introduction

​	This project is a rewritten version of Searching Images project in Chapter 7 in the book-***Programming Computer Vision***. This project has a simple but integrated ability of content based image retrieval. This project has five parts, creating vocabulary, indexing the image, searching in the database, ranking the images and  using in web demo.



## Project Structure



###Creating Vocabulary (Vocabulary)

*   Property

    | attribute    | Type   | DECR                             |
    | ------------ | ------ | -------------------------------- |
    | name         | string | name of vocabulary               |
    | voc          | list   | visual words, content of voc     |
    | idf          | list   | idf value of every visual word   |
    | trainingdata | list   | path of sift file of every image |
    | nor_word     | int    | number of visual words           |

*   Function

    1. train(self, featurefiles, k, subsampling)

       to create vocabulary. First read all the sift files of every image. Second, calculate the visual words by using k-means clustering. 

       Finally, go through all training images and project on vocabulary.

       ​

    2. project(self, descriptors)

       to create the histogram of every visual word

       ​


### Indexing the image (Indexer)

* Database Tables

  * imlist

    | type   | name | descr      |
    | ------ | ---- | ---------- |
    | string | file | image path |

  * imwords

    | type   | name    | descr           |
    | ------ | ------- | --------------- |
    | int    | imid    | image id        |
    | int    | wordid  | visual id       |
    | string | vocname | vocabulary name |

  * imhistograms

    | type      | name   | descr                     |
    | --------- | ------ | ------------------------- |
    | int       | imid   | image id                  |
    | histogram | pickle | histogram value in pickle |
    | vocname   | string | voc name                  |




### Ranking

​	show two different ways to rank the images, one is regular way, another is in homography way 

​	<u>the ranking functions need to be improved</u>



### Search the images

​	use basic inverted list which use visual words as primary element to implete searching the image retrieval.

### Implements in web

​	use flask web framework



## Notes



1. need to use tf-idf 



## Requirements



1. PCV

2. pysqlite2

3. pickle

4. PIL

5. numpy

6. pylab

7. scipy

8. vlfeat commad lines (shell not python modlues)

    http://www.vlfeat.org/install-shell.html

