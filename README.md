# # About Color Vision App Project

The Final Project of Ironhack Data Analytics Bootcamp. October-November 2022, presented on December 2022.


## Overview  

Can you easily identify colors such as red, green, blue, purple, etc? 

Most people can do it, but a specific condition made me think about how hard it can be sometimes for people that misinterpret the colors as they really are. 

There is a condition called Color-Blindness, and this affect more men than women, actually. 

"Color blindness affects approximately 1 in 12 men and 1 in 200 women."

![](https://github.com/cristiana-ayres/color-vision-app/blob/main/flask_images/colorblindness.jpg)

Basically, and depending on the type of condition, some colors can be misinterpreted and that's not what we want in some cases, specially when we have to communicate using colors. 

## Why this matters

The purpose is to bring awareness: correct matching colors are pleasant and improves the intention to communicate clearly and objectively. 

My inspiration to develop this project came firstly by a well-known situation I've been living with my Dad: he's a color-blind person. Nothing that incapacitates him, but struggles to pick the correct object indicated by its color, and specially matching clothes. I've been his style coach since then. 

Then, as a Data Analyst, something in particular has caught my eye: if we are dealing with Data Visualization, colors are really important.   


## Problem Definition

Specially thought for the colorblind people, but also for anyone who's interested in how colors match the best!

The project brings, through Object Detection (Neural Networks) and Color Extraction (Unsupervised Learning Algorithm) models, a way to correctly identify colors in an outfit.


Project Planning: 

1. Data Gathering | Divided into 2 steps 
- Collecting images of outfits manually, at online shops, such as Mango, Zara, Massimo Dutti, etc...
- Then, in an automated way, through simple_image_download library, searching and locally saving directly from Google images.

- After selecting the best pictures to train the model, I ended up with 230 images in total.  

2. Model Building | and libraries used
- Through Roboflow, to annotate each image with the labels I wanted, splitting into labels
- Through Yolov7 and PyTorch, to finally generate the best model

3. Developing Functionality through Python | After Object Detecting, cropping the items into new images, followed by Color Extraction, using K-Means Clustering (Unsupervised Learning Method)

4. Demonstration on Flask | generating a webpage hosted locally

5. Making the webpage visually appealing according to the purpose, using HTML and CSS

## Home page

Passing through the images: from a Black&White wardrobe, we encounter happy people, colorful fully dressed, and finally an image that trully represents the purpose and usability of the webpage: discover, throught HEX colors codes, the true colors the user is dressing.

<p align="center" width="100%">
  <img width="150%" src="https://github.com/cristiana-ayres/color-vision-app/blob/main/flask_images/Home%20Page%20Carrousel.gif"/>
</p>

## About Section

Just scrolling down a bit, it is possible to have a brief description of how to use and enjoy the webpage. 

![](https://github.com/cristiana-ayres/color-vision-app/blob/main/flask_images/how_it_works.JPG)

# # Navigation bar

## Upload page

## Results page

## Dropdown | Suggestions

