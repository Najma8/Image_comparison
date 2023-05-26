"""
Created on Mon Dec 13 20:10:24 2021

@author: NAJMA
"""
import cv2
import sys

#main.py -i1 C:\Users\Folder1\photo1.png -i2 C:\Users\Folder1\photo2.png -o C:\Users\Folder2\Sub_folder -d D:\Folder3\Sub_folder -s true

#since the command line from the command prompt is in the form of a list, converting the elements in the list to string:
inputs = sys.argv
inputsentence = ' '.join([str(element) for element in inputs])
#splitting the string to find properties of the external command line:
inputsentence = inputsentence.split('-')
#assignment of properties to related variables:
for x in inputsentence:
    if x[0] == "i" and x[1] == "1":
        path1 = (x[3:-1])
    elif x[0] == "i" and x[1] == "2":
        path2 = (x[3:-1])
    elif x[0] == "o":
        output_path = (x[2:-1])
    elif x[0] == "d":
        difference_path = (x[2:-1])
    elif x[0] == "s":
        show_or_not = (x[2:])

        
#reading photos from given path and assigning to relevant variables:
image1 = cv2.imread(path1)
image2 = cv2.imread(path2)
img1_shape = image1.shape
img2_shape = image2.shape
#comparison of the sizes of the two photos:
if img1_shape == img2_shape:
    print("Size : Same")
    #subtracting the first photo from the second photo to find the difference:
    difference1 = cv2.subtract(image1, image2)
    #subtracting the second photo from the first photo to find the difference:
    difference2 = cv2.subtract(image2, image1)
    #combining the difference results for a two-sided result:
    overall_difference = difference1+difference2
    
    b, g, r = cv2.split(overall_difference)
    #displaying the difference photo on the screen:
    if show_or_not == "true":
        cv2.imshow("Difference", cv2.resize(overall_difference, None, fx=0.8, fy=0.8))
    #saving the resulting difference photo to the given path:
    cv2.imwrite(difference_path+'difference.jpg', overall_difference)

    #print(cv2.countNonZero(b))
    #print(cv2.countNonZero(g))
    #print(cv2.countNonZero(r))
    #checking the BGR values of the photos if they are the same:
    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("Image1 and Image2: Same")
    else:
        print("Image1 and Image2: Not same")

    #cv2.imshow("b", b)
    #cv2.imshow("g", g)
    #cv2.imshow("r", r)

sift = cv2.SIFT_create()
#finding salient points for both photos:
kp_1, desc_1 = sift.detectAndCompute(image1, None)
kp_2, desc_2 = sift.detectAndCompute(image2, None)
index_parameters = dict(algorithm=0, trees=5)
search_parameters= dict()
#runing the image matching algorithm:
flann = cv2.FlannBasedMatcher(index_parameters, search_parameters)
#comparison of descs to find same spots in two photos:
similarity = flann.knnMatch(desc_1, desc_2, k=2)
#number of all salient points to calculate percentage:
all_points = flann.knnMatch(desc_1, desc_1, k=2)

#find ideal matches:
fair_points = []
for m, n in similarity:
    if m.distance < 0.5*n.distance:
        fair_points.append(m)
print("Total fair points:")
print(len(fair_points))
#calculating similarity ratio:
ratio = (len(fair_points)*100)/len(all_points)
#formatting the ratio:
percentage = "{:.0f}".format(ratio)
print("Similarity percentage: "+percentage+"%")
#drawing similar points found between two photos:
result = cv2.drawMatches(image1, kp_1, image2, kp_2, fair_points, None)
print("Show: "+show_or_not)
#saving result to given path:
cv2.imwrite(output_path+'result.jpg', result)
#display of first, second and final photos on the screen:
if show_or_not == "true":
    cv2.imshow("Result", cv2.resize(result, None, fx=0.8, fy=0.8))
    cv2.imshow("Image1", cv2.resize(image1, None, fx=0.8, fy=0.8))
    cv2.imshow("Image2", cv2.resize(image2, None, fx=0.8, fy=0.8))
cv2.waitKey(0)
cv2.destroyAllWindows()
