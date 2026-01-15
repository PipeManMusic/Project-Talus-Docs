---
# Bronco II "Tactical" Restomod Sun Visor Design Document

> **Project:** Custom Sun Visor Fabrication  
> **Theme:** Industrial/Tactical (Camp Hale Inspiration) with Modern Functionality  
> **Vehicle:** Ford Bronco II (Restomod)

---

## 1. Project Overview

Replace the floppy vintage vinyl visors with a rigid, modern-feeling system. The design uses a "Sandwich" construction method to combine a soft safety rim with a recessed industrial aluminum core featuring MOLLE storage and integrated "Stealth" lighting.

### Key Features
- **Modern Feel:** Utilizes 2009–2014 Ford F-150 internal detent mechanisms for a factory-grade "snap" action.
- **Tactical Storage:** Recessed aluminum center plate with laser-cut MOLLE grid.
- **Integrated Lighting:** High-output LED bolts disguised as mounting hardware.
- **Safety:** Upholstered outer rim to prevent injury from sharp metal edges.

---

## 2. Bill of Materials (BOM)

### A. The Donor Mechanism (Junkyard Source)
- **Donor Vehicle:** 2009–2014 Ford F-150 (12th Gen)

**Parts to Harvest:**
- *Pivot Mechanism*: The internal black plastic "detent block" (requires cutting open the donor visor)
- *Pivot Rod*: The metal arm connecting the visor to the roof (hollow versions preferred for wiring)
- *Center Clips*: The hooks that mount near the rearview mirror (for the rod tip to snap into)

### B. Lighting & Electronics
- **Light Units:** Oznium Flush Mount LED Bolt
  - Size: `6mm (M6 Thread)`
  - Lens: *No Lens* (Flat face / Stealth look)
  - Housing: Black Aluminum
  - Color: Cool White (Functional) or Warm White (Vintage)
- **Switching:** Magnetic Reed Switch (Normally Closed) + Neodymium Magnet (hidden in headliner)
- **Dimming:** 1k Ohm Resistor (1/4 Watt) – Essential to dim the 1W LEDs to a non-blinding glow
- **Wire:** 26 AWG Silicone Wire (High flexibility for the pivot point)

### C. Structural Materials
- **Frame (Rim):** 1/2" HDPE Plastic Sheet or Baltic Birch Plywood
- **Core (Plate):** 1/8" (0.125") Aluminum Sheet (5052 Alloy)
- **Mirror:** 1/8" Acrylic Mirror (Shatterproof)

### D. Aesthetic Hardware
- **Trim Washers:** M6 Anodized Aluminum Beauty Washers (Color: Orange)
- **Finish:** Cerakote (Sniper Grey or Armor Black) for the Aluminum Plate

---

## 3. Fabrication Specifications

### The "Sandwich" Assembly (Layer Stack)
Designed to create a 1/2" deep storage cavity on the underside.

#### Top Layer (Aluminum Plate)
- Serves as the rigid spine
- Laser-cut with PALS/MOLLE grid (`1" x 1.5"` slots)
- Contains the cutout for the mirror and 4 mounting holes for the LED bolts
- Mounts to the top face of the Frame

#### Middle Layer (The Frame)
- 1/2" thick material cut into a ring (approx 1.5" wide border)
- **Router Pocket:** A cavity routed into the corner to house the F-150 plastic pivot block flush
- **Wire Channels:** Shallow grooves routed to guide wires from the pivot to the lights

#### Outer Layer (Upholstery)
- 1/8" Closed-cell foam + Interior Fabric wrapped around the Frame only
- Creates a soft "bumper" edge

### The "Stealth" Light Install
- **Concept:** The lights replace the screws holding the mirror
- **Mounting:** The Oznium LED Bolts pass through the Orange Beauty Washers → Aluminum Plate → Secured with thin nuts on the back (inside the hollow wire gap)
- **Visual:** Looks like 4 orange industrial rivets holding the mirror plate on

---

## 4. Integration Logic (TalusTrace)

**Wiring Path:**  
Fuse Box (ACC Power) → A-Pillar → Pivot Rod (Hollow) → Resistor → Reed Switch → LED Bolts → Ground (Return via Rod or separate wire)

**TalusTrace Pinout Data:**
- **Component ID:** `VISOR_L` / `VISOR_R`
- **Connector:** `2-PIN_MICRO_JST` (Inside the headliner for easy removal)
- **Load:** 20mA (dimmed) per visor
- **Function:** Automated on/off via magnet sensor (no physical toggle switch visible)

---

## 5. Step-by-Step Build Notes

1. **Harvest:** Cut open F-150 visors. Extract the plastic pivot mechanism carefully. Keep the plastic housing around the rod intact for structure.
2. **Router:** Trace the F-150 mechanism onto the HDPE frame. Router a pocket so the mechanism sits flush. Through-bolt it to the frame for strength.
3. **Modify Rod:** If the F-150 rod angle is wrong for the BII roof, heat and bend or cut and weld the BII triangular mounting base onto the F-150 rod shaft.
4. **Assemble Sandwich:**
    - Install LEDs and Mirror to the Aluminum Plate first
    - Perform all soldering on the back of the plate
    - Screw the Aluminum Plate onto the Upholstered Frame
5. **Install:** Mount the visor. Glue the small magnet inside the headliner fabric exactly where the "Reed Switch" (inside the visor) touches the roof when stowed.
---