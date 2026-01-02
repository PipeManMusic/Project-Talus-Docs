
# 3. Electronics Architecture (Bronco OS)
* **Architecture:** Dual-Node Compute + Distributed ESP32 I/O.
* **Network:** CAN Bus 2.0B (500kbps) on Twisted Pair (Green/Yellow).

## Compute Nodes
* **Cluster (Dash):** Pi 4 + CarPiHat + 12.3" Wisecoco Bar Display.
    * *Repo:* `github.com/PipeManMusic/BroncoIIDash`
    * *Stack:* **Python 3 + PySide6 (Qt Quick/QML)**.
    * *Data:* Direct CAN decode via `can_decoder.py`.
* **Infotainment (Center):** Pi 5 + Touchscreen.
    * *Repo:* `github.com/PipeManMusic/BroncoII-Infotainment`
    * *Stack:* **Python 3 + PySide6 (Qt Quick/QML)**.
    * *Function:* Media, Nav, System Config, Manual Viewer.
    * *Storage:* Industrial USB Hub in "Tech Bay" (Glovebox).

## Distributed I/O Nodes
* **Node A (Engine):** ESP32. Lights, Horn, Hood.
* **Node B (Dash):** ESP32 + MCP23017 + AD5206.
    * **Layout:** Landscape orientation; Deutsch connectors North/South.
    * **Isolation:** 2.5mm physical "Moat" (Keepout) between GND_LOGIC and GND_FIELD.
    * **GPIO 27:** Dedicated Backlight PWM for Wisecoco Driver.
* **Node C (Rear):** ESP32 + ADS1115. Fuel Level, Lights, Pump.

## Navigation Strategy (Native)
* **Engine:** MapLibre Native for Qt.
* **Data Source:** OpenStreetMap (OSM) vector tiles.
* **Offline Capability:** Local `.mbtiles` storage on the Pi 5 SSD.
* **Aesthetic:** Custom Mapbox Studio JSON style designed to match 1989 "Retro-Mod" color palette.

## Development Philosophy: The "Mule" Phase
* **Current Priority:** Hardware abstraction and functional logic (Radio tuning, CAN data parsing, Video piping).
* **UI Strategy:** Modular "Mule Tabs" in QML. High-fidelity UI (based on original 1989 Ford stereo buttons) is deferred until all "moving parts" are verified functional.
