import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50}{:<20}{:<8}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

count = 0
for entry in data['imdata']:
    if count == 3:
        break
    interface = entry.get('l1PhysIf', {}).get('attributes', {})
    dn = interface.get('dn', '')
    description = interface.get('descr', '')
    speed = interface.get('speed', 'inherit')
    mtu = interface.get('mtu', 'inherit')
    print("{:<50}{:<20}{:<8}{:<6}".format(dn, description, speed, mtu))
    count += 1
