
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
* **Hardware:** Pi 5.
* **Stack:** Python 3 + PySide6 (Qt).
* **Core:** `can_manager.py` (SocketCAN), `media_manager.py` (DBus/MPRIS).

### 3. Instrument Cluster (`BroncoIIDash`)
* **Repo:** `github.com/PipeManMusic/BroncoIIDash`
* **Hardware:** Pi 4 (CarPiHat).
* **Stack:** Python 3 + PySide6 (Qt).
* **Core:** `can_decoder.py`, `dashboard.qml`.
* **Features:** Switchable Layouts (Sport/Zen), Custom SVG Status Doll.
