
# Network & Port Scanner

## Overview

The **Network & Port Scanner** is a powerful tool designed to discover active devices on your local network and scan the open ports on those devices for potential security vulnerabilities. This tool continuously scans the network every 5 seconds, helping you monitor the security of your network in real time. It is designed for use by system administrators and network security professionals to identify and protect against unauthorized access and vulnerabilities.

## Features

* **Network Scanning**: Identifies active devices on the local network by discovering their IP and MAC addresses.
* **Port Scanning**: Scans common ports on identified devices to detect open ports that could be vulnerable to attacks.
* **Logging**: Logs the scan results with timestamps into a file (`log.txt`) for later analysis.
* **Continuous Scanning**: The tool runs every 5 seconds by default, continuously scanning and updating results.
* **Common Vulnerability Detection**: Identifies open ports associated with known vulnerabilities, such as SSH, HTTP, FTP, and RDP.

## Use Cases

* **Network Discovery**: Identify all devices connected to your local network by discovering their IP and MAC addresses.
* **Security Assessment**: Check for open ports on devices that could be vulnerable to attacks (e.g., brute-force, SQL injection, password cracking).
* **Vulnerability Detection**: Monitor for unprotected ports on devices, such as SSH, HTTP, FTP, RDP, etc., that are common targets for attacks.
* **Real-Time Network Monitoring**: Continuously scan the network to identify new devices or services as they connect to your network.

## Ports and Vulnerabilities

The script scans the following ports, which are commonly associated with various vulnerabilities:

* **22 (SSH)**: Allows remote login. Vulnerable to weak passwords and brute-force attacks.
* **80 (HTTP)**: Common web server port. Vulnerable to attacks like XSS and SQL Injection.
* **443 (HTTPS)**: Secure HTTP port. Vulnerable to misconfigurations and weak encryption.
* **21 (FTP)**: File Transfer Protocol. Often vulnerable to password cracking and unencrypted data transfer.
* **23 (Telnet)**: Known to be vulnerable to eavesdropping. Should be replaced with SSH.
* **3389 (RDP)**: Remote Desktop Protocol. Common target for brute-force attacks and exploits.
* **3306 (MySQL)**: SQL Database Service. Often vulnerable to SQL injection attacks if not secured properly.
* **8080 (HTTP Alt)**: Alternate HTTP port. Can have vulnerabilities similar to HTTP (port 80), such as XSS or injection flaws.

## Requirements

* **Python 3.x**: Ensure Python 3 is installed on your system.

* **`scapy` Library**: This tool requires the `scapy` library for network packet manipulation. Install it using the following command:

  ```bash
  pip install scapy
  ```

* **Network Access**: The script needs to be run with administrative privileges to scan the network and access raw network interfaces.

## Installation

1. Clone or download the repository to your local machine:

   ```bash
   git clone https://github.com/CEHCVKR/Network_Port_Scanner.git
   cd Network_Port_Scanner
   ```

2. Install the required dependencies:

   ```bash
   pip install scapy
   ```

3. Save the script as `main.py` in your desired directory.

## Setup and Usage

### Running the Script

To start the scanner, execute the script by running:

```bash
python main.py
```

This will initiate the continuous network scanning process. The script will detect active devices and their corresponding open ports every 5 seconds, logging the results to `log.txt`.

### Stopping the Scan

To stop the scanning process, press `Ctrl+C` in the terminal. This will halt the script gracefully.

### Logging

* The script logs each scan to `log.txt` with a timestamp.
* Each entry will include:

  * The IP and MAC address of detected devices.
  * The open ports found on those devices.
  * A description of the vulnerability associated with each open port.

### Scan Configuration

The script can be configured to scan different subnets or networks by modifying the following line in the script:

```python
network_range = f"{local_ip.rsplit('.', 1)[0]}.0/24"
```

This sets the network range to scan. You can modify this to scan other subnets, depending on your network configuration.

### Scan Interval

The default scan interval is set to 5 seconds:

```python
time.sleep(5)  # 5-second interval between scan cycles
```

You can change this value to adjust how frequently the network is scanned.

## Example Log Output

```
[2025-05-15 10:00:05] Scanning network: 192.168.1.0/24
[2025-05-15 10:00:10] Scanned 192.168.1.10 - MAC: 00:14:22:01:23:45
[2025-05-15 10:00:10] ⚠️ Port 22 open on 192.168.1.10 - SSH
[2025-05-15 10:00:15] Scanned 192.168.1.15 - MAC: 00:14:22:01:67:89
[2025-05-15 10:00:15] ⚠️ Port 80 open on 192.168.1.15 - HTTP
[2025-05-15 10:00:20] Scanned 192.168.1.20 - MAC: 00:14:22:01:45:67
[2025-05-15 10:00:20] ⚠️ Port 3389 open on 192.168.1.20 - RDP
```

## Troubleshooting

### Unable to scan network or get IP address

Ensure that you have administrator privileges and that your network adapter is properly configured.

### Ports Not Showing Up

If the scan does not detect any open ports, make sure the target device has the relevant services running and accessible from the network.

### Permissions Issue

Make sure the script is executed with sufficient privileges to modify network interfaces, especially when accessing raw packets or managing firewall settings.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

**CHINNAPAREDDY VENKATA KARTHIK REDDY**
LinkedIn: [https://www.linkedin.com/in/cvkr/](https://www.linkedin.com/in/cvkr/)
GitHub: [https://github.com/CEHCVKR](https://github.com/CEHCVKR)

---

Feel free to contribute to this project by opening issues, submitting pull requests, or providing feedback. Happy scanning!
