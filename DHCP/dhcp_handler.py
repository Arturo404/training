import logging
import ipaddress

global dhcp_logger
dhcp_logger = logging.getLogger('dhcp_handler')
dhcp_logger.setLevel(logging.INFO)

class DHCPHandler:
    def __init__(self,network_ip,subnet_mask):
        self.dhcp_network = ipaddress.IPv4Network((network_ip, subnet_mask))
        self.free_ip_adresses = list(self.dhcp_network.hosts())

    def assign_new_ip(self):
        ip_assigned = self.free_ip_adresses.pop()
        dhcp_logger.info(f"New adress assigned {ip_assigned}")
        return str(ip_assigned)

