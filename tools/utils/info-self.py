#!/usr/bin/env python3

import socket
import requests


def info():
    host_name = socket.gethostname()
    local_ip = socket.gethostbyname(host_name)
    global_ip = requests.get('https://ifconfig.me').text
    print(f'HostName: {host_name}')
    print(f'Local IP: {local_ip}')
    print(f'Global IP: {global_ip}')


if __name__ == "__main__":
    info()
