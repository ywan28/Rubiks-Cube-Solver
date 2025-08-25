import cv2
import numpy as np
imageList = ['RedSide.jpg','BlueSide.jpg','OrangeSide.jpg','GreenSide.jpg','WhiteSide.jpg','YellowSide.jpg']
coordinateList = [[190,190],[280,190],[370,190],[190,280],[280,280],[370,280],[190,370],[280,370],[370,370]]
for image in imageList:
    for coordinate in coordinateList:
        x = coordinate[0]
        y = coordinate[1]
        imageCheck = cv2.imread(image)
        b, g, r = imageCheck[y, x]
        # Define color thresholds (BGR values)
        blue_lower = np.array([50, 0, 0])
        blue_upper = np.array([255, 100, 100])

        red_lower = np.array([0, 0, 100])
        red_upper = np.array([100, 100, 255])

        green_lower = np.array([0, 100, 0])
        green_upper = np.array([100, 255, 100])

        orange_lower = np.array([0, 100, 200])
        orange_upper = np.array([100, 200, 255])

        white_lower = np.array([150, 150, 150])
        white_upper = np.array([255, 255, 255])

        yellow_lower = np.array([0, 150, 150])
        yellow_upper = np.array([149, 255, 255])

        # Example pixel's BGR values (replace with actual pixel values)
        pixel_bgr = np.array([b, g, r])

        # Check if the pixel falls within the defined color thresholds
        if (blue_lower <= pixel_bgr).all() and (pixel_bgr <= blue_upper).all():
            print("Blue")
        elif (red_lower <= pixel_bgr).all() and (pixel_bgr <= red_upper).all():
            print("Red")
        elif (green_lower <= pixel_bgr).all() and (pixel_bgr <= green_upper).all():
            print("Green")
        elif (orange_lower <= pixel_bgr).all() and (pixel_bgr <= orange_upper).all():
            print("Orange")
        elif (white_lower <= pixel_bgr).all() and (pixel_bgr <= white_upper).all():
            print("White")
        elif (yellow_lower <= pixel_bgr).all() and (pixel_bgr <= yellow_upper).all():
            print("Yellow")
        else:
            print(b,g,r)

