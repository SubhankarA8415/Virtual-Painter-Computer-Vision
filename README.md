Virtual Air Painter 🎨✋
A real-time virtual air drawing application using hand gestures. Users can draw on the screen without touching anything, simply by using their fingers in front of a webcam. The project leverages OpenCV and MediaPipe for hand tracking and gesture recognition.
Features
•	Air Drawing: Draw on the screen using the index finger.
•	Color Selection: Switch between multiple colors using gesture-based selection.
•	Eraser Tool: Erase drawings with a virtual eraser.
•	Header Toolbar: Visual header showing available colors and tools.
•	Real-time Hand Tracking: Smooth and responsive tracking of hand movements.
•	No Physical Input Needed: Fully gesture-based, contactless interaction.

Technologies Used
•	Python 3
•	OpenCV – For webcam input, image processing, and drawing.
•	MediaPipe – For real-time hand tracking and gesture recognition.
•	NumPy – For matrix and image operations.

How It Works
1.	Hand Detection: The MediaPipe Hand module detects and tracks hand landmarks.
2.	Finger Identification: The application checks which fingers are up to determine the mode:
o	Selection Mode: Two fingers up → choose color/tool.
o	Drawing Mode: Only index finger up → draw on canvas.
3.	Canvas Merge: Drawings are merged with the webcam feed in real-time.
4.	Header Overlay: The top toolbar shows available tools/colors for easy selection.

Future Improvements
•	Add more colors and brush sizes.
•	Add undo/redo functionality.
•	Save drawings as images automatically.
•	Implement multi-hand drawing support.

Contact
•	Author: Subhankar Pandit
•	Email: subhankar.pandit2002@gmail.com
•	GitHub: https://github.com/SubhankarA8415
