# For Checking The IP address and CIDR Values lying in the Range of the Network Classes



def check_ip(network_class, ip):
    ip_addr = ip.split('.')
    if network_class == 'A':
        if (int(ip_addr[0]) >= 0 and int(ip_addr[0]) <= 127):
            return 'VALID'
        elif (int(ip_addr[0]) >= 224 and int(ip_addr[0]) <= 239):
            return 'INVALID2'
        elif (int(ip_addr[0]) >= 240 and int(ip_addr[0]) <= 255):
            return 'INVALID3'
        else:
            return 'INVALID'
    if network_class == 'B':
        if (int(ip_addr[0]) >= 128 and int(ip_addr[0]) <= 191):
            return 'VALID'
        elif (int(ip_addr[0]) >= 224 and int(ip_addr[0]) <= 239):
            return 'INVALID2'
        elif (int(ip_addr[0]) >= 240 and int(ip_addr[0]) <= 255):
            return 'INVALID3'
        else:
            return 'INVALID'
    if network_class == 'C':
        if (int(ip_addr[0]) >= 192 and int(ip_addr[0]) <= 223):
            return 'VALID'
        elif (int(ip_addr[0]) >= 224 and int(ip_addr[0]) <= 239):
            return 'INVALID2'
        elif (int(ip_addr[0]) >= 240 and int(ip_addr[0]) <= 255):
            return 'INVALID3'
        else:
            return 'INVALID'

def check_cidr(network_class, cidr):
    if network_class == 'A':
        if (int(cidr) >= 8 and int(cidr) <= 15):
            return 'VALID'
        else:
            return 'INVALID'
    if network_class == 'B':
        if (int(cidr) >= 16 and int(cidr) <= 23):
            return 'VALID'
        else:
            return 'INVALID'
    if network_class == 'C':
        if (int(cidr) >= 17 and int(cidr) <= 32):
            return 'VALID'
        else:
            return 'INVALID'
