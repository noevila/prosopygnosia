# Live Facial Recognition and Emotion Identification with Python and OpenCV


## The Project

This project consists of implementing live facial recognition and emotion identification with Python 3

## Tools, libraries and important APIS that are used on this program

### OpenCV

OpenCV (Open source computer vision) is a library of programming functions mainly aimed at real-time computer vision.


### Keras and Tensorflow

Keras is the high level API of Tensorflow, used for make and train deep learning models.


### ~~Instagram API~~


~~The Instagram API Platform can be used to build non-automated, authentic, high-quality apps and services that:~~

* ~~Help individuals share their own content with 3rd party apps.~~
* ~~Help brands and advertisers understand, manage their audience and media rights.~~
* ~~Help broadcasters and publishers discover content, get digital rights to media, and share media with proper 
attribution.~~

#### Updated (15/10/2019)


Because of the public API of Instagram is no longer available, and only the enterprise one, which I cannot full access
 due to  is private and only available for registered companies, is available for working with Instagram's data I'm
 gonna use another third part python library (with MIT license) called instaloader. 
 
 Here the official Instagram communicate:
```
UPDATE: Starting October 15, 2019, new client registration and permission review on Instagram API platform are 
discontinued in favor of the Instagram Basic Display API.
```


### Instaloader

* downloads public and private profiles, hashtags, user stories, feeds and saved media,
* downloads comments, geotags and captions of each post,
* automatically detects profile name changes and renames the target directory accordingly,
* allows fine-grained customization of filters and where to store downloaded media.


### Numpy

NumPy is the fundamental package for scientific computing with Python


### fer2013

Dataset for faces, it will be used for the emotional recognition.


## Authors

* **Noé Vila Muñoz** - [noevila](https://github.com/noevila)

## Licenses

OpenCV license:

https://opencv.org/license/

Keras and Tensorflow license:

https://github.com/keras-team/keras/blob/master/LICENSE

~~Instagram API license:~~

~~https://www.instagram.com/about/legal/terms/api/~~

Instaloader license:

https://github.com/instaloader/instaloader/blob/master/LICENSE

Numpy license:

https://numpy.org/license.html

fer2013 license:

https://creativecommons.org/publicdomain/zero/1.0/

## Acknowledgments

* https://github.com/ageitgey/face_recognition
* https://www.instagram.com/developer/
* https://www.kaggle.com/deadskull7/fer2013
