
# Development Environment & Workflow

* **Host Machine:** Ubuntu Linux Laptop.
* **IDE:** Visual Studio Code (VS Code).
* **Connection Method:** VS Code "Remote - SSH" Extension.
* **Version Control:** Git / GitHub.

## Repository Architecture
The Project Talus ecosystem is comprised of five distinct repositories to ensure modularity and fault isolation:

1. **BroncoIIDash:** Cluster logic and gauge rendering.
2. **BroncoIIInfotainment:** Navigation, MapLibre, and Media stack.
3. **Talus_Trace:** Orthogonal A* harness generation utility.
4. **Talus_Manual:** Markdown-based technical documentation and data-store.
5. **Talus_Tally:** Standalone management engine using JSON-backed task hierarchies.

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

### 4. Progress Tracker (`Talus Tally`)
* **Purpose:** Mobile todo tracking synced to Markdown project documentation.
* **Logic:** Bi-directional sync between Android (Mobile) and GitHub (Docs).
* **Architecture:** Standalone Python (FastAPI) Backend + Android Frontend.
* **Dependency:** Divorced from vehicle hardware (Runs on Dev Workstation/Server).
* **Primary Libraries:** FastAPI, GitPython, Pydantic, Pytest.
* **Status:** TDD Phase - Task Parser & Engine.