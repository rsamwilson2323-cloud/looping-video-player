import cv2
import tkinter as tk
from tkinter import filedialog

# Hide Tkinter window
root = tk.Tk()
root.withdraw()

# Select video
video_path = filedialog.askopenfilename(
    title="Select Video",
    filetypes=[
        ("Video Files", "*.mp4 *.avi *.mkv *.mov *.wmv *.flv"),
        ("All Files", "*.*")
    ]
)

if not video_path:
    print("No video selected.")
    exit()

# Create fullscreen window
window_name = "FULLSCREEN VIDEO"

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(
    window_name,
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

while True:

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        break

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow(window_name, frame)

        # Press Q or ESC to exit
        key = cv2.waitKey(25) & 0xFF

        if key == ord('q') or key == 27:
            cap.release()
            cv2.destroyAllWindows()
            exit()

    cap.release()

cv2.destroyAllWindows()
