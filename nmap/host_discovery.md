## Host Discovery

### Command
nmap -sn 192.168.1.0/24

### Purpose
Identifies live hosts on a network without scanning ports.

### Explanation
This scan sends ICMP echo requests to determine which devices are active.
It is commonly used during the reconnaissance phase of penetration testing.
