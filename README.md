Checking if two images are equal/similar using opencv library in python.
The two main elements the program uses to compare the 2 images are:
1: By checking if the two image has the same size and channels.
2: By checking if both of the picture's pixels has the same value.

Finding the difference:
First the program takes two images as Input one (-i1/image path) and Input two (-i2/image path) through command prompt, then to check if the images are exactly the same the program will compare the size/shape of both images. Using the "subtract" function of cv2 the program extracts the difference between the 2 images and generates the (Difference) image which will be saved at the path given as Difference (-d) through cmd. 

Finding the similarity:
The program uses "SIFT" function to compute and detect keypoints and descriptors for both images, then using "flann"  function of the open-cv library to draw the matches between the 2 images and to calculate the similar points between the images and overall points for calculating the percentage of similarity. The program generates an image showing all the matches between the two images and saves it by the name of (Result) which will be saved at the path given as Output (-o) through cmd.

Overall the program generates 2 images (Difference and Result), calculates the similarity percentage and total fair points.

cmd input example: main.py -i1 C:\Users\Folder1\photo1.png -i2 C:\Users\Folder1\photo2.png -o C:\Users\Folder2\Sub_folder -d D:\Folder3\Sub_folder -s true

-i1: path_to_Image1, -i2: path_to_Image2, -o: path to "output" image, -d: path to "difference" image, -s: show images(true)/don't show images(false)
