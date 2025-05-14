import socket
import time
from scapy.all import ARP, Ether, srp
from datetime import datetime

# Common ports to scan with descriptions
PORTS = {
    22: ("SSH", "Allows remote login. Weak passwords are a vulnerability."),
    80: ("HTTP", "Common web server. Vulnerable to attacks like XSS and SQL Injection."),
    443: ("HTTPS", "Secure HTTP. Can be vulnerable to misconfigurations."),
    21: ("FTP", "File Transfer Protocol. Vulnerable to password cracking."),
    23: ("Telnet", "Vulnerable to eavesdropping, should be replaced by SSH."),
    3389: ("RDP", "Remote Desktop Protocol. Vulnerable to brute-force attacks."),
    3306: ("MySQL", "SQL Database Service. Vulnerable to injection attacks."),
    8080: ("HTTP Alt", "Alternative HTTP port. Can have security flaws."),
}

def log(msg):
    """Logs messages with a timestamp to log.txt"""
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")
    print(msg)  # Also print to console

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        return local_ip
    except Exception as e:
        log(f"[!] Error getting local IP: {e}")
        return None

def scan_network(network_range):
    """Scan the network for active hosts and return a list of IPs and MAC addresses"""
    log(f"[*] Scanning network: {network_range}")
    active_hosts = []
    arp_request = ARP(pdst=network_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    result = srp(packet, timeout=3, verbose=False)[0]

    local_ip = get_local_ip()
    router_ip = f"{local_ip.rsplit('.', 1)[0]}.1"

    for _, received in result:
        if received.psrc != router_ip:
            active_hosts.append({"ip": received.psrc, "mac": received.hwsrc})

    return active_hosts

def scan_ports(host):
    """Scan the ports of a host and return a list of open ports"""
    open_ports = []
    log(f"[*] Scanning ports for {host['ip']} ({host['mac']})")
    for port in PORTS.keys():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host['ip'], port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            continue
    return open_ports

def run_network_scanner():
    """Main function to run the network and port scanner"""
    local_ip = get_local_ip()
    if not local_ip:
        log("[!] Could not determine local IP.")
        return

    network_range = f"{local_ip.rsplit('.', 1)[0]}.0/24"
    log(f"[*] Starting continuous scan for network: {network_range}")

    while True:
        active_hosts = scan_network(network_range)

        if not active_hosts:
            log("[*] No active hosts found.")
        else:
            for host in active_hosts:
                open_ports = scan_ports(host)
                for port in open_ports:
                    log(f"[*] ⚠️ Port {port} open on {host['ip']} - {PORTS[port][0]}")

        time.sleep(5)  # 5-second interval between scan cycles

if __name__ == "__main__":
    try:
        run_network_scanner()
    except KeyboardInterrupt:
        log("[!] Scan stopped by user.")
