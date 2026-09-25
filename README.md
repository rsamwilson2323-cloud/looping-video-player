# 🎬 Looping Video Player

> A simple fullscreen Python video player that allows users to select a video from their PC and play it continuously in an automatic loop.

**Looping Video Player** is a lightweight Windows-based Python application built using **OpenCV** and **Tkinter**. It allows users to select a video file from anywhere on their computer and automatically play the video in fullscreen mode.

When the video reaches the end, it automatically starts again from the beginning, making it useful for **events, exhibitions, college symposiums, digital signage, presentations, kiosks, and continuous display systems**.

---

# ✨ Features

* 🎬 Video file selection from anywhere on the PC
* 📂 Windows file selection dialog
* 🖥️ Fullscreen video playback
* 🔄 Automatic infinite video looping
* ▶️ Smooth continuous playback
* 🎯 Supports multiple common video formats
* ⌨️ Press `Q` to exit
* ⎋ Press `ESC` to exit
* ⚡ Lightweight and fast
* 🪟 Designed for Windows
* 🐍 Built with Python
* 🔒 Runs completely locally
* 🚫 No internet connection required
* 🚫 No external media player required

---

# 🖥️ Tech Stack

### Programming Language

* Python 3.9+

### Libraries

* OpenCV
* Tkinter

### Video Processing

* OpenCV VideoCapture
* OpenCV video frame rendering
* Automatic video restart
* Fullscreen window management

### User Interface

* Tkinter file dialog
* OpenCV fullscreen window

---

# 🚀 Project Repository

View the source code on GitHub:

