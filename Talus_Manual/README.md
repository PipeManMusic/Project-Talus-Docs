# Project Talus: Bronco II Infotainment
**Current Phase:** Mule Build (Functionality > Aesthetics)  
**Prototyping Hardware:** Raspberry Pi 4 (Targeting Pi 5 for Production)

## 🎯 Project Vision
A 1989-themed digital dashboard for a 5.0L Swapped Bronco II. The system integrates MS3 Engine Data, MK60 ABS telemetry, and a custom "Open Source First" navigation engine, all wrapped in a skeuomorphic UI that mimics the original Ford factory stereo.

---

## 🏗️ Implementation Roadmap (Functional Gates)

### Gate 1: Hardware Finalization
- [x] **PCB Logic:** Isolated CAN & FET Drivers (Flux AI).
- [x] **Thermal Guard:** TypeScript automation for high-current traces.
- [ ] **Gerber Export:** Generate files for manufacturing.
- [ ] **BOM (Bill of Materials):** Verify availability of Murata and ISO1050 chips.
- [ ] **Touch Panel Probe:** Verify CTP USB identification on Pi 4.
- [ ] **Backlight PWM:** Confirm ESP32 GPIO 27 controls brightness via ADJ pin.

### Gate 2: Logic & Safety
- [ ] **Relay Verification:** Implement "Sense-back" logic for Mirror Heaters.
- [ ] **Fault Handling:** Define CAN "Error Frames" if feedback signal fails.
- [ ] **Current Limiting:** Logic to disable outputs if sensed current exceeds threshold.

### Gate 3: Navigation (OSM Native)
- [ ] **Local Tile Server:** Directory structure created for `.mbtiles`.
- [ ] **MapLibre Setup:** Integrate MapLibre Native into Qt/QML.
- [ ] **Retro Style:** Inject Mapbox Studio JSON (Amber/Green theme).

---

## 📦 Hardware & Budget Tracker
*Budget details are maintained in a separate spreadsheet; technical specs are tracked here.*

### In-Hand (The Bench)
| Component | Device | ID / Spec | Status |
| :--- | :--- | :--- | :--- |
| **Compute** | Raspberry Pi 4 | 8GB RAM | Active Proto |
| **Radio** | RTL-SDR Blog V4 | `0xbda:0x2838` | Handshake OK |
| **Phone** | CarlinKit CCPA | `0x1314:0x1521`| Handshake OK |
| **CAN** | USB-CAN Adapter | Ch. A (MS3) / B (MK60) | Wired |
| **Display** | 7" Touchscreen | 800x480 HDMI | Mounted |

### To Purchase (The Wishlist)
- [ ] **Raspberry Pi 5:** For production-speed vector map rendering.
- [ ] **NVMe Base:** Fast storage for 40GB+ of offline OSM tiles.
- [ ] **MCX-to-Motorola Adapter:** To bridge SDR to factory Bronco antenna.
- [ ] **12V to 5.1V Buck Converter:** Dedicated clean power for Tech Bay.

---

## 📂 Repository Map
* `/backend`: Python logic engines (CAN, Gear, Media).
* `/lib`: Hardware managers (CarPlay, SDR, GPS).
* `/ui`: QML Tab definitions (Nav, Media, Drivetrain).
* `/tests`: Unit tests for hardware handshakes and math.
* `/assets`: Fonts (`vcr.ttf`) and Inkscape UI buttons.

---

## 🚦 System Status
| Subsystem | Logic | Hardware | UI Mule |
| :--- | :--- | :--- | :--- |
| **Media** | 🟢 Ready | 🟢 Active | 🟢 Ready |
| **Drivetrain**| 🟡 Testing | 🟢 Active | 🟢 Ready |
| **Radio** | 🔴 Pending | 🟢 Active | ⚪ Placeholder |
| **Phone** | 🟡 Testing | 🟢 Active | ⚪ Placeholder |
| **Nav** | 🔴 Pending | ⚪ N/A | ⚪ Placeholder |
| **Dash Display** | 🟡 Testing | 🟢 Active | 🟢 Ready |



## ⚡ Power & Control Logic
- [x] **Relay Strategy:** External Relay Block (Off-PCB).
- [ ] **PCB Logic Layer:** Implement MOSFET/Transistor drivers for relay triggers.
- [ ] **Protection:** Flyback diodes integrated on PCB or at relay coils.
- [ ] **Isolation:** Opto-isolated inputs for 12V vehicle triggers.

## 📦 Hardware Inventory (Custom PCB)
- [ ] **Body Module V1:** ESP32-based CAN controller.
    - [x] Dual Deutsch 12-pin Connectors (Standardized Pinout).
    - [x] Isolated CAN & Opto-I/O.
    - [x] 12x Low-side Outputs (for external relay triggers).
    - [x] 4x Opto-isolated Inputs (Atlas II / Vehicle Triggers).
    
## 🔌 PCB Engineering Specs (Body Module)
- **Processor:** ESP32 (Header Socket Mounted)
- **Connectors:** Dual TE DTM13-12PA-R008 (12-Pin Deutsch)
- **CAN Transceiver:** ISO1050DUBR (Isolated, AEC-Q100)
- **Isolation:** Murata CRE1S0505S3C (3kV Galvanic Isolation)
- **I/O Logic:**
    - 6x Low-Side Sinking Outputs (External Relay Triggers)
    - 2x High-Voltage Opto-Isolated Inputs (Sense/Feedback)
    
## 💻 Firmware Objectives (ESP32)
- [ ] **CAN Driver:** Implement TWAI (Two-Wire Automotive Interface) at 500kbps.
- [ ] **Verification Loop:** Code to compare Output state vs. Opto-Input state.
- [ ] **Debounce Logic:** 50ms filter for Atlas II stick sensors.
- [ ] **Failsafe:** Auto-shutdown for high-amp loads on comms loss.

## 🤖 Flux AI Automations
- [x] **Trace Width Guard:** Custom rule to prevent undersized heater traces.
- [ ] **Thermal Simulation:** Verify ESP32 voltage regulator heat dissipation.
- [ ] **Clearance Check:** 2.5mm isolation gap between Field and Logic rails.

## 🗺️ Master Wiring & Logic
- [x] **Harness Definition:** WireViz YAML configured for MS3, MK60, and ESP32.
- [ ] **Physical Build:** Shielded twisted-pair backbone installation.
- [ ] **Termination Check:** 120-ohm resistors verified at MS3 and Pi 4 nodes.

