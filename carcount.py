import cv2
import numpy as np
import sys

sys.path.append("C:/Users/mmani/opencv/sort")  # Ensure Python finds sort.py
from sort import Sort  # Import SORT Tracker

# Load video
video_source = "C:/Users/mmani/opencv/video (1).mp4"
cap = cv2.VideoCapture(video_source)

# Background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=100)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# SORT tracker initialization
tracker = Sort()

# Define line positions
enter_line_y = 600  # Vehicles coming in
leave_line_y = 500  # Vehicles leaving (IGNORE)
offset = 10  # Tolerance range

# Track counted vehicles to avoid double counting
counted_vehicles = set()
vehicle_count = 0

# Minimum object size to be considered a vehicle
min_contour_width = 40
min_contour_height = 40

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Background subtraction and noise reduction
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    # Find contours of moving objects
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    detections = []  # Store bounding boxes for SORT
    
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w >= min_contour_width and h >= min_contour_height:
            detections.append([x, y, x + w, y + h, 1])  # (x1, y1, x2, y2, confidence=1)

    # Convert detections to numpy array
    detections = np.array(detections) if detections else np.empty((0, 5))

    # Update SORT tracker
    tracked_objects = tracker.update(detections)

    # Process tracked objects
    for obj in tracked_objects:
        x1, y1, x2, y2, track_id = map(int, obj)  # Extract coordinates and ID
        center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2

        # Check if vehicle crosses the entry line
        if enter_line_y - offset < center_y < enter_line_y + offset:
            if track_id not in counted_vehicles:  # Prevent double counting
                counted_vehicles.add(track_id)
                vehicle_count += 1  # Increment count when a vehicle crosses

        # Draw tracking box and ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Draw counting lines
    cv2.line(frame, (0, enter_line_y), (frame.shape[1], enter_line_y), (0, 255, 0), 2)

    # Display vehicle count at the **top-right corner**
    cv2.putText(frame, f'Incoming Vehicles: {vehicle_count}', 
                (frame.shape[1] - 350, 50),  # Adjust position for top-right corner
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show output frame
    cv2.imshow('Vehicle Counter', frame)

    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
