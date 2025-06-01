import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open on {ip}")

            else:
                pass
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")


def port_scanner(ip, start_port, end_port):
    print(f"Scanning {ip} ports {start_port} on {end_port}...")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)


if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    port_scanner(target_ip, start_port, end_port)