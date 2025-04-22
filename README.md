Sure! Here’s a clean and clear `README.md` for vehicle counting script using OpenCV and the SORT tracking algorithm:

---

# Vehicle Counting System using OpenCV & SORT Tracker

This Python project uses **OpenCV** for motion detection and **SORT (Simple Online and Realtime Tracking)** to count vehicles crossing a virtual line in a video.

---

## 🚗 Features

- Background subtraction using `MOG2` for detecting moving vehicles.
- Real-time vehicle tracking using the **SORT** algorithm.
- Avoids double-counting the same vehicle.
- Live display with:
  - Tracked bounding boxes.
  - Unique vehicle IDs.
  - Total vehicle count overlay.

---

## 🧑‍💻 Requirements

- Python 3.x
- OpenCV
- NumPy
- SORT tracking module (`sort.py` must be available).

Install dependencies with:

```bash
pip install opencv-python numpy
```

---

## 📁 Project Structure

```
your_project_folder/
├── app.py                # Main vehicle counting script
├── sort/
│   └── sort.py           # SORT tracking algorithm
└── video (1).mp4         # Input video file
```

---

## ⚙️ How It Works

1. **Background Subtraction**  
   Uses `cv2.createBackgroundSubtractorMOG2()` to detect moving objects.

2. **Filtering Objects**  
   Filters objects smaller than `40x40` pixels to remove noise.

3. **Tracking**  
   Uses the SORT tracker to assign a unique ID to each vehicle.

4. **Counting Logic**  
   When a vehicle’s center crosses the entry line (`y = 600`), it increments the counter if that ID hasn’t been counted before.

---

## 🏁 Running the Script

1. Update the video path:

```python
video_source = "C:/Users/mmani/opencv/video (1).mp4"
```

2. Ensure `sort.py` is correctly imported:

```python
sys.path.append("C:/Users/mmani/opencv/sort")
from sort import Sort
```

3. Run:

```bash
python app.py
```

---

## 💡 Customization

- **Line Positioning:**  
  Change `enter_line_y` to set the counting line.

- **Object Size Threshold:**  
  Adjust `min_contour_width` and `min_contour_height` for different object sizes.

- **Video Input:**  
  Replace `video_source` with your desired video file path.

---

## ⚠️ Important

- Make sure `sort.py` is present in the specified folder.
- Avoid hardcoding sensitive paths. Use relative paths where possible.
- Test different `offset` values depending on camera angle and video stability.

---

## 📸 Sample Output

Tracked vehicles will be highlighted with bounding boxes, labeled with IDs, and the total count will be displayed at the top-right corner.

---

## 🧹 Exit

Press `Esc` key (`27`) to close the window.

---

## 📄 License

This project is for educational purposes. SORT's original license applies for the tracker code.

---

Let me know if you want me to also help draft a `requirements.txt` or a GitHub-style description!
