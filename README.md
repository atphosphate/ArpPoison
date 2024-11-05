# ArpPoison

## About
**ArpPoison** is a tool designed to perform ARP spoofing or ARP poisoning attacks in a network. This type of attack allows a user to intercept, modify, or stop data in a network by poisoning the ARP cache of devices.

## Features
- **ARP Spoofing**: Redirect network traffic by impersonating another device on the network.
- **Packet Inspection**: Inspect and modify packets as they travel through the network.

## Requirements
Make sure you have Python and the necessary libraries installed before using this tool.

```bash
pip install -r requirements.txt
```

# Setup
```bash
git clone https://github.com/atphosphate/ArpPoison.git
```

# Usage
```bash
sudo python3 arp_posion.py --target <target-ip> -gateway <gateway-ip>
```
## Arguments
- **--target**: The IP address of the target device.
- **--gateway**: The IP address of the gateway or router.

# Disclaimer
This tool is for educational purposes only. Unauthorized use of this tool is illegal.
