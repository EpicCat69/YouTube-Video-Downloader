# YouTube-Video-Downloader

A simple **YouTube video and audio downloader** with a clean **PyQt5 GUI**, powered by **yt-dlp**.  

✅ Download videos in multiple qualities (Best, 1080p, 720p)  
✅ Download audio as **MP3**  
✅ Choose download folder  
✅ Progress bar and status updates  
✅ Works on **Windows**, **macOS**, and **Linux**  

---

## 🚀 Features
- **Video Download**: Best, 1080p, 720p  
- **Audio Download**: Convert to MP3 (via FFmpeg)  
- **Progress Bar**: Live download progress  
- **Custom Save Location**: Choose any folder  
- **Threaded Downloads**: No GUI freezing  

---

## 🖥️ Screenshots
*(Add your screenshots here after running the app)*  

---

## ⚙️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/youtube-downloader-gui.git
cd youtube-downloader-gui
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
yt-dlp
PyQt5
```

### 3. Install FFmpeg (Required for MP3 conversion)

#### Windows (Winget):
```powershell
winget install ffmpeg
```

#### macOS (Homebrew):
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg
```

**Verify installation:**
```bash
ffmpeg -version
```

> ⚠ On Windows, restart PowerShell or your PC if `ffmpeg` is not recognized.

---

## ▶️ Run the App
```bash
python youtube_downloader.py
```

---

## ✅ How to Use
1. Enter a **YouTube video URL**  
2. Select **quality** (Best, 1080p, 720p, Audio MP3)  
3. Choose a **download folder**  
4. Click **Download**  
5. Wait for the progress bar to finish  

---

## 🛠 Built With
- [PyQt5](https://pypi.org/project/PyQt5/) - GUI framework  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - YouTube downloader  

---

## ⚠️ Disclaimer
This tool is for **personal use only**. Downloading videos from YouTube may violate **YouTube's Terms of Service**. Use at your own risk.
