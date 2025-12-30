
# 5. Development Environment & Workflow

* **Host Machine:** Ubuntu Linux Laptop.
* **IDE:** Visual Studio Code (VS Code).
* **Connection Method:** VS Code "Remote - SSH" Extension.
* **Version Control:** Git / GitHub.

## Repository Structure

### 1. Documentation (`Project-Talus-Docs`)
* **Repo:** `github.com/PipeManMusic/Project-Talus-Docs` (Private)
* **Purpose:** The "Digital Glovebox."

### 2. Infotainment System (`BroncoII-Infotainment`)
* **Repo:** `github.com/PipeManMusic/BroncoII-Infotainment` (Public)
* **Target Hardware:** Raspberry Pi 5.
* **Architecture:** Python 3 + Qt Quick (QML).
    * **Language:** Python 3.11+
    * **UI Framework:** PySide6 (Qt for Python).
    * **Key Files:**
        * `main.py`: App Entry Point. Bootstraps QML engine.
        * `ui/*.qml`: UI Layouts (Infotainment.qml, MediaTab.qml).
        * `lib/can_manager.py`: SocketCAN interface.
        * `lib/media_manager.py`: DBus/MPRIS Media control.
        * `lib/bluetooth_manager.py`: BlueZ Phone pairing.

### 3. Instrument Cluster (`BroncoIIDash`)
* **Repo:** `github.com/PipeManMusic/BroncoIIDash`
* **Target Hardware:** Raspberry Pi 4.
* **Engine:** Godot Game Engine (Exported to Linux/X11).
