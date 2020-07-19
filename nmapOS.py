import nmap
nm = nmap.PortScanner()
nm.scan('172.17.1.*',arguments='-O')
