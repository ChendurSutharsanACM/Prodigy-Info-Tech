from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):  
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        proto = packet["IP"].proto
        
        # Determine protocol
        if packet.haslayer("TCP"):
            protocol = "TCP"
        elif packet.haslayer("UDP"):
            protocol = "UDP"
        elif packet.haslayer("ICMP"):
            protocol = "ICMP"
        else:
            protocol = "Unknown"
        
        with open("captured_packets.txt", "a") as f:
            f.write(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {proto}, Layer4 Protocol: {protocol}\n")

def main():
    print("Sniffing started...")
    sniff(prn=packet_callback, store=0)  

if __name__ == "__main__":
    main()
