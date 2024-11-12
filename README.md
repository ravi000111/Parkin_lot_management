# Parkin_lot_management
This project uses OpenCV to detect available parking spots in a parking lot from a video feed. It allows users to manually mark the coordinates of parking spots in an image and tracks whether each parking space is occupied or available in a given video.

Features
Manual Spot Selection: The user can manually select parking spots by clicking on an image and save the coordinates using pickle.
Parking Spot Detection: The system processes a video feed to track whether parking spaces are occupied or free.
Visual Feedback: It displays the status of parking spots (free or occupied) on the video feed, highlighting available spots in green and occupied ones in red.
Real-time Updates: The system processes each frame of the video and updates the status of parking spaces.

## File Structure

```bash
.
├── carParkImg.png          # Image used to manually select parking spots
├── carPark.mp4             # Input video of the parking lot
├── CarParkPos              # File to store and retrieve parking spot coordinates
├── parkingspot.py          # Script to manually select parking spots
└── main.py                 # Main script to detect and track parking spots in the video

```

Requirements
Python 3.x
OpenCV
NumPy
CVZone (for text display in the video feed)
To install required dependencies, run:
```bash
pip install opencv-python opencv-python-headless numpy cvzone
```

How It Works
Step 1: Manually Mark Parking Spots (parkingspot.py)
Run the parkingspot.py script to manually select the parking spots in an image. Click on the image to mark the top-left corner of each parking spot, and right-click to remove a marked spot. The coordinates will be saved in the CarParkPos file using pickle.

Step 2: Track Parking Spot Availability (main.py)
Once the parking spots are marked, run the main.py script to process a video feed and track whether each parking spot is occupied or free. The system analyzes each frame of the video and marks parking spots in red (occupied) or green (free). It also shows the number of free parking spaces on the video.

Step 3: Exit
Press the Esc key to exit the video feed at any time.


Code Explanation

parkingspot.py
This script is used to manually select parking spots on an image. When the left mouse button is clicked, a new spot is marked. Right-clicking removes the selected spot.

The parking spot coordinates are saved in a pickle file (CarParkPos) for later use.
main.py

This script loads the saved parking spot coordinates and processes each frame of the input video (carPark.mp4).
It applies image processing techniques such as grayscale conversion, Gaussian blur, adaptive thresholding, and dilation to detect parking space occupancy.
It then counts the number of non-zero pixels in each parking spot's area to determine if the spot is free or occupied.
The result is displayed in real-time with free spots marked in green and occupied spots in red.


Example Output

The output is displayed in a window, showing the video with rectangles drawn around the parking spots. Free spots are highlighted in green, and occupied spots are highlighted in red. The number of free spots is shown at the top left of the video.

