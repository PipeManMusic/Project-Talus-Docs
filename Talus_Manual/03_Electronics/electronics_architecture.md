
# 3. Electronics Architecture (Bronco OS)
* **Architecture:** Dual-Node Compute + Distributed ESP32 I/O.
* **Network:** CAN Bus 2.0B (500kbps) on Twisted Pair (Green/Yellow).

## Compute Nodes
* **Cluster (Dash):** Pi 4 + CarPiHat + 12.3" Wisecoco Bar Display (1920x720).
    * *Repo:* `github.com/PipeManMusic/BroncoIIDash`
* **Infotainment (Center):** Pi 5 + Touchscreen [TBD].
    * *Function:* Media, Nav, "Digital Owner's Manual" Host.

## Distributed I/O Nodes
* **Node A (Engine):** ESP32. Lights, Horn, Hood.
* **Node B (Dash):** ESP32 + MCP23017 + AD5206.
    * *Specifics:* Controls Vintage Air (Drive-by-Wire), Reads Steering Buttons.
    * *GPIO 27:* Reserved for Screen Backlight PWM.
* **Node C (Rear):** ESP32 + ADS1115. Fuel Level, Lights, Pump.
