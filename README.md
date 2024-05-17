<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>


<h1 align="center">Car COUNTER👀🏎 </h1>
<h1 align="center">With Opencv🥇</h1>






<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<p align="center">
<img src="https://img.shields.io/badge/language-python-blue?style"/><img src="https://img.shields.io/github/stars/jokernets/face-plot"/><img src="https://img.shields.io/github/forks/jokernets/face-plot"/>
</p>


   


<h4 align="center">🛑Time to study 10 minutes⚠👁‍🗨</h4>


## How create Care Counter white Opncv-python:
- `Reading to` [requriment](https://github.com/jokernets/car-counter/requriment.md)
- 
--------------------------------------------------------------------------------------------------------------------------
# Installation 

## Install the Library with pip:

```python
pip install opencv-python
pip install numpy
```
Update existing installation:`pip3 install (YOUR LIBRARY) --upgrade`
(update as often as possible because this library is under active development)

-----------------------------------------------------------------------------------------------------------------------------

```python
import cv2
import numpy as np
```


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
- `cap = cv2.VideoCapture('video.mp4')`.This line initializes a `cv2.VideoCapture` object with your video file `video.mp4`. This `cap` object is used to capture frames from your video.
- "min_width_rect = 80".
 - "min_height_rect = 80".
These lines set the minimum width and height for moving objects detected in the video. Any detected object with a width or height less than these values is ignored.
- `control_line_position = 550`This line sets the position of a line (possibly horizontal) in the video frame. This line can be used to count objects passing through it.
- `algo = cv2.createBackgroundSubtractorMOG2()`This line creates a background subtractor object using the MOG2 algorithm. This `pattern` object is used to subtract the background from each frame, allowing for the detection of moving objects.

- Remember, after setting these parameters, you typically apply background subtraction to each frame in a loop, use thresholding and contours to detect moving objects, filter out small objects, and then perform your desired analysis on the detected objects. you do

```python
cap = cv2.VideoCapture('video.mp4')
min_width_rect = 80
min_height_rect = 80
counter_line_postion = 550
algo = cv2.createBackgroundSubtractorMOG2()
```



<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

- This is a function named `center_handle` that takes four parameters: `x`, `y`, `w`, `h`. These parameters represent the x-coordinate, y-coordinate, width, and height of a rectangle (possibly a bounding box around a detected object). The function calculates the center (`cx`, `cy`) of the rectangle and returns these coordinates.
- `detect = []`This line initializes an empty list named `detect`. This list might be used to store the centers of detected objects.
- `offset = 6`This line sets an `offset` value to 6. This could be used as a threshold for determining whether an object has moved or crossed a line.
- `counter = 0`This line initializes a `counter` variable to 0. This variable might be used to count the number of objects that have crossed a certain line in the video frame.

- Remember, the actual use of these variables and functions would depend on the rest of your code. This is just an analysis based on common practices in video processing tasks.

```python
def center_handle(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []
offset = 6
counter = 0
```



<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

- `while True:`This line starts an infinite loop. This is common in video processing tasks where you want to process each frame of the video continuously
- 
- `ret, frame1 = cap.read()`This line reads the next frame from the video capture object `cap`. The `read()` function returns two values: a boolean `ret` that indicates if the frame was read correctly, and the frame itself `frame1`.


- `grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)`This line converts the color frame to grayscale using the `cv2.cvtColor()` function. This is often done in video processing tasks as many operations like background subtraction and contour detection work better on grayscale images.

- `blur = cv2.GaussianBlur(grey, (3, 3), 5)`This line applies a Gaussian blur to the grayscale image. This is done to reduce noise in the image which can improve the results of subsequent operations.


- `img_sub = algo.apply(blur)`This line applies the background subtractor `algo` to the blurred image. This will return a binary image where the white pixels correspond to the foreground (moving objects) and the black pixels correspond to the background.


- `dilat = cv2.dilate(img_sub, np.ones((5, 5)))`This line dilates the image, which can help to merge adjacent contours and fill small holes in the contours.


- `kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)`

These lines perform morphological closing on the image. Closing is a dilation followed by an erosion. It is useful in closing small holes or dark areas within an object.


- `countershape, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)`This line finds the contours in the image. The contours are a useful tool for object detection and are often used to find the boundary of objects.


- `cv2.line(frame1, (25, counter_line_postion), (1200, counter_line_postion), (255, 127, 0), 3)This line draws a line on the original frame. This could be the line that you're using to count objects that cross it. The parameters are the image, the start and end point of the line, the color of the line, and the thickness, respectively.
```python
while True:
    ret, frame1 = cap.read()
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    countershape, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.line(frame1, (25, counter_line_postion), (1200, counter_line_postion), (255, 127, 0), 3)
```


<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

- `for (i, c) in enumerate(countershape):`This line starts a loop over the contours found in the image. The `enumerate()` function is used to get both the index `i` and the contour `c`.

`(x, y, w, h) = cv2.boundingRect(c)`This line calculates the bounding rectangle of the contour `c`. The `cv2.boundingRect()` function returns the x-coordinate, y-coordinate, width, and height of the rectangle.

- `cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)`This line draws a rectangle around the detected object on the frame.


- `center = center_handle(x, y, w, h)
detect.append(center)`
These lines calculate the center of the bounding rectangle using the `center_handle()` function and append the center to the 

- `cv2.circle(frame1, center, 4, (0, 0, 255), -1)`This line draws a circle at the center of the detected object on the frame.

- `for (x, y) in detect:
    if y < (counter_line_postion + offset) and y > (counter_line_postion - offset):
        counter += 1
    cv2.line(frame1, (25, counter_line_postion), (1200, counter_line_postion), (0, 127, 255), 3)
    detect.remove((x, y))
    print("Car Counter:" + str(counter))`
These lines loop over each center in the `detect` list. If the y-coordinate of the center is within a certain range of the `counter_line_position`, the `counter` is incremented, indicating that an object has crossed the line. The center is then removed from the `detect` list. The current count is printed to the console. A line is also drawn at the`counter_line_position` on the frame.

```python
    for (i, c) in enumerate(countershape):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_rect) and (h >= min_height_rect)
        if not validate_counter:
            continue
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)
        for (x, y) in detect:
            if y < (counter_line_postion + offset) and y > (counter_line_postion - offset):
                counter += 1
            cv2.line(frame1, (25, counter_line_postion), (1200, counter_line_postion), (0, 127, 255), 3)
            detect.remove((x, y))
            print("Car Counter:" + str(counter))
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>