[Looping Video Player — GitHub Repository](https://github.com/rsamwilson2323-cloud/looping-video-player.git?utm_source=chatgpt.com)

---

# 📦 Installation

The project is designed to run easily on Windows.

### 1. Clone the repository

```bash
git clone https://github.com/rsamwilson2323-cloud/looping-video-player.git
```

### 2. Go into the project folder

```bash
cd looping-video-player
```

### 3. Install OpenCV

For Python 3.9:

```bash
python -m pip install opencv-python
```

Tkinter is normally included with standard Python installations on Windows.

---

# ▶️ Run the Application

Start the program using:

```bash
python "looping video player.py"
```

The application will open a file-selection window.

---

# 📂 Select a Video

When the application starts, a Windows file picker will appear.

```text
Select a Video
       ↓
Browse your PC
       ↓
Select Video
       ↓
Open
       ↓
Fullscreen Playback
```

You can select a video from any folder on your computer.

---

# 🎬 Supported Video Formats

The application is configured to support common video formats including:

```text
.mp4
.avi
.mkv
.mov
.wmv
.flv
```

Support for individual formats may depend on the video codecs available to OpenCV on the system.

---

# 🖥️ Fullscreen Playback

After selecting the video, the player automatically opens the video in **fullscreen mode**.

```text
┌───────────────────────────────────────────────┐
│                                               │
│                                               │
│                 YOUR VIDEO                    │
│                                               │
│                                               │
│                                               │
└───────────────────────────────────────────────┘
```

The application is suitable for displaying videos on:

* 🖥️ Computer monitors
* 📺 TVs
* 📽️ Projectors
* 🏫 College event displays
* 🏢 Digital signage screens
* 🎪 Exhibition displays

---

# 🔄 Automatic Looping

The main feature of the project is continuous playback.

```text
       ┌───────────────┐
       │   Select      │
       │    Video      │
       └───────┬───────┘
               ↓
       ┌───────────────┐
       │    Play       │
       │    Video      │
       └───────┬───────┘
               ↓
       ┌───────────────┐
       │ Video Ends    │
       └───────┬───────┘
               ↓
       ┌───────────────┐
       │ Restart Video │
       └───────┬───────┘
               │
               └──────────────→ LOOP
```

The video automatically restarts when playback reaches the end.

There is no need to manually restart the video.

---

# ⌨️ Keyboard Controls

| Key   | Action                 |
| ----- | ---------------------- |
| `Q`   | Exit the application   |
| `ESC` | Exit fullscreen/player |

---

# 🧠 How It Works

The application follows a simple workflow:

```text
Start Application
       ↓
Open File Dialog
       ↓
Select Video
       ↓
Open Video with OpenCV
       ↓
Create Fullscreen Window
       ↓
Read Video Frames
       ↓
Display Frames
       ↓
Video Ends
       ↓
Release Video
       ↓
Open Video Again
       ↓
Continue Looping
```

---

# 🧩 Core Components

### 📂 Tkinter File Dialog

Tkinter is used to open the Windows file-selection dialog.

It allows the user to browse the computer and select the desired video.

### 🎥 OpenCV VideoCapture

OpenCV handles video loading and frame-by-frame playback.

```python
cap = cv2.VideoCapture(video_path)
```

### 🖥️ Fullscreen Window

OpenCV's window properties are used to display the video in fullscreen mode.

```python
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

cv2.setWindowProperty(
    window_name,
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)
```

### 🔄 Loop Controller

When the video reaches the end, the video capture is released and opened again.

This creates continuous playback.

---

# 📁 Project Structure

```text
looping-video-player/
│
├── looping video player.py
│
├── README.md
│
└── LICENSE
```

---

# ⚡ Lightweight Design

The project intentionally keeps the architecture simple.

It does not require:

* ❌ Database
* ❌ Web server
* ❌ Cloud services
* ❌ Internet connection
* ❌ Browser
* ❌ External media player
* ❌ Complex configuration

Everything runs locally on the computer.

---

# 🔒 Privacy

The application works completely locally.

The selected video is **not uploaded to a server**.

```text
Your PC
   ↓
Select Video
   ↓
OpenCV
   ↓
Local Playback
   ↓
Fullscreen Display
```

No video data needs to leave the computer.

---

# 🎯 Use Cases

Looping Video Player can be useful for:

* 🎓 College symposiums
* 🏫 College events
* 🎪 Exhibitions
* 🧪 Science exhibitions
* 💻 Project demonstrations
* 🏢 Digital signage
* 📺 Continuous display screens
* 🎤 Conferences
* 🖼️ Art exhibitions
* 🛍️ Promotional displays
* 🏆 Hackathons
* 🚀 Product demonstrations
* 📽️ Projector presentations
* 🏛️ Reception displays

---

# 🧪 Example Usage

Suppose you have a college event video:

```text
AI_ML_TITANS_INTRO.mp4
```

Start the application:

```bash
python "looping video player.py"
```

Select:

```text
AI_ML_TITANS_INTRO.mp4
```

The application will display:

```text
AI_ML_TITANS_INTRO.mp4
        ↓
      PLAY
        ↓
      END
        ↓
      PLAY
        ↓
      END
        ↓
      PLAY
        ↓
     ∞ LOOP
```

This is especially useful when a video needs to be displayed continuously during an event.

---

# 🛠️ Requirements

### Operating System

```text
Windows 10
Windows 11
```

### Python

```text
Python 3.9+
```

### Required Package

```text
opencv-python
```

Install using:

```bash
python -m pip install opencv-python
```

---

# 🔧 Troubleshooting

### Video does not open

Make sure the selected video is valid and supported by your OpenCV installation.

Try using an `.mp4` video encoded with a commonly supported codec.

### OpenCV is not installed

Run:

```bash
python -m pip install opencv-python
```

### Python is not recognized

Verify your Python installation:

```bash
python --version
```

Expected output:

```text
Python 3.9.13
```

---

# 🔮 Future Improvements

Possible future enhancements include:

* 🎚️ Volume control
* ⏯️ Play/Pause controls
* ⏭️ Next/Previous video
* 📁 Playlist support
* 🔀 Random video playback
* 🖥️ Multi-monitor support
* 🎞️ Multiple video looping
* 🖱️ Automatic cursor hiding
* 🔇 Mute option
* ⏱️ Scheduled playback
* 📺 Automatic screen resolution detection
* 🖼️ Better aspect-ratio handling
* 🏷️ Custom event branding
* ⚙️ Configuration settings
* 🚀 Windows startup support
* 📦 Standalone `.exe` version

---

# 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

Create your own fork of the project.

### 2. Create a feature branch

```bash
git checkout -b feature/amazing-feature
```

### 3. Make your changes

Improve the player, UI, playback system, or documentation.

### 4. Commit your changes

```bash
git commit -m "Add amazing feature"
```

### 5. Push your branch

```bash
git push origin feature/amazing-feature
```

### 6. Open a Pull Request

Submit your changes for review.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

# ⭐ Show Your Support

If you like **Looping Video Player**:

⭐ Star the repository

🍴 Fork the project

🐞 Report bugs

💡 Suggest improvements

🚀 Contribute features

📢 Share the project

---

# 👨‍💻 Author

**Sam Wilson**

AI & Full Stack Developer

Interested in:

* 🤖 Artificial Intelligence
* 🧠 Machine Learning
* 👁️ Computer Vision
* 🌐 Web Development
* 🎨 UI/UX Design
* 💻 Creative Coding
* ⚙️ Automation

---

# 🖥️ Made With

**Python + OpenCV + Tkinter**

Built with ❤️, ⚡ and Python.

