import os
import datetime

# ==========================================
# PROJECT TALUS: MASTER DATA BLOCKS
# ==========================================
TIMESTAMP = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

CONTEXT_RESTORE_HEADER = f"""
# SYSTEM PROMPT: RESTORE PROJECT CONTEXT
# DATE: {TIMESTAMP}
# INSTRUCTION: The user is building "Project Talus". Adopt the persona of the Project Talus AI Assistant. 
# Below is the current configuration state. Ingest this data and wait for user input.

---
"""

# 1. OVERVIEW
SECTION_OVERVIEW = """
# 1. Overview & Constraints
* **Project Name:** Talus
* **Base Vehicle:** 1984-1990 Ford Bronco II
* **Objective:** Retro-Mod. 1988 Aesthetics + SVT Raptor Capability.
* **Media:** YouTube Channel "Project Talus".
* **The "Wife Contract" (Hard Constraints):**
    1. Workspace must be clean.
    2. **The 2-Week Rule:** Vehicle cannot be non-operational for >2 weeks.
    3. Funding: Sale of 1954 F100 + Bonus.
"""

# 2. MECHANICAL
SECTION_MECHANICAL = """
# 2. Mechanical Systems
* **Engine:** 5.0L Ford Windsor V8 (Explorer Serpentine Front Dress).
* **ECU:** MegaSquirt 3 (MS3) w/ CAN Bus Broadcast.
* **Transmission:** Mazda M5OD-R2 (Manual 5-Speed).
* **Transfer Case:** Advance Adapters Atlas II (Twin Stick).
* **Axles:**
    * Front: Dana 35 TTB (1993-94 Explorer Knuckles for ABS).
    * Rear: Ford 8.8 (Mustang S197 Backing Plates for ABS).
* **Brakes/ABS:** BMW MK60E5 (E90 3-Series) Standalone Swap.
    * Integration: Reads custom tone rings, sends speed to CAN Bus.
* **Suspension:** James Duff Stage 3 (Long Arms, Variable Rate Springs).
"""

# 3. ELECTRONICS (UPDATED: Unified Python/Qt Stack)
SECTION_ELECTRONICS = """
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
"""

# 4. FABRICATION
SECTION_FABRICATION = """
# 4. Fabrication & Interior
* **Steering:**
    * Column: Late 90s Ford Ranger (Manual/Floor Shift).
    * Wheel: Lincoln Navigator (Wood/Leather).
    * Logic: Wireless ESP32 Hub inside wheel (Powered by Cruise wires).
* **Glovebox "Tech Bay":**
    * Stock liner removed for Vintage Air clearance.
    * False wall installed to mount Industrial USB Hub (Switched).
* **Climate Control:**
    * Vintage Air Gen IV (Internal).
    * Controls: Digital Potentiometers (AD5206) spoofing slide levers.
* **Wiring Standards (DIN 72551):**
    * **Red (30):** Battery Constant.
    * **Black (15):** Ignition Switched.
    * **Brown (31):** Ground.
    * **Connectors:** Deutsch DT/DTM.
    * **Loom:** Snake Skin (Engine) / Tesa Felt (Interior).
"""

# 5. DEVELOPMENT ENVIRONMENT (UPDATED: Unified Python/Qt Stack)
SECTION_DEV_ENV = """
# 5. Development Environment & Workflow

* **Host Machine:** Ubuntu Linux Laptop.
* **IDE:** Visual Studio Code (VS Code).
* **Connection Method:** VS Code "Remote - SSH" Extension.
* **Version Control:** Git / GitHub.

## Repository Structure

### 1. Documentation (`Project-Talus-Docs`)
* **Repo:** `github.com/PipeManMusic/Project-Talus-Docs` (Private)
* **Purpose:** The "Digital Glovebox."

### 2. Infotainment System (`BroncoII-Infotainment`)
* **Repo:** `github.com/PipeManMusic/BroncoII-Infotainment` (Public)
* **Hardware:** Pi 5.
* **Stack:** Python 3 + PySide6 (Qt).
* **Core:** `can_manager.py` (SocketCAN), `media_manager.py` (DBus/MPRIS).

### 3. Instrument Cluster (`BroncoIIDash`)
* **Repo:** `github.com/PipeManMusic/BroncoIIDash`
* **Hardware:** Pi 4 (CarPiHat).
* **Stack:** Python 3 + PySide6 (Qt).
* **Core:** `can_decoder.py`, `dashboard.qml`.
* **Features:** Switchable Layouts (Sport/Zen), Custom SVG Status Doll.
"""

# ==========================================
# SCRIPT LOGIC
# ==========================================

def write_file(path, content):
    """Writes content to a file, ensuring directories exist."""
    dir_name = os.path.dirname(path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[CREATED] {path}")

def main():
    base_dir = "Talus_Manual"
    
    # 1. Generate Human Documentation
    print(f"--- Updating Project Talus Documentation ({TIMESTAMP}) ---")
    
    write_file(f"{base_dir}/01_Overview/project_overview.md", SECTION_OVERVIEW)
    write_file(f"{base_dir}/02_Mechanical/mechanical_systems.md", SECTION_MECHANICAL)
    write_file(f"{base_dir}/03_Electronics/electronics_architecture.md", SECTION_ELECTRONICS)
    write_file(f"{base_dir}/04_Fabrication/fabrication_standards.md", SECTION_FABRICATION)
    write_file(f"{base_dir}/05_Development/dev_environment.md", SECTION_DEV_ENV)
    
    # 2. Generate AI Context Restoration File
    ai_memory_blob = (
        CONTEXT_RESTORE_HEADER + "\n" +
        SECTION_OVERVIEW + "\n" +
        SECTION_MECHANICAL + "\n" +
        SECTION_ELECTRONICS + "\n" +
        SECTION_FABRICATION + "\n" +
        SECTION_DEV_ENV + "\n" +
        "--- \n# END OF CONTEXT RESTORE BLOCK"
    )
    
    write_file(f"{base_dir}/_AI_CONTEXT_RESTORE.md", ai_memory_blob)
    
    print("--- Update Complete ---")
    print(f"AI Memory updated: Unified Python/Qt Stack for BOTH screens.")

if __name__ == "__main__":
    main()