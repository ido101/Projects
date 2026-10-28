import subprocess

def scan_network(network_prefix):
    active_ips = []
    for num in range(1, 255):
        ip_address = f"{network_prefix}.{num}"
        if check_ping(ip_address):
            print(f"----------Found active host: {ip_address}----------")
            active_ips.append(ip_address)
        else:
            print(f"----------No response from: {ip_address}-----------")
    return active_ips


def check_ping(ip_address):
    # Use the ping command to check if the IP address is reachable
    result = subprocess.run(["ping", "-n", "1", ip_address], capture_output=True, text=True)
    print(f"Ping result for {ip_address}: {result.stdout}")
    return "TTL" in result.stdout.upper()


prefix = input("Enter the network prefix (e.g., 192.168.1): ")
active_hosts = scan_network(prefix)
print("Active hosts in the network:")
for host in active_hosts:
    print(host)