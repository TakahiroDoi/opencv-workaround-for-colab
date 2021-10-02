from google.colab.patches import cv2_imshow


class Cv2Workaround:

  def imshow(self, title, image):
    cv2_imshow(image)
    print(title,'\n')
