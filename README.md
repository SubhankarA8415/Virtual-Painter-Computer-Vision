# Virtual Air Painter 🎨✋

A **real-time virtual air drawing application** using hand gestures. Users can draw on the screen without touching anything — simply by moving their fingers in front of a webcam.  
This project leverages **OpenCV** and **MediaPipe** for hand tracking and gesture recognition.

---

## 🚀 Features

- **Air Drawing:** Draw on the screen using the index finger.  
- **Color Selection:** Switch between multiple colors using gesture-based selection.  
- **Eraser Tool:** Erase drawings using a virtual eraser.  
- **Header Toolbar:** Visual toolbar showing available colors and tools.  
- **Real-time Hand Tracking:** Smooth and accurate hand and gesture detection.  
- **Touchless Interaction:** Fully gesture-based, no physical input required.

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV** – Webcam input, image processing, drawing  
- **MediaPipe** – Hand tracking & gesture recognition  
- **NumPy** – Matrix and image operations  

---

## 🔍 How It Works

1. **Hand Detection:**  
   MediaPipe Hand module detects & tracks 21 hand landmarks.

2. **Finger Identification:**  
   The system checks which fingers are up to determine modes:
   - ✌️ **Selection Mode:** Two fingers up → choose color/tool  
   - ☝️ **Drawing Mode:** Only index finger up → draw  

3. **Canvas Merge:**  
   The drawn strokes are merged with the webcam feed live.

4. **Header Overlay:**  
   A top toolbar displays available tools/colors for selection.

---

## 🔮 Future Improvements

- Add more colors and brush sizes  
- Add undo/redo functionality  
- Auto-save drawings as images  
- Multi-hand drawing support  

---

## 📞 Contact

**Subhankar Pandit**  
**Full Stack Developer | Backend Engineer | AI/ML | Cloud**  
**GitHub**: https://github.com/SubhankarA8415  
**LinkedIn**: https://linkedin.com/in/subhankar-pandit   

