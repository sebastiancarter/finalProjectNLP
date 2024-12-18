import matplotlib.image as mpimg
import matplotlib.pyplot as plt


img = mpimg.imread("cat2.png")

greenToRedRatio = (img[:,:,1] / (img[:,:,0] + 0.00001))
greenToBlueRatio = (img[:,:,1] / (img[:,:,2] + 0.00001))

nonEyes = ((greenToBlueRatio <= 1.07) | (greenToRedRatio <= 1.07))

print(nonEyes)

img[nonEyes] *= 0.5

plt.imshow(img)
plt.show()
