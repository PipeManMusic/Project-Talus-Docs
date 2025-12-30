
# 5. Development Environment & Workflow
* **Host Machine:** Ubuntu Linux Laptop.
* **IDE:** Visual Studio Code (VS Code).
* **Connection Method:** VS Code "Remote - SSH" Extension.
    * *Target:* Connects directly to Raspberry Pi 4 (Cluster Node) or Pi 5 (Infotainment).
    * *Benefit:* Edits code live on the vehicle hardware.
* **Version Control:** Git / GitHub.
    * *Cluster Repo:* `github.com/PipeManMusic/BroncoIIDash`
* **Software Stack:**
    * *Cluster:* Godot Engine (Exported to Pi 4).
    * *Backend:* Node.js (Handling CAN Bus messages).
    * *Microcontrollers:* ESP-IDF or Arduino Framework (PlatformIO recommended).
