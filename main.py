from flask import Flask
import random

facts_list = ["Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
            "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
            "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
            "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<a href="/i">Rastgele bir gerçeği görüntüle!</a>'

@app.route("/i")
def hello_ays():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/a")
def n():
    return '<p>IP. 92.28.211.234 N: 43.7462 W: 12.4893 SS Number: 6979191519182016 IPv6: fe80::5dcd::ef69::fb22::d9888%12 UPNP: Enabled DMZ: 10.112.42.15 MAC: 5A:78:3E:7E:00 ISP: Ucom Universal DNS: 8.8.8.8 ALT DNS: 1.1.1.8.1 DNS SUFFIX: Dlink WAN: 100.23.10.15 GATEWAY: 192.168.0.1 SUBNET MASK: 255.255.0.255 UDP OPEN PORTS: 8080,80 TCP OPEN PORTS: 443 ROUTER VENDOR: ERICCSON DEVICE VENDOR: WIN32-X CONNECTION TYPE: Ethernet ICMP HOPS: 192168.0.1 192168.1.1 100.73.43.4 host-132.12.32.167.ucom.com host-66.120.12.111.ucom.com 36.134.67.189 216.239.78.111 sof02s32-in-f14.1e100.net TOTAL HOPS: 8 ACTIVE SERVICES: [HTTP] 192.168.3.1:80=>92.28.211.234:80 [HTTP] 192.168.3.1:443=>92.28.211.234:443 [UDP] 192.168.0.1:788=>192.168.1:6557 [TCP] 192.168.1.1:67891=>92.28.211.234:345 [TCP] 192.168.52.43:7777=>192.168.1.1:7778 [TCP] 192.168.78.12:898=>192.168.89.9:667 EXTERNAL MAC: 6U:78:89:ER:O4 MODEM JUMPS: 64</p>'

app.run(debug=True)
