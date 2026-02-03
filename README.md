# Object Tracking with OpenCV

A real-time object tracking application using OpenCV's legacy tracking algorithms. This program allows users to track objects in video files with interactive controls for pausing, resuming, and selecting new regions to track.

## Features

- **Multiple Tracker Support**: Choose from 7 different tracking algorithms
- **Interactive Controls**: 
  - Pause/Resume tracking with 'P' key
  - Select new region with 'S' key
  - Exit with ESC key
- **Frame Scaling**: Automatically rescales video frames for better display
- **Visual Feedback**: Shows tracking status and bounding boxes
- **CSRT Tracker Default**: Uses the accurate CSRT tracker by default

## Requirements

- Python 3.x
- OpenCV (with legacy tracking module)
- NumPy (automatically installed with OpenCV)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/object-tracking.git
cd object-tracking
```

2. Install dependencies:
```bash
pip install opencv-python opencv-contrib-python
```

## Usage

1. Place your video file (e.g., `traffic.mp4`) in the project directory
2. Run the script:
```bash
python object_tracker.py
```

3. Controls:
   - **ESC**: Exit the program
   - **P**: Pause/Resume video playback
   - **S**: Select a new region to track (when paused)
   - **Mouse**: Draw a bounding box when in selection mode

## Available Trackers

The program supports the following OpenCV tracking algorithms:
- **BOOSTING**: Adaptive Boosting (AdaBoost) based tracker
- **MIL**: Multiple Instance Learning tracker
- **KCF**: Kernelized Correlation Filters
- **TLD**: Tracking, Learning and Detection
- **MEDIANFLOW**: Median Flow tracker
- **MOSSE**: Minimum Output Sum of Squared Error
- **CSRT**: Discriminative Correlation Filter with Channel and Spatial Reliability (Default)

## Code Structure

- `rescale_frame()`: Resizes frames to specified percentage
- `select()`: Handles ROI selection and tracker initialization
- Main loop: Processes video frames and handles user input
- Tracker initialization: Creates tracker based on selected type

## Customization

To change the default tracker, modify line 34:
```python
tracker_type = tracker_types[6]  # Change index to select different tracker
```

To adjust frame scaling, modify the `percent` parameter in `rescale_frame()` calls (default is 40%).

## Notes

- The legacy tracking module is used (`cv.legacy.*`) as newer OpenCV versions moved trackers to a different API
- Performance may vary depending on the chosen tracker and video resolution
- For best results with fast-moving objects, consider using CSRT or KCF

## Troubleshooting

1. **"Invalid Camera" error**: Ensure the video file exists and is accessible
2. **Poor tracking performance**: Try a different tracker algorithm or adjust scaling
3. **High CPU usage**: Increase the waitKey value or scale frames smaller

## Acknowledgments

- OpenCV for the computer vision library
- All contributors to the OpenCV tracking algorithms

---

**Note**: Replace `traffic.mp4` with your own video file name in the code before running.
