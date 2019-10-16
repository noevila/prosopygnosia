# Proso*Py*gnosia _(Pre-Project)_
Pre-project of a program written in python that helps people with prosopagnosia.

## The Project

#### What's prosopagnosia?

Prosopagnosia, also called face blindness, is a cognitive disorder of face perception in which the ability to recognize 
familiar faces, including one's own face (self-recognition), is impaired, while other aspects of visual processing 
(e.g., object discrimination) and intellectual functioning (e.g., decision-making) remain intact. The term originally 
referred to a condition following acute brain damage (acquired prosopagnosia), but a congenital or developmental form of
 the disorder also exists, which may affect up to 2.5% of people.
In addition, apperceptive sub-types of prosopagnosia struggle recognizing facial emotion.
### What will be ProsoPygnosia?

The initial idea of ProsoPygnosia it's that this will be a program writen in Python that helps people with propagnosia
recognising persons that the user with prosopagnosia has as friends on social networks.
The first idea is to work with Instagram as a social network, but due to the recent changes of Instagram's 
API and future terms and conditions it exists the posibilit that this program ends working with another 
social network and not with Instagram.

### How ProsoPygnosia will works?

The main idea is to download Instagram photos of the people that the user follows, then recognise the faces of the
this followers and relation it with their username and showing this relation to the user.
Once this will be implemented the second part of this app will be the emotional recognition with the faces.


## Tools, libraries and important APIS that are gonna be used


### face_recognition (python library)

Recognize and manipulate faces from Python or from the command line with the world's simplest face recognition library.

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


### fer2013

Dataset for faces, it will be used for the emotional recognition.


## Authors

* **Noé Vila Muñoz** - [noevila](https://github.com/noevila)

## Licenses

face_recognition license:

https://github.com/ageitgey/face_recognition/blob/master/LICENSE

~~Instagram API license:~~

~~https://www.instagram.com/about/legal/terms/api/~~

Instaloader license:

https://github.com/instaloader/instaloader/blob/master/LICENSE

Fer2013 license:

https://creativecommons.org/publicdomain/zero/1.0/

## Acknowledgments

* https://en.wikipedia.org/wiki/Prosopagnosia
* https://github.com/ageitgey/face_recognition
* https://www.instagram.com/developer/
* https://www.kaggle.com/deadskull7/fer2013
