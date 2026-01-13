# Navigation System Specification
**Target Hardware:** Infotainment Node (Raspberry Pi 5)
**Software Stack:** Python 3 + PySide6 (Qt) + MapLibre Native
**Design Philosophy:** "Offline First" (Desert Capable) + "Retro-Mod" (1988 Aesthetic)

---

## 1. Core Architecture
The navigation system is designed to be completely autonomous, requiring no cellular connection for tile rendering or route calculation.

### The Stack
| Component | Technology | Role |
| :--- | :--- | :--- |
| **Renderer** | `MapLibre Native` (Qt Bindings) | Draws vector tiles at 60fps using OpenGL. |
| **Data Source** | OpenStreetMap (OSM) Vector Tiles | The "World" data stored locally. |
| **Routing Engine** | Valhalla (Docker) *or* OSRM | Calculates paths (A to B) locally. |
| **Positioning** | `gpsd` (via USB or CAN) | Provides Lat/Lon/Head/Speed to Qt. |

---

## 2. Data Pipeline (The "Atlas" Workflow)
Since we cannot stream tiles from the web, the map data must be "baked" into a single file before the vehicle leaves the garage.

### Tile Generation Strategy
* **Tool:** `Planetiler` (Java-based, high performance).
* **Source:** Geofabrik (`north-america-latest.osm.pbf`).
* **Output:** `.mbtiles` (SQLite container).
* **Storage Location:** `/opt/talus/maps/bronco_world.mbtiles` (on NVMe SSD).

### Workflow Step-by-Step
1.  **Download:** Fetch latest `.osm.pbf` region file on Host PC.
2.  **Crunch:** Run Planetiler to generate vector tiles (Zoom 0-14).
3.  **Transfer:** `rsync` the `.mbtiles` file to the Pi 5 NVMe drive.
4.  **Serve:** MapLibre reads directly from the SQLite container (no local HTTP server required for rendering).

---

## 3. Routing Engine (Navigation)
MapLibre draws the map, but it does not know how to navigate it. We utilize a separate local service for routing.

### Selected Engine: Valhalla
* **Why:** optimized for offline use, supports "multimodal" routing (e.g., ignoring highways), and runs well in a Docker container on ARM64.
* **Implementation:**
    * Pi 5 runs Valhalla in a Docker container exposing port `8002`.
    * **Request:** Python backend sends HTTP GET `localhost:8002/route?json={...}`.
    * **Response:** JSON object containing the "Shape" (Polyline geometry) and "Maneuvers" (Turn-by-turn instructions).
* **Visuals:** The Python backend parses the "Shape" and draws a `MapPolyline` on the QML Map layer.

---

## 4. UI/UX Specifications ("Retro-Mod")
The UI must feel like a piece of high-end 1988 military/aviation equipment, not a modern smartphone.

### A. "Zen" Mode (Default)
* **Visuals:** Map fills 100% of the screen.
* **Overlays:** Minimal. Small "Speed" (Digital 7-segment font) and "Heading" (Compass tape) in corners.
* **Behavior:** Map auto-centers on vehicle. North-Up or Track-Up togglable via rotary knob.

### B. "Rally" Mode (Active Nav)
* **Visuals:** High-contrast topography. Route line is bright Amber or Green (CRT phosphor style).
* **Breadcrumbs:** System records path points every 5 seconds (green dots) to trace "where we've been" (crucial for backtracking in off-road scenarios).
* **Waypoints:** Physical button press drops a "Flag" on the map at current location.

### C. Controls
* **Zoom:** Physical Rotary Encoder (Tech Bay or Console).
* **Pan:** Touchscreen (Capacitive).
* **Input:** On-screen keyboard for address search (only allowed when Speed = 0).