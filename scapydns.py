from scapy.all import DNS, DNSQR, IP, sr1, UDP

dnsRequest = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname='www.google.com')
dnsResponse = sr1(dnsRequest)
                                                 
print(dnsResponse[DNS].summary())
