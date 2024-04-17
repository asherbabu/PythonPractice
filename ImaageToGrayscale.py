#Image to Grayscale fucntion
import cv2
def grayScale(filename):
    print(f"Image Gray Scale for {filename}")
    img = cv2.imread(f"Uploads/{filename}")
    imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    newFilename = f"Static/{filename}"
    cv2.imwrite(newFilename, imgProcessed)
    return newFilename