
import cv2 as cv
import sys

# Function to rescale the frame to a percentage of the original size
def rescale_frame(frame, percent=40):
   width = int(frame.shape[1] * percent / 100)
   height = int(frame.shape[0] * percent / 100)
   dim = (width, height)
   return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

# Function to select a region and initialize the tracker
def select(frame, bbox):
   # Select the region (Bounding Box) for tracking the object
   bbox = cv.selectROI('frame', frame, True, False)
   # Set the coordinates of the selected region
   x, y, w, h = (int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]))
   # Extract the template from the image based on the selected region
   template = frame[y:y + h, x:x + w]
   # Initialize the tracker with the frame and selected region
   tracker.init(frame, bbox)
   return frame, bbox

# Pause/resume status
paused = False
# Initial value for the tracking region
bbox = None

# Load video from file
cap = cv.VideoCapture('traffic.mp4')

# Select tracker type
tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
tracker_type = tracker_types[6]  # Select CSRT type

# Select and create tracker based on the chosen type
if tracker_type == 'BOOSTING':
   tracker = cv.legacy.TrackerBoosting_create()
elif tracker_type == 'MIL':
   tracker = cv.legacy.TrackerMIL_create()
elif tracker_type == 'KCF':
   tracker = cv.legacy.TrackerKCF_create()
elif tracker_type == 'TLD':
   tracker = cv.legacy.TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
   tracker = cv.legacy.TrackerMedianFlow_create()
elif tracker_type == 'MOSSE':
   tracker = cv.legacy.TrackerMOSSE_create()
elif tracker_type == "CSRT":
   tracker = cv.legacy.TrackerCSRT_create()

# Read the first frame from the video
ret, frame = cap.read()
if not ret:
   # If the frame is invalid, exit the program
   print('Invalid Camera')
   sys.exit()

# Main program loop
while True:
   if not paused:  # If the program is not paused
       ret2, frame = cap.read()  # Read the next frame
       if not ret2:
           # If the frame is invalid or the video ends
           print('Failed to read frame or end of video')
           break

       frame = rescale_frame(frame)  # Rescale the frame

       # Update the tracker with the new frame
       success, bbox = tracker.update(frame)
       if success:
           # If the object is successfully tracked, draw a rectangle around it
           x, y, w, h = (int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]))
           cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3, 3)
           cv.putText(frame, 'Tracking', (25, 25), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
       else:
           # If the object is lost
           cv.putText(frame, 'Lost', (25, 25), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

   # Display the frame
   cv.imshow('frame', frame)
   key = cv.waitKey(5)
   if key == 27:
   # If the 'ESC' key is pressed, exit the program
       break
   elif key == ord('p') or key == ord('P'):
   # If the 'P' key is pressed, pause/resume
       paused = not paused
   elif key == ord('s') or key == ord('S'):
   # If the 'S' key is pressed, select a region
       frame, bbox = select(frame, bbox)

# Release resources
cap.release()
cv.destroyAllWindows()
