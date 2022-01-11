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
LENOVO_IP_ADDRESS = os.getenv('LENOVO_IP_ADDRESS')
LENOVO_MAC_ADDRESS = os.getenv('LENOVO_MAC_ADDRESS')
MIKA_PC_IP_ADDRESS = os.getenv('MIKA_PC_IP_ADDRESS')
MIKA_PC_MAC_ADDRESS = os.getenv('MIKA_PC_MAC_ADDRESS')
KOJI_IP_ADDRESS = os.getenv('KOJI_IP_ADDRESS')
KOJI_MAC_ADDRESS = os.getenv('KOJI_MAC_ADDRESS')

IP_ADDRESS = [DESKTOP_ID_ADDRESS, YUSUKE_IP_ADDRESS,
              MIKA_IP_ADDRESS, LENOVO_IP_ADDRESS, MIKA_PC_IP_ADDRESS, KOJI_IP_ADDRESS]


MAC_ADDRESS = [DESKTOP_MAC_ADDRESS, YUSUKE_MAC_ADDRESS,
               MIKA_MAC_ADDRESS, LENOVO_MAC_ADDRESS, MIKA_PC_MAC_ADDRESS, KOJI_MAC_ADDRESS]

NAME = ['DESKTOP', 'YUSUKE', 'MIKA', 'LENOVO', 'MIKA_PC', 'KOJI']


df = pd.DataFrame(list(zip(IP_ADDRESS, MAC_ADDRESS, NAME)),
                  columns=['IP', 'MAC', "NAME"])


def check_lists(list1, list2):
    if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, list1, list2), True):

        return True
    else:
        pass


def get_connected_devices():
    df_result = pd.DataFrame(
        columns=['IP', 'MAC', "NAME"])
    index = df.index
    rowLen = len(index)
    request = scapy.ARP()

    request.pdst = '192.168.0.1/24'
    broadcast = scapy.Ether()

    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout=10, verbose=1)[0]
    for element in clients:
        get_device_data = [element[1].psrc, element[1].hwsrc]
        get_device_data.append('null')

        for row in range(0, rowLen):
            get_device_data

            data_split = df.iloc[[row], 0:2]
            data_split_list = data_split.values.flatten()
            res = check_lists(get_device_data, data_split_list)

            if res == True:
                name = df['NAME'][row]
                get_device_data[-1] = name
                break

        df_result.loc[len(df_result)] = get_device_data

    return df_result


res = get_connected_devices()
print(res)
