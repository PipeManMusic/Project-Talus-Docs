#!/bin/bash

# Project Talus - Manual Setup Script
# Creates the directory structure and populates stub files with Bible data.

ROOT_DIR="Talus_Manual"

echo "Creating Project Talus Digital Manual Structure..."

# 1. Create Directory Hierarchy
mkdir -p "$ROOT_DIR/01_Quick_Reference"
mkdir -p "$ROOT_DIR/02_Wiring_Diagrams"
mkdir -p "$ROOT_DIR/03_Parts_Catalog"
mkdir -p "$ROOT_DIR/04_Troubleshooting"
mkdir -p "$ROOT_DIR/assets" # For images/pdfs

# ---------------------------------------------------------
# 2. Populate "01_Quick_Reference"
# ---------------------------------------------------------

cat <<EOF > "$ROOT_DIR/01_Quick_Reference/starting_procedure.md"
# Starting Procedure
* **System:** Project Talus (Bronco OS)
* **Engine:** 5.0L Ford V8 (MegaSquirt 3)

## Standard Start
1. Ensure Gear is in **Neutral**.
2. Turn Ignition Switch to **ON** (Red LED on Node B).
3. Wait 2 seconds for Fuel Pump prime (Listen for whine from rear).
4. Press **Start Button**.

## Limp Mode / Flood Clear
* If engine is flooded, hold throttle 100% open while cranking (Flood Clear Mode).
EOF

cat <<EOF > "$ROOT_DIR/01_Quick_Reference/fluids_and_capacities.md"
# Fluids & Capacities

| Component | Fluid Type | Capacity | Notes |
| :--- | :--- | :--- | :--- |
| **Engine Oil** | 5W-30 Synthetic | 5.0 Quarts | Ford Explorer 5.0L Spec |
| **Transmission** | Mercon V ATF | 2.8 Quarts | Mazda M5OD-R2 (Yes, it uses ATF) |
| **Transfer Case** | Amsoil Syncromesh | 2.0 Quarts | Atlas II Spec |
| **Front Diff** | 80W-90 Gear Oil | ~3.5 Pints | Dana 35 TTB |
| **Rear Diff** | 75W-140 Synthetic | ~5.5 Pints | Ford 8.8 (Requires Friction Modifier if Clutch LSD) |
| **Coolant** | Green (Ethylene Glycol) | ~12 Quarts | Vintage Air requires 50/50 mix |
EOF

# ---------------------------------------------------------
# 3. Populate "02_Wiring_Diagrams"
# ---------------------------------------------------------

cat <<EOF > "$ROOT_DIR/02_Wiring_Diagrams/wiring_standards.md"
# Wiring Standards (DIN 72551)

**CRITICAL WARNING:**
* **BROWN** is Ground (31).
* **BLACK** is Ignition Power (15).
* Do not confuse with US Ford standards!

## Color Code Key
| Function | Terminal | Color | Code | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Battery Constant** | 30 | Red | RD | Always Hot |
| **Ignition Switched** | 15 | Black | BK | Hot in Run/Start |
| **Chassis Ground** | 31 | Brown | BN | Main Ground Points |
| **Illumination** | 58 | Grey | GY | Dash/Running Lights |
| **High Beam** | 56a | White | WH | |
| **Low Beam** | 56b | Yellow | YE | |
| **Turn Left** | L | Black/White | BK/WH | |
| **Turn Right** | R | Black/Green | BK/GN | |
| **CAN High** | -- | Green | GN | Twisted Pair |
| **CAN Low** | -- | Yellow | YE | Twisted Pair |
| **5V Ref** | -- | Orange | OR | Sensors |
| **Signal Return** | -- | Blue | BU | Sensors |

## Connector Standard
* **External/Weather:** Deutsch DT / DTM Series
* **Internal:** Molex Mini-Fit Jr (or OEM Ford)
* **Labels:** Printed Heat Shrink on BOTH ends.
EOF

# Create placeholder binary files for diagrams
touch "$ROOT_DIR/02_Wiring_Diagrams/00_System_Overview.pdf"
touch "$ROOT_DIR/02_Wiring_Diagrams/01_Node_A_Front.pdf"
touch "$ROOT_DIR/02_Wiring_Diagrams/02_Node_B_Dash.pdf"
touch "$ROOT_DIR/02_Wiring_Diagrams/03_Node_C_Rear.pdf"

# ---------------------------------------------------------
# 4. Populate "03_Parts_Catalog"
# ---------------------------------------------------------

cat <<EOF > "$ROOT_DIR/03_Parts_Catalog/electronics_parts.md"
# Electronics Parts Catalog

## Displays
### Primary Cluster (Dash)
* **Model:** Wisecoco / HannStar HSD123KPW1-A30
* **Specs:** 12.3 inch, 1920x720, 1000 nits.
* **Driver Board Voltage:** 12V DC (Terminal 15).
* **RPi Config:**
  \`\`\`bash
  hdmi_group=2
  hdmi_mode=87
  hdmi_cvt=1920 720 60 6 0 0 0
  hdmi_drive=2
  \`\`\`
* **Backlight Hack:** Connect ESP32 GPIO 27 to "ADJ" pin on driver board. Remove 0-ohm jumper if needed.

## Compute Modules
* **Cluster Node:** Raspberry Pi 4 (4GB) + CarPiHat
* **Infotainment:** Raspberry Pi 5 (16GB)
* **Microcontrollers:** ESP32-WROOM-32 (DevKit V1)

## Sensors
* **ABS Module:** BMW MK60E5 (E90 3-Series) - Part: 3451-6777158
EOF

cat <<EOF > "$ROOT_DIR/03_Parts_Catalog/mechanical_parts.md"
# Mechanical Parts Catalog

## Powertrain
* **Engine:** 5.0L Ford Windsor V8 (1996-2001 Ford Explorer basis)
* **Belt:** Serpentine (Explorer Front Dress) - Part: [TBD]
* **Transmission:** Mazda M5OD-R2 (Manual 5-Speed)
* **Transfer Case:** Advance Adapters Atlas II (Twin Stick)

## Suspension & Axles
* **Front Axle:** Dana 35 TTB (Reverse Rotation)
* **Front Knuckles:** 1993-1994 Ford Explorer (ABS Sensor Mounts)
* **Rear Axle:** Ford 8.8 (Disc Brake, 31 Spline)
* **Lift Kit:** James Duff "Stage 3" (Variable Rate Springs, Long Arms)

## Steering
* **Column:** 1998-2003 Ford Ranger (Manual/Floor Shift)
* **Wheel:** 2000s Lincoln Navigator (Wood/Leather)
EOF

# ---------------------------------------------------------
# 5. Populate "04_Troubleshooting"
# ---------------------------------------------------------

cat <<EOF > "$ROOT_DIR/04_Troubleshooting/boot_logs.md"
# Boot Logs & Debugging

## Accessing Logs
* **Cluster Node:** \`ssh pi@192.168.1.10\` -> \`journalctl -u bronco-dash.service\`
* **Infotainment:** \`ssh pi@192.168.1.11\` -> \`pm2 logs\`

## Common Issues
* **Screen Black:** Check HDMI timings in /boot/config.txt
* **No Start:** Check Node B "Ignition" LED status.
EOF

echo "Done! 'Talus_Manual' created with Version 1.3 data."
echo "Location: $(pwd)/$ROOT_DIR"