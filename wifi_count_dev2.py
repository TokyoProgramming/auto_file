from pandas._libs.missing import NA
import scapy.all as scapy
import os
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import functools

load_dotenv()

DESKTOP_ID_ADDRESS = os.getenv('DESKTOP_IP_ADDRESS')
DESKTOP_MAC_ADDRESS = os.getenv('DESKTOP_MAC_ADDRESS')
YUSUKE_IP_ADDRESS = os.getenv('YUSUKE_IP_ADDRESS')
YUSUKE_MAC_ADDRESS = os.getenv('YUSUKE_MAC_ADDRESS')
MIKA_IP_ADDRESS = os.getenv('MIKA_IP_ADDRESS')
MIKA_MAC_ADDRESS = os.getenv('MIKA_MAC_ADDRESS')


IP_ADDRESS = [DESKTOP_ID_ADDRESS, YUSUKE_IP_ADDRESS, MIKA_IP_ADDRESS]
MAC_ADDRESS = [DESKTOP_MAC_ADDRESS, YUSUKE_MAC_ADDRESS, MIKA_MAC_ADDRESS]
NAME = ['DESKTOP', 'YUSUKE', 'MIKA']


df = pd.DataFrame(list(zip(IP_ADDRESS, MAC_ADDRESS, NAME)),
                  columns=['IP', 'MAC', "NAME"])


test_list = ['192.168.0.5', '70:cd:0d:b0:70:f2']
data_split = df.iloc[[0], 0:2]
data_split_list = data_split.values.flatten()


if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, test_list, data_split_list), True):
    print("The lists l1 and l2 are the same")


# request = scapy.ARP()

# request.pdst = '192.168.0.1/24'
# broadcast = scapy.Ether()

# broadcast.dst = 'ff:ff:ff:ff:ff:ff'

# request_broadcast = broadcast / request
# clients = scapy.srp(request_broadcast, timeout=10, verbose=1)[0]
# for element in clients:
#     get_device_data = [element[1].psrc, element[1].hwsrc]
