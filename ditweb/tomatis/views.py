from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Device, Log
import paramiko
import time
from datetime import datetime
import subprocess
from subprocess import Popen, PIPE
import nmap
from urllib.request import urlopen
from django.template import Context, Template


# Create your views here.

def index(request):
	all_device = Device.objects.all()
	cisco_device = Device.objects.filter(vendor="cisco")
	mikrotik_device = Device.objects.filter(vendor="mikrotik")
	last_event = Log.objects.all().order_by('-id')[:10]
	context = {
		'name': 'amar',
		'ip': 8080,
		'all_device' : len(all_device),
		'cisco_device' : len(cisco_device),
		'mikrotik_device' : len(mikrotik_device),
		'last_event': last_event,
	}
	return render(request ,'index.html', context)

def devices(request):
	all_device = Device.objects.order_by('ip_address')
	
	context = {
		'name': 'amar',
		'ip': 8080,
		'all_device' : all_device,
	}
	return render(request ,'devices.html', context)

def otomatis(request):
	all_device = Device.objects.all()
	
	context = {
		'name': 'amar',
		'ip': 8080,
		'all_device' : all_device,
	}
	return render(request ,'otomatis.html', context)


def dummy(request):
	all_device = Device.objects.all()
	
	context = {
		'name': 'amar',
		'ip': 8080,
		'all_device' : all_device,
	}
	return render(request ,'dummy.html', context)

def config(request):
	if request.method == "POST":
		selected_device_id = request.POST.getlist('device')
		mikrotik_command = request.POST['mikrotik_command'].splitlines()
		cisco_command = request.POST['cisco_command'].splitlines()
		for x in selected_device_id:
			try:
				dev = get_object_or_404(Device, pk=x)
				ssh_client = paramiko.SSHClient()
				ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh_client.connect(hostname=dev.ip_address,username=dev.username,password=dev.password)
				if dev.vendor.lower() == 'cisco':
					conn = ssh_client.invoke_shell()
					conn.send("conf t\n")
					for cmd in cisco_command:
						conn.send(cmd + "\n")
						time.sleep(1)
				else:
					for cmd in mikrotik_command:
						ssh_client.exec_command(cmd)
				log = Log(target=dev.ip_address,action="Config", status="Success", time=datetime.now(), messages="No Error")
				log.save()
			except Exception as e:
				log = Log(target=dev.ip_address,action="Config", status="Error", time=datetime.now(), messages=e)
				log.save()
		return redirect('/')

	else:
		devices = Device.objects.order_by('ip_address')
		context = {
			'devices' : devices,
			'mode' : 'Input Configuration',
		}
				

	return render(request ,'config.html', context)


def verify_result(request):
	if request.method == "POST":
		result = []
		selected_device_id = request.POST.getlist('device')
		mikrotik_command = request.POST['mikrotik_command'].splitlines()
		cisco_command = request.POST['cisco_command'].splitlines()
		for x in selected_device_id:
			try:
				dev = get_object_or_404(Device, pk=x)
				ssh_client = paramiko.SSHClient()
				ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				ssh_client.connect(hostname=dev.ip_address,username=dev.username,password=dev.password)

				if dev.vendor.lower() == 'mikrotik':
					for cmd in mikrotik_command:
						stdin,stdout,stderr = ssh_client.exec_command(cmd)
						result.append("Result on {}".format(dev.ip_address))
						result.append(stdout.read().decode())
				else:
					conn = ssh_client.invoke_shell()
					conn.send('terminal length 0\n')
					for cmd in cisco_command:
						result.append("Result on {}".format(dev.ip_address))
						conn.send(cmd + "\n")
						time.sleep(1)
						output = conn.recv(65535)
						result.append(output.decode())
				log = Log(target=dev.ip_address,action="Verify config", status="Success", time=datetime.now(), messages="No Error")
				log.save()
			except Exception as e:
				log = Log(target=dev.ip_address,action="Verify config", status="Error", time=datetime.now(), messages=e)
				log.save()
		result = '\n'.join(result)
		return render(request, 'result.html', {'result':result})
	else:

		devices = Device.objects.order_by('ip_address')
		context = {
			'devices' : devices,
			'mode' : 'View & Verify Result'
		}
		return render(request ,'config.html', context)

def log(request):
	logs = Log.objects.all()
	
	context = {
		'logs': logs,
	}
	return render(request ,'log.html', context)

def sdn(request):
	tpl_html = urlopen("https://twitter.com").read()
	tpl = Template(tpl_html)
	context = {
	'tpl': tpl,
	'tpl_html' : tpl_html,

	}
	
	return render(request ,'sdn.html', context)

def about(request):
#	cmd = '/home/amardfajri/miniconda3/bin/python /home/amardfajri/marskrip/nmapOS.py'.split()
#	spas = ''
#	pout = Popen(['sudo', '-S'] + cmd,stdin=PIPE,stderr=PIPE , universal_newlines=True, stdout=PIPE)
#	outt = pout.communicate(spas + '\n')[1]
#	xml_results = outt

	# nm = nmap.PortScanner()
	# nm.scan('172.17.1.*', '22-443') # scan host 127.0.0.1, ports from 22 to 443
	# nm.command_line() # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
	# nm.scaninfo() # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
	# nmal = nm.all_hosts() # get all hosts that were scanned
	#nms = nm['172.17.1.*'].state()
	
	context = {
		
		
	}

	return render(request ,'about.html', context)


def NMap(request):
	pout = subprocess.Popen(['nmap', '172.17.1.*', '-sP',], stdout=subprocess.PIPE)
	outt = pout.communicate(b"stdin")[0].decode('utf-8')
	xml_results = outt.splitlines()
	iter_nmap = iter(xml_results)
	next(iter_nmap)

#	nm = nmap.PortScanner()
#	mmap = nm.scan("172.17.1.*", arguments="-sP")
	context = {
		'name': 'Amar Fajri',
		'alamat': 'Pondok Betung',
		'nmap' : xml_results,
		'iter_nmap' : iter_nmap,
#		'mmap' : mmap,
	}

	return render(request ,'nmap.html', context)



