from netmiko import ConnectHandler
from getpass import getpass # import os --> os.environ["RELEVANT_VAR"]

# exception handling!

def main():
    cisco_switch = {
    'device_type': 'cisco_ios',
    'host': input('Device IP or hostname: '),
    'username': input('Username: '),
    'password': getpass('Password: '),
    'port': 22, # optional
    # a manual login throws netmiko out of enable mode (connection remains)
    'secret': getpass('Enable password: '), # optional, enable password
    } 

    net_connect = ConnectHandler(**cisco_switch) # show ssh --> 1x in/out
    
    mac_addresses = net_connect.send_command("show mac address-table dynamic")
    arp_table = net_connect.send_command("show arp")
    int_up_descr = net_connect.send_command("show int descr | i up")
    
    net_connect.disconnect() # show ssh --> in/out pair now gone
    
    print(mac_addresses)
    print(arp_table)
    print(int_up_descr)

if __name__ == "__main__":
    main()
