# opencv-workaround-for-colab
Convenience method to use **cv2.imshow** on Google Colab with minimal code change    

# Background 
* **cv2.imshow(title, image)** cannot be used on Google Colab
* A common workaround is to use **cv2_imshow(image)** from google.colab.patches
* But **cv2_imshow** takes only **image** as the input argument 
* Consequently, you have to manually delete the **title** from the code each time... 
* This can become quite tedious when the original script or notebook used **cv2.imshow** many times.   
* And, of course, the originla title is not shown.
* Using **Cv2Workaround** class, you can show both title and image by just deleting one letter from the original line.  

# Usage
1. Create an instance of the **Cv2Workaround** class as **cv**: cv = Cv2Workaround()
2. Delete **2** from the original line: cv**2**.imshow(title, image) -> cv.imshow(title, image)

# Example 
https://colab.research.google.com/drive/1AJ3LfOK7ruuVj3EgR64WIgtTlMNQVb_8?usp=sharing
