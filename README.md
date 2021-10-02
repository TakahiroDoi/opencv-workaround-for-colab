# opencv-workaround-for-colab
Convenience method to use **cv2.imshow** with minimal code change on Google Colab   

# Background 
* **cv2.imshow(title, image)** cannot be used on Google Colab
* Default workaround is **cv2_imshow(image)** from google.colab.patches
* But **cv2_imshow** takes only **image** as the input argument 
* Consequently, you have to manually delete the **title** each time... 
* This can become quite tedious when the original script or notebook used **cv2.imshow** many times.   
* And, of course, the originla title is not shown.
* Using **Cv2Workaround** class, you can show both title and image with just deleting one letter from the original line.  

# Usage
1. Create an instance of the **Cv2Workaround** class as **cv** (cv = Cv2Workaround)
2. Delete 2 from the original line: cv2.imshow(title, image) -> cv.imshow(title, image)
