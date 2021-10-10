from PIL import ImageTk, Image


image2 = Image.open('cube.png')
image2 = image2.resize((128,72), Image.ANTIALIAS)

image2.save("resizedCube.png")
