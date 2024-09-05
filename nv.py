#! /usr/bin/python3

import ntplib
import socket
import time
import tkinter
import tkinter.messagebox


root = tkinter.Tk()
root.title("NTPview")
root.geometry('800x600')

label = tkinter.Label(root, text = "enter hostname:")
label.grid(column=0, row=0)

entry = tkinter.Entry(root, width=64)
entry.grid(column=1, row=0)

entries = (
        'leap second indicator',
        'version',
        'mode',
        'stratum',
        'poll interval',
        'precision',
        'root delay',
        'root dispersion',
        'reference clock identifier',
        'reference timestamp',
        'originate timestamp',
        'receive timestamp',
        'transmit timestamp'
)

def put_row(nr, key, value):
    label = tkinter.Label(root, text = key)
    label.grid(column=0, row=nr)
    label = tkinter.Label(root, text = value)
    label.grid(column=1, row=nr)

def time_str(v):
    struct_now = time.localtime(v)
    us = repr(v).split('.')[1][:6]
    return time.strftime("%Y-%m-%d %H:%M:%S.{} %Z".format(us), struct_now)

def ms_value(v):
    return f'{v * 1000:.6f} ms'

def click():
    value = entry.get()

    if value == '':
        tkinter.messagebox.showinfo('hostname', 'please enter a hostname')

    else:
        try:
            ip = socket.gethostbyname(value)
            print(ip)
            
            c = ntplib.NTPClient()
            response = c.request(ip, version=3)

            put_row(3, 'leap second indicator', f'{ntplib.leap_to_text(response.leap)}')
            put_row(4, 'version', f'{response.version}')
            put_row(5, 'mode', f'{ntplib.mode_to_text(response.mode)}')
            put_row(6, 'stratum', f'{ntplib.stratum_to_text(response.stratum)}')
            put_row(7, 'poll interval', f'{response.poll}')
            put_row(8, 'precision', f'{response.precision}')
            put_row(9, 'root delay', f'{ms_value(response.root_delay)}')
            put_row(10, 'root dispersion', f'{ms_value(response.root_dispersion)}')
            put_row(11, 'reference id', f'{ntplib.ref_id_to_text(response.ref_id)}')
            put_row(12, 'offset', f'{ms_value(response.offset)}')
            put_row(13, 'delay', f'{ms_value(response.delay)}')
            put_row(14, 'transmit timestamp', f'{time_str(response.tx_time)}')
            put_row(15, 'receive timestamp', f'{time_str(response.recv_time)}')
            put_row(16, 'originate timestamp', f'{time_str(response.orig_time)}')
            put_row(17, 'reference timestamp', f'{time_str(response.ref_time)}')

        except socket.gaierror as e:
            tkinter.messagebox.showinfo('hostname', f'hostname invalid: {e}')

button = tkinter.Button(root, text = "Probe NTP server", command=click)
button.grid(column=0, row=1)

entry.focus_set()

root.mainloop()