## :


1. `cv2.putText(frame1, "COUNTER:" + str(counter), (500, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5": This line of code puts a text on Places the image `frame1`. The text ``COUNTER:'' + str(counter)` is written at position `(500, 70)` with the font `cv2.FONT_HERSHEY_SIMPLEX` and the text color `(0, 0 , 255)` (i.e. red) and the thickness of the line is `5`.

2. `#cv2.imshow('Detector', dilatada)`: This line of code is disabled by a `#`. If it was not disabled, it would open a window called 'detector' and give the 'dilatada' image.

3. `cv2.imshow('video orginal', frame1)`: This line of code opens a window named 'video original' and displays the image `frame1`.

4. `if cv2.waitKey(100) & 0xFF == ord('q'): break: This line of code breaks the program if the user presses the 'q' key. `cv2.waitKey(100)` creates a 100ms timeout.

5. `cv2.destroyAllWindows()`: This line of code closes all windows opened by OpenCV.

6. `cap.release()`: This line of code releases the image input source (eg camera or video file). This is important to free up system resources.
```python
    cv2.putText(frame1, "COUNTER:" + str(counter), (500, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    #cv2.imshow('Detector', dilatada)
    cv2.imshow('video orginal', frame1)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
```
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
## More Examples and Showcase 👑
<img src="https://github.com/jokernets/car-counter-/blob/main/public/car.png" width=500 height=400>
<img src="https://github.com/jokernets/car-counter-/blob/main/public/cargif.gif" width=500 height=400>



### Video image of the APP 📺 [Watching the video](https://github.com/jokernets/car-counter-/blob/main/public/via.mp4)




# `𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐌𝐞`🎈🎃

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammadfallahnejad/" height="40" width="60" /></a>
