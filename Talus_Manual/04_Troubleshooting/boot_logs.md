# Boot Logs & Debugging

## Accessing Logs
* **Cluster Node:** `ssh pi@192.168.1.10` -> `journalctl -u bronco-dash.service`
* **Infotainment:** `ssh pi@192.168.1.11` -> `pm2 logs`

## Common Issues
* **Screen Black:** Check HDMI timings in /boot/config.txt
* **No Start:** Check Node B "Ignition" LED status.
