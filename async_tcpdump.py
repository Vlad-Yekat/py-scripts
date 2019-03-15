# requirement python 3.7.1
# template for change data in parallel executions
import asyncio
from scapy.all import rdpcap
from scapy.layers.dns import DNSRR


async def inner_proc(file_dump):
    packets = rdpcap(file_dump)

    # Let's iterate through every packet
    for packet in packets:
        # We're only interested packets with a DNS Round Robin layer
        if packet.haslayer(DNSRR):
            # If the an(swer) is a DNSRR, print the name it replied with.
            if isinstance(packet.an, DNSRR):
                print(file_dump, packet.an.rrname)
                await asyncio.sleep(1)

async def main():
    futures = []
    files_dump = ['example.pcap', 'example2.pcap']  # etc
    for file_dump in files_dump:
        future = asyncio.create_task(inner_proc(file_dump))
        futures.append(future)
    for future in futures:
        await future

asyncio.run(main())