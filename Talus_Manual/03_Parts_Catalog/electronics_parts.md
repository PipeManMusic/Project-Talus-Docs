# Electronics Parts Catalog

## Displays
### Primary Cluster (Dash)
* **Model:** Wisecoco / HannStar HSD123KPW1-A30
* **Specs:** 12.3 inch, 1920x720, 1000 nits.
* **Driver Board Voltage:** 12V DC (Terminal 15).
* **RPi Config:**
  ```bash
  hdmi_group=2
  hdmi_mode=87
  hdmi_cvt=1920 720 60 6 0 0 0
  hdmi_drive=2
  ```
* **Backlight Hack:** Connect ESP32 GPIO 27 to "ADJ" pin on driver board. Remove 0-ohm jumper if needed.

## Compute Modules
* **Cluster Node:** Raspberry Pi 4 (4GB) + CarPiHat
* **Infotainment:** Raspberry Pi 5 (16GB)
* **Microcontrollers:** ESP32-WROOM-32 (DevKit V1)

## Sensors
* **ABS Module:** BMW MK60E5 (E90 3-Series) - Part: 3451-6777158
