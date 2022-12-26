from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
from PIL import Image, ImageDraw
# importing the detect function, from another file
# from detect import detect, opt

# the name of the model, generated through roboflor - google colab
# opt.weights = ("best.pt")
# # the name of the picture, which is inside the folder 'yolo7'
# opt.source = ("0001.jpg")
# detect()

# detecting through model pieces of clothes

# folder = "crop"                           
# images_names = [filename for filename in os.listdir(folder)]
# crop_images_list = os.listdir(folder)
# print(crop_images_list)

# print(f"These cropped images are inside {folder} folder")

# for i in crop_images_list:
#     img = Image.open("crop/" + i)
#     img.show(i)
# this would open each image separetly

#Make piecharts folder
if not os.path.exists("static/pie_charts"):
    os.mkdir("static/pie_charts")

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_colors(image, number_of_colors, show_chart, name):
    
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    
    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    
    counts = Counter(labels)
    counts = dict(sorted(counts.items()))
    
    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (show_chart):
        plt.figure(figsize = (7, 5))
        # plt.title('Colors Detection ($n=5$)', fontsize=15)
        plt.pie(counts.values(), labels = hex_colors, colors = hex_colors, autopct='%1.1f%%')
        plt.legend(hex_colors, title="HEX Colors", loc='upper right', bbox_to_anchor=(0.1, 0.1), framealpha=0.5)
        plt.savefig(os.path.join("static/pie_charts",str(name.split('.')[0]) + "_pie_chart.jpeg"), bbox_inches='tight')
    
    return hex_colors

def color_model():
    folder = "static/crop"                           
    images_names = [filename for filename in os.listdir(folder)]
    crop_images_list = os.listdir(folder)
    hex_colors_all = []
    for i in crop_images_list:
        image = cv2.imread('static/crop/' + i)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)

        hex_colors = get_colors(get_image('static/crop/' + i), 5, True, i)
        hex_colors_all.append(', '.join(hex_colors))
    
    return hex_colors_all
    
