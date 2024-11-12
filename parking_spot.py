import cv2
import pickle

width, height = 107, 48

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('carParkImg.png')
    
    # Draw rectangles for the parking spots
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    # Display the image
    cv2.imshow("Image", img)

    # Set the mouse callback function
    cv2.setMouseCallback("Image", mouseClick)

    # Wait for a key press
    key = cv2.waitKey(1)

    # Exit if the 'Esc' key is pressed
    if key == 27:  # 27 is the ASCII code for the 'Esc' key
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
