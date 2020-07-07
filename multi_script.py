import paramiko
import time


devices = [
	{
		'ip_address' : '10.1.1.2',
		'vendor' : 'cisco',
		'username' : 'cisco',
		'password' : 'cisco',
		'secret' : 'cisco',

	},
	{
		'ip_address' : '10.1.1.3',
		'vendor' : 'mikrotik',
		'username' : 'admin',
		'password' : '',
	}
]

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for device in devices:
	ssh_client.connect(hostname=device['ip_address'],username=device['username'],password=device['password'])
	print("berhasil login ke {}".format(device['ip_address']))

	if device['vendor'] == 'cisco':
		conn = ssh_client.invoke_shell()
		conn.send("en\n")
		conn.send("cisco\n")
		conn.send("conf t\n")
		conn.send("int lo0\n")
		conn.send("ip add 10.10.10.1 255.255.255.255\n")
		time.sleep(1)

		output = conn.recv(65535)
		print(output.decode())
	else:
		ssh_client.exec_command("interface bridge add name loopback0\n")
		ssh_client.exec_command("ip address add address 10.10.10.2/32 interface=loopback0\n")

	ssh_client.close()