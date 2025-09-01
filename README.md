# YouTube Downloader

A simple and elegant desktop application for downloading YouTube videos and audio, built with Python and CustomTkinter.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)

## 🚀 Features

- **Modern GUI** with CustomTkinter
- **Video download** in highest available quality (MP4)
- **Audio-only download** for creating audio files
- **Real-time progress bar** during downloads
- **Custom folder selector** for download location
- **Robust error handling**
- **Spanish interface** (can be easily modified)

## 📋 Requirements

- Python 3.7 or higher
- Required Python libraries:
  - `customtkinter`
  - `pytube`
  - `tkinter` (included with Python)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/danielsm107/YOUTUBE-DOWNLOADER.git
   cd YOUTUBE-DOWNLOADER
   ```

2. **Install dependencies:**
   ```bash
   pip install customtkinter pytube
   ```

3. **Run the application:**
   ```bash
   python Youtube_Downloader.py
   ```

## 🎯 Usage

1. **Launch the application** by double-clicking `Youtube_Downloader.py` or running from terminal
2. **Enter the YouTube URL** in the text field
3. **Select download folder** where you want to save the file (optional)
4. **Choose download type:**
   - **"Descargar" (Download)**: Downloads the complete video in MP4 format
   - **"Descargar audio" (Download Audio)**: Downloads only the audio from the video
5. **Monitor progress** with the real-time progress bar
6. **Done!** The file will be saved to your selected folder

## 📁 Project Structure

```
YOUTUBE_DOWNLOADER/
│
├── Youtube_Downloader.py      # Main application file
├── Youtube_Downloader.spec    # PyInstaller configuration file
├── .gitignore                 # Git ignored files
├── README.md                  # This file
├── build/                     # Build files
└── dist/                      # Compiled executable
```

## 🔧 Building Executable

The project includes files to create a standalone executable:

```bash
pyinstaller Youtube_Downloader.spec
```

The executable will be generated in the `dist/` folder.

## 🌟 Technical Features

- **Modern GUI**: Uses CustomTkinter for a modern and responsive interface
- **Efficient downloading**: Uses pytube to access YouTube streams
- **Real-time progress**: Progress callback that updates the interface
- **Quality management**: Automatically selects the highest available quality
- **Error handling**: Captures and displays errors in a user-friendly way

## 🐛 Troubleshooting

### Download Error
- Verify that the YouTube URL is valid
- Make sure you have an internet connection
- Some videos may be geographically restricted

### Application Won't Start
- Verify you have Python 3.7+ installed
- Install all required dependencies
- Run from terminal to see specific errors

## 🤝 Contributing

Contributions are welcome! For major changes:

1. Fork the project
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## ⚠️ Disclaimer

This tool is for educational and personal use only. Please respect YouTube's terms of service and copyright laws in your country. The author is not responsible for misuse of this application.

## 🙋‍♂️ Author

**Daniel SM** - [danielsm107](https://github.com/danielsm107)

---

⭐ Don't forget to star the project if you found it useful!
