# Project Talus: AI Context & State Restore
**Last Updated:** January 3, 2026
**Repository Status:** Active Build
**Master Ledger:** `talus_master.json` (Cost & Task Tracking)

---

## 1. Core Mission
**Objective:** Transform a 1988 Ford Bronco II into a "Modern SVT Raptor in a Retro Shell."
**Philosophy:**
* **Aesthetics:** Period-correct 1988 exterior (Two-Tone Molten Orange/Black) but flawless "Bad Chad" bodywork.
* **Capability:** Modern powertrain (5.0L V8), digital nervous system (CAN Bus), and overbuilt safety (Cage/Armor).
* **User Experience:** Digital dash, push-button control, but analog feel.

## 2. The "Wife Contract" (Immutable Constraints)
* **The 2-Week Rule:** The vehicle cannot be non-operational (on jack stands) for more than 14 consecutive days. Major surgeries must be staged in sub-2-week sprints.
* **Clean Garage Protocol:** No permanent mess. Bodywork dust (High-Build Primer) must be managed via section-work and immediate cleanup.
* **Clean Office Protocol:** The office must be cleaned and organized regularly. This includes dusting, wiping down surfaces, and vacuuming multiple times a week to prevent project "creep" into living spaces.
* **Financial Velocity:** Tasks are prioritized by *Financial Velocity* ($Velocity = Priority / Cost$). "Quick Wins" keep morale high.

## 3. Critical Engineering Decisions (Do Not Regress)

### A. Electronics & Body Control (The "Nervous System")
* **Architecture:** Distributed I/O using Custom PCB Nodes (ESP32-based) communicating via CAN Bus.
* **Hardware Spec:**
    * **Nodes:** Node A (Engine Bay Acc.), Node B (Dash/Interior), Node C (Rear Chassis).
    * **PCB Design:** Custom Flux.ai Board with socketed ESP32 DevKit V1.
    * **Power Supply:** **LM76003-Q1** (60V Buck) + **SMBJ26CA** TVS. *Critical: Must survive 60V Load Dump.*
    * **Drivers:** **IRLML0060TRPBF** (60V, 2.7A) Logic Level MOSFETs. *Replaces 2N7002.*
    * **Connectivity:** Deutsch DTM13 PCB-mount headers (Waterproof).

### B. Powertrain & Engine Management
* **Engine:** 5.0L Ford Windsor V8 (Explorer Donor).
* **Engine Management (ECU):** **MS3Pro Ultimate** (Standalone).
    * *Role:* Controls Fuel, Ignition, and Engine Safeties.
    * *Integration:* Broadcasts engine data (RPM, Temp, TPS) to the CAN Bus for the Digital Dash.
* **Transmission:** M5OD-R2 5-Speed Manual.
* **Transfer Case:** Advance Adapters Atlas II.
* **Charging System:**
    * **Alternator:** 180A High Output (3G Large Case or 4G Rewound).
    * **Protection:** "Big 3" Upgrade (1/0 AWG) + 200A AMG Fuse.
    * **Risk:** 180A Alternator creates massive inductive spikes. All electronics must be Load Dump rated.

### C. Body & Aesthetics
* **Paint Scheme:**
    * **Upper:** Ford Molten Orange (Tri-Stage Pearl).
    * **Lower:** Jet Black (Base/Clear).
    * **Chassis/Armor:** **Steel-It Polyurethane** (Black/Gray). *Weld-through capability required.*
* **Bodywork Strategy:** "Bad Chad" Method. Heavy high-build polyester primer -> Block Sand 80-grit -> Seal -> Paint. Done in sections (Hood, Doors, Roof) to respect the 2-Week Rule.
* **Hood:** US Body Source "Mach I" Fiberglass.

## 4. Active Workflows
1.  **Talus Tally:** All purchases must be logged in `talus_master.json` under the specific `WP-ID`.
2.  **Flux.ai Workflow:**
    * Current BOM: `...BOM-V2026-01-03...Flux.csv`
    * PCB Fab: JLCPCB (4-Layer, Impedance Control).
3.  **Documentation:**
    * `electronics_architecture.md`: Detailed pinouts and ESP32 GPIO maps.
    * `mechanical_config.md`: Suspension, steering, and adapter specs.

---
**End of Context Restore**