
# Network & Port Scanner

This tool scans the entire network and discovers active hosts. It then scans the ports of the active hosts to identify open ports which can be vulnerable to attacks. The tool logs the results in a `log.txt` file and scans the network every 5 seconds.

## Features

- Discovers IP addresses along with MAC addresses of active hosts in the network.
- Scans ports of active hosts to detect open ports and potential vulnerabilities.
- Logs results with a timestamp in `log.txt`.
- Scans the network continuously every 5 seconds.
- Helps identify unknown or potentially malicious nodes on the network.

## Use Cases

- **Network Discovery**: Identifies active IP addresses and their associated MAC addresses.
- **Security Assessment**: Scans for common open ports that may indicate vulnerabilities (e.g., SSH, HTTP, FTP, RDP).
- **Vulnerability Detection**: Detects open ports on devices that could be vulnerable to attacks such as brute-force, SQL injection, and password cracking.

## Ports and Vulnerabilities

The following ports are scanned by default:

- **22 (SSH)**: Allows remote login. Weak passwords are a vulnerability.
- **80 (HTTP)**: Common web server. Vulnerable to attacks like XSS and SQL Injection.
- **443 (HTTPS)**: Secure HTTP. Can be vulnerable to misconfigurations.
- **21 (FTP)**: File Transfer Protocol. Vulnerable to password cracking.
- **23 (Telnet)**: Vulnerable to eavesdropping, should be replaced by SSH.
- **3389 (RDP)**: Remote Desktop Protocol. Vulnerable to brute-force attacks.
- **3306 (MySQL)**: SQL Database Service. Vulnerable to injection attacks.
- **8080 (HTTP Alt)**: Alternative HTTP port. Can have security flaws.

## Requirements

- Python 3.x
- `scapy` library (install using `pip install scapy`)

## Installation

1. Clone or download the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install scapy
   ```
3. Save the script as `main.py`.

## Usage

To run the scanner, execute the following command in your terminal:

```bash
python main.py
```

The script will continuously scan the network for active hosts and open ports, logging the results to `log.txt`. The scan runs every 5 seconds.

## Stopping the Scan

To stop the scan at any time, press `Ctrl+C` in your terminal.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
