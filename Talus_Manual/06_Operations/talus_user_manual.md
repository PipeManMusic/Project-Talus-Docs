# Project Talus: Owner's Operating Handbook
**Vehicle:** 1988 Ford Bronco II "SVT Restomod"
**VIN:** [Insert VIN]
**Engine:** 5.0L Windsor V8 (Explorer) | **ECU:** MS3Pro Ultimate
**Electrical System:** 12V Distributed CAN Bus

---

## 1. Quick Start Guide
### Normal Startup Procedure
1.  **Master Power:** Ensure the **Battery Cutoff Switch** (if equipped) is ON.
2.  **Ignition:** Turn key to **RUN** position.
    * *Check:* Listen for Fuel Pump prime (2 seconds) from the rear.
    * *Check:* Digital Dash should boot to "Gauge Cluster" screen.
3.  **Start:** Turn key to **START**.
    * *Note:* The MS3Pro handles idle air. Do not touch the throttle pedal while cranking.
4.  **Warm Up:** Allow oil pressure to stabilize (>20 psi) before driving.

### Emergency Shutdown
* **In case of Electrical Fire/Runaway:** Pull the **Main Battery Disconnect** (Location: Driver Seat Base / Under Hood).
* **Engine Kill:** The Ignition Key kills power to the **MS3Pro** and **Node A** (Ignition/Injectors).

---

## 2. Driver Controls (The "Nervous System")
*This vehicle uses digital switching. There are no direct wires from switches to lights.*

### Center Stack Controls (Node B)
| Control | Action | Function |
| :--- | :--- | :--- |
| **Knob 1 (Left)** | Rotate | Headlight Mode: OFF -> DRL -> LOW -> HIGH |
| **Knob 1 (Left)** | Push | Flash-to-Pass (High Beams) |
| **Knob 2 (Right)** | Rotate | Wiper Speed: OFF -> INT -> LO -> HI |
| **Knob 2 (Right)** | Push | Wash / Wipe Cycle |
| **Switch Bank** | Toggle 1 | Hazard Lights |
| **Switch Bank** | Toggle 2 | Aux Lights (Bumper) |
| **Switch Bank** | Toggle 3 | Winch Power Arm (Requires Key ON) |

### Digital Dash Interface
* **Screen 1 (Gauge Cluster):** Speed, RPM, Coolant Temp, Oil Pres, Fuel Lvl.
* **Screen 2 (Diagnostics):** Real-time CAN status.
    * *Green Dot:* Node Online.
    * *Red Dot:* Node Offline (Check Fuses).
* **Screen 3 (Manuals):** Displays the "Talus Knowledge Base" (See Section 6).

---

## 3. Maintenance & Fluid Specs
*Use only specified fluids. The 5.0L and TTB are sensitive to incorrect oils.*

### Engine (5.0L Windsor)
* **Oil:** 5W-30 Synthetic (Capacity: ~6 Quarts w/ Dual Sump Pan).
* **Filter:** Motorcraft FL-820S (or equivalent).
* **Coolant:** Green (Ethylene Glycol) - 50/50 Mix.
* **Spark Plugs:** Motorcraft SP-432 (Gap: .054").

### Drivetrain
* **Transmission (M5OD-R2):** Mercon V ATF. *Do not use Gear Oil.*
* **Transfer Case (Atlas II):** Amsoil 75W-90 GL-4.
* **Front Diff (Dana 35):** 80W-90 Gear Oil.
* **Rear Diff (Ford 8.8):** 75W-140 Synthetic (Requires Friction Modifier if Limited Slip).

---

## 4. Electrical Troubleshooting
*The truck uses 3 Custom "Talus Nodes" instead of a fuse box.*

### "The Truck Won't Start"
1.  **Check Battery Voltage:** Dash should read >12.0V.
2.  **Check Main Fuse:** Inspect the **200A AMG Fuse** on the inner fender (near Battery).
3.  **Check MS3Pro:** Is the ECU LED green? (Located in Glovebox/Kickpanel).

### "A Light Isn't Working"
1.  **Check the Node LEDs:** Look at the custom PCB (Clear cover).
    * *LED ON:* The ESP32 is trying to turn the output ON. (Issue is wiring/bulb).
    * *LED OFF:* The ESP32 is not receiving the command. (Issue is CAN Bus or Switch).
2.  **Reboot:** Cycle Master Power to reset the electronic fuses.

### Jump Starting
* **WARNING:** This vehicle has a **180A High-Output Alternator** and sensitive electronics.
* **Procedure:** Connect cables. Wait 5 minutes. Crank.
* **Do NOT** rev the donor car while cranking Talus (Risk of voltage spike).

---

## 5. Towing & Recovery
* **Tow Points:** Use the **Shackle Mounts** on the Plate Bumpers. Do not hook to suspension.
* **Flat Towing:**
    * **Transmission:** NEUTRAL.
    * **Transfer Case:** NEUTRAL.
    * *Note:* Unlock front hubs to save wear.

---

## 6. The "Talus Knowledge Base" App
*Accessed via the "DOCS" tab on the central display.*

### Features
* **Live Specs:** Displays the current configuration (Pinouts, Part Numbers, Fluid Capacities).
* **Search:** Find "Fuse" or "Oil" instantly.
* **Mechanic Mode (Export):**
    1.  Connect the truck to Wi-Fi (or Phone Hotspot).
    2.  Navigate to the relevant section (e.g., "Electrical Architecture").
    3.  Press **"EMAIL TO TECH"**.
    4.  Enter the recipient's email.
    5.  *Result:* The system generates a PDF of the current specs and emails it instantly.

---
**Keep this file updated as you finish the build.**