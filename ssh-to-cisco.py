from netmiko import ConnectHandler

CSR = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.220',
    'username': 'root',
    'password': 'root'
}

# Establish SSH connection
net_connect = ConnectHandler(**CSR)

# Send command and retrieve output
output = net_connect.send_command('show ip int brief')
print(output)

# Disconnect from the device
net_connect.disconnect()
