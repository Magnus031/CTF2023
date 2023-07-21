from dns.resolver import Resolver
from dnslib import DNSRecord, QTYPE, RD, SOA, DNSHeader, RR, A
DNS=Resolver()
DNS.nameservers = ['8.8.8.8','8.8.4.4']
#使用Google公共DNS服务器地址
def resolve_dns(Domain):
    #完成resolve normarlly for common hosts
    resolver = Resolver()
    iP = resolver.query(Domain) 
    for answer in iP:
        print(answer)

def response(record, ip,ttl):
    #response 函数是用来作为回应,record为输入的DNS
    r_data = A(ip)
    ttl=60
    #low ttl
    header = DNSHeader(id=record.header.id, bitmap=record.header.bitmap, qr=1)
    #创建新的响应Header
    domain = record.q.qname
    GetA = QTYPE.reverse.get('A') or record.q.qtype
    response = DNSRecord(header, q=record.q, a=RR(domain, GetA, rdata=r_data, ttl=ttl))
    return response


domain=input("Please write your domain:")
resolve_dns(domain)


