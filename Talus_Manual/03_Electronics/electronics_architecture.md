# Project Talus: Electronics Architecture & HAL
**Status:** Frozen for PCB Rev 1 (Flux.ai)
**Controller:** ESP32 DevKit V1 (30-Pin)
**Protocol:** CAN 2.0B @ 500kbps

---

## 1. System Topology
The vehicle uses a **Distributed I/O** architecture. Instead of one massive fuse box, three "Smart Nodes" control local devices.
* **Bus Speed:** 500kbps (Standard OBD-II/MS3Pro speed).
* **Wiring:** Shielded Twisted Pair (White/Blue) for all CAN High/Low connections.
* **Termination:** 120Ω resistor at **Node A** (Front) and **Node C** (Rear). Node B and MS3Pro are stubs.

### The Nodes
1.  **Node A (Engine Bay):**
    * *Location:* Driver fender well.
    * *Role:* Headlights, Horn, Turn Signals (Front), Wiper triggers, Hood pin.
2.  **Node B (Dashboard):**
    * *Location:* Center console / Behind dash.
    * *Role:* Interior Lights, Blinkers (Indicator), Rotary Knobs (via I2C), Ignition Switch sense.
3.  **Node C (Rear Chassis):**
    * *Location:* Interior panel (Driver rear).
    * *Role:* Fuel Pump (via Relay), Tail Lights, Reverse Lights, Fuel Level Sender (ADC).

---

## 2. "The Talus Node" (Hardware Specification)
Each node uses the identical **Custom Flux.ai PCB** to simplify spares and manufacturing.
* **Power:** 12V Input -> **LM76003-Q1** (60V Buck) -> 5V System.
* **Logic:** ESP32 DevKit V1 (Socketed).
* **Protection:**
    * **Input:** SMBJ26CA TVS (Load Dump Clamp).
    * **Outputs:** Flyback Diodes on all Relay Drivers.
    * **Isolation:** Opto-isolated Digital Inputs (12V tolerant).

### GPIO Pinout (The "Truth Table")
*Firmware MUST use these assignments.*

| Function | PCB Designator | ESP32 GPIO | Logic State | Note |
| :--- | :--- | :--- | :--- | :--- |
| **Output 1** | Q1 (IRLML0060) | **GPIO 13** | High = ON | Low-Side Sink (GND) |
| **Output 2** | Q2 (IRLML0060) | **GPIO 14** | High = ON | Low-Side Sink (GND) |
| **Output 3** | Q3 (IRLML0060) | **GPIO 27** | High = ON | Low-Side Sink (GND) |
| **Output 4** | Q4 (IRLML0060) | **GPIO 26** | High = ON | Low-Side Sink (GND) |
| **Output 5** | Q5 (IRLML0060) | **GPIO 25** | High = ON | Low-Side Sink (GND) |
| **Output 6** | Q6 (IRLML0060) | **GPIO 33** | High = ON | Low-Side Sink (GND) |
| **Input 1** | U5 (Opto) | **GPIO 34** | High = Active | Input Only (No Pull-up) |
| **Input 2** | U6 (Opto) | **GPIO 35** | High = Active | Input Only (No Pull-up) |
| **Input 3** | U7 (Opto) | **GPIO 32** | High = Active | |
| **Input 4** | U8 (Opto) | **GPIO 39** | High = Active | Input Only (VN) |
| **CAN TX** | U4 (ISO1050) | **GPIO 22** | Serial | |
| **CAN RX** | U4 (ISO1050) | **GPIO 21** | Serial | |

---

## 3. Connector Pinout (Deutsch DTM13-12P)
The PCB features two **mirrored** 12-pin headers (`J1` and `J2`).
* *Note:* Inputs 3 & 4 (GPIO 32/39) are available on the PCB internal headers but **not** routed to the main 12-pin connector limit.

| Pin # | Function | Spec | Wire Gauge (Rec.) |
| :--- | :--- | :--- | :--- |
| **1** | **+12V Battery** | Fused Input (15A Max) | 14 AWG |
| **2** | **Chassis GND** | Power Ground | 14 AWG |
| **3** | **CAN High** | Data + | 20 AWG (Twisted) |
| **4** | **CAN Low** | Data - | 20 AWG (Twisted) |
| **5** | **Output 1** | 2.7A Max (Sink) | 18 AWG |
| **6** | **Output 2** | 2.7A Max (Sink) | 18 AWG |
| **7** | **Output 3** | 2.7A Max (Sink) | 18 AWG |
| **8** | **Output 4** | 2.7A Max (Sink) | 18 AWG |
| **9** | **Output 5** | 2.7A Max (Sink) | 18 AWG |
| **10** | **Output 6** | 2.7A Max (Sink) | 18 AWG |
| **11** | **Input 1** | 12V Trigger (Opto) | 20 AWG |
| **12** | **Input 2** | 12V Trigger (Opto) | 20 AWG |

---

## 4. MS3Pro Ultimate Integration
The Engine ECU is a "Black Box" that broadcasts data to the CAN Bus.
* **CAN ID Base:** `1512` (Standard MS3 29-bit or 11-bit broadcast).
* **Critical Data Consumed by Nodes:**
    * *RPM:* Used by Dashboard (Node B) for Display.
    * *Coolant Temp:* Used by Node A to trigger Electric Fan (via Relay).
    * *Voltage:* Used by all nodes for "Low Bat" conservation mode.