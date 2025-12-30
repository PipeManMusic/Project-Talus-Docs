
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
    * *Specifics:* Controls Vintage Air (Drive-by-Wire), Reads Steering Buttons.
    * *GPIO 27:* Reserved for Screen Backlight PWM.
* **Node C (Rear):** ESP32 + ADS1115. Fuel Level, Lights, Pump.
