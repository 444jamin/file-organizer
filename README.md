📂 File Organizer (Python)
A simple file organizer script written in Python using os, shutil, and watchdog.

🔧 Features:
Automatically sorts files into folders by type:
- 📷 Images
- 🎵 Audio (including SFX)
- 🎬 Videos
- 📄 Documents
- Monitors a specified folder and reacts instantly when files are dropped in.
- Supports a wide variety of file extensions for each type.

⚙️ How it works:
Once the script is running, any file dropped into the monitored folder is automatically moved to its designated destination folder based on its extension.

⚠️ Notes:
- The script must be running in the background to work.
- Currently uses a polling observer for compatibility with WSL and Windows folders.
- Can be optimized further to run as a background service or tray app.
- Requires --pip install watchdog (or pip3) to set up watchdog