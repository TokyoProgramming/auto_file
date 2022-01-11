# importing the subprocess module
import subprocess


def get_ssid():

    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

    devices = devices.decode("ascii")
    devices = devices.replace("\r", "")
    ls = devices.split("\n")

    ls = ls[4:]
    ssids = []
    x = 0
    while x < len(ls):
        if x % 5 == 0:
            ssids.append(ls[x])
        x += 1

    print(devices)

    return devices


get_ssid()


def get_password():

    data = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    # print(profiles)

    for i in profiles:
        results = subprocess.check_output(
            ['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1]
                   for b in results if "Key Content" in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
    return results[0]


get_password()
