from netmiko import ConnectHandler
 
print('-'*12)
print('Devices:')
print('-'*12)

with open('devices.txt') as switches:
    for IP in switches:
        Switch = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'username',
            'password': 'password'
        }
 
        net_connect = ConnectHandler(**Switch)
        
        output = net_connect.send_command('[COMMAND]')
        
        if '[]' in output:
            print(IP)

net_connect.disconnect()
