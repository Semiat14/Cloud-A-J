network = "192.168.1.0"
prefix = 24
subnet_mask = "255.255.255.0"
total_hosts = 254

devices = [
    {"name": "Router", "ip" : "192.168.1.1"}, 
    {"name": "Switch", "ip" : "192.168.1.2"}, 
    {"name": "PC1",    "ip" : "192.168.1.10"}, 
    {"name": "PC2",    "ip" : "192.168.1.11"}, 
] 
print("=" * 31)
print("        NETWORK DIAGRAM")
print("=" * 31) 
print()
print(f"[{devices[0]['name']}]  {devices[0]['ip']}")
print("       | ")
print(f"[{devices[1]['name']}]  {devices[1]['ip']}")
print("       | ")
print("   ---|---")
print("   |     |")
print(f"[{devices[2]['name']}]  {devices[3]['name']}")
print(f"{devices[2]['ip']}  {devices[3]['ip']}")
print()
print(f"Network:     {network} / {prefix}")
print(f"subnet mask: {subnet_mask}")
print(f"total hosts: {total_hosts}") 

print()
print("--- IP CHECK ---")
for device in devices : 
    parts = device["ip"].split(".")
    if parts[0] =="192" and parts[1] =="168" and parts[2] =="1":
        print(f"{device['name']}  ({device['ip']}) --OK" )
    else:
        print(f"{device['name']}  ({device['ip']}) -- WARNING: outside subnet")