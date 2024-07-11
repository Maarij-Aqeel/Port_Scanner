#Port Scanner

This Python script performs a basic port scan on a specified target to check the status of common ports. It takes a hostname or IP address as an input and reports whether each scanned port is open or closed.
Features:

    Scans a predefined list of common ports (e.g., 53, 80, 443, etc.).
    Option to specify custom ports for scanning.
    Converts hostname to IP address for scanning.
    Displays the start time of the scan and the target being scanned.
    Handles common errors like invalid arguments, hostname resolution failure, and connection issues gracefully.

Usage:
      To scan common ports on a target:  python port_Scanner.py <hostname>

To scan specific ports on a target:  python port_Scanner.py <hostname> <arg2> <comma_separated_ports>

    Note: <arg2> can be -p as the script currently checks for the presence of four arguments to trigger the custom port scan.

Example:
        python3 port_Scanner.py example.com
        
        python3 port_Scanner.py example.com -p 21,22,80

Requirements:

    Python 3.x
