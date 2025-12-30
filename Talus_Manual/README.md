# Project Talus: Bronco II Infotainment
**Current Phase:** Mule Build (Functionality > Aesthetics)  
**Prototyping Hardware:** Raspberry Pi 4 (Targeting Pi 5 for Production)

## 🎯 Project Vision
A 1989-themed digital dashboard for a 5.0L Swapped Bronco II. The system integrates MS3 Engine Data, MK60 ABS telemetry, and a custom "Open Source First" navigation engine, all wrapped in a skeuomorphic UI that mimics the original Ford factory stereo.

---

## 🏗️ Implementation Roadmap (Functional Gates)

### Gate 1: Hardware Abstraction & Handshaking
- [x] **USB Bus Probe:** Peripherals identified on Pi 4.
- [x] **CarlinKit Handshake:** Handshake logic verified in `tests/test_carlinkit.py`.
- [x] **RTL-SDR Identification:** RTL-SDR Blog V4 confirmed on Bus.
- [ ] **SDR Audio Stream:** Establish stable audio out from RTL-SDR.
- [ ] **CarPlay Video:** Implement `v4l2h264dec` GStreamer pipeline for Pi 4.

### Gate 2: Logic & Drivetrain Engine
- [x] **Gear Calculation:** RPM/Speed math verified in `logic_engine.py`.
- [ ] **Atlas II States:** Define logic for Twin Stick position sensor mapping.
- [ ] **CAN Mapping:** Standardize MS3 and MK60 message parsing.
- [ ] **GPS Integration:** Connect `gpsd` stream to backend.

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

### Gate 1: Hardware Abstraction & Handshaking
- [x] **360° Vision Link:** Waveshare USB HDMI Capture Card (Inbound).
- [ ] **Capture Verification:** Verify 1080p stream stability via `ffplay` or `v4l2-ctl`.
- [ ] **UVC Integration:** Connect USB video stream to `VisionTab.qml`.
