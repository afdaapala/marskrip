import paramiko
import time

ip_address = '10.1.1.2'
username = 'cisco'
password = 'cisco'
secret = 'cisco'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print("berhasil login ke {}".format(ip_address))
conn = ssh_client.invoke_shell()

conn.send("en\n")
conn.send("cisco\n")
conn.send("conf t\n")
conn.send("int lo0\n")

conn.send("ip add 10.10.10.1 255.255.255.255\n")
time.sleep(1)

output = conn.recv(65535)
print(output.decode())

ssh_client.close()