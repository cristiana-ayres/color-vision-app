from detect import detect, opt

# the name of the model, generated through roboflor - google colab

def detect_image(filename):
    opt.weights = ("best.pt")
    opt.source = ("static/files/" + filename)
    detect()
