import ipaddress
ip = "2001:0db8:85a3:08d3:1319:8a2e:0370:7334"


try:
    ip_obj = ipaddress.IPv6Address(ip)
    print(f"{ip} is a valid IPv6 address")
except ipaddress.AddressValueError:
    print(f"{ip} is a invlaid IPv6 address")