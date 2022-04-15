#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   Servo Example - Example of usage ASMpi class

.. Licence MIT
.. codeauthor:: Jan Lipovský <janlipovsky@gmail.com>, janlipovsky.cz
"""

from AMSpi import AMSpi
import socket
import sys

control = None

def stop(amspi,timesec):
    print("Stop")
    amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2, amspi.DC_Motor_3, amspi.DC_Motor_4])

def run(amspi,timesec):
    print("Adelante")
    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_3])
    amspi.run_dc_motors([amspi.DC_Motor_2, amspi.DC_Motor_4], clockwise=False)

def reverse(amspi,timesec):
    print("Reversa")
    amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_3], clockwise=False)
    amspi.run_dc_motors([amspi.DC_Motor_2, amspi.DC_Motor_4])

def izquierda(amspi,timesec):
    print("Gira izquierda")
    amspi.run_dc_motors([amspi.DC_Motor_2,amspi.DC_Motor_1], clockwise=False)
    amspi.run_dc_motors([amspi.DC_Motor_4,amspi.DC_Motor_3])

def derecha(amspi,timesec):
    print("Gira derecha")
    amspi.run_dc_motors([amspi.DC_Motor_2,amspi.DC_Motor_1])
    amspi.run_dc_motors([amspi.DC_Motor_4,amspi.DC_Motor_3],  clockwise=False)

def on_message(message):
    print('mensaje recibido '+message)

    if(message == 'AD'):
       run(control, 10)

    if(message == 'AT'):
        reverse(control,10)

    if(message == 'ST'):
        stop(control,0)

    if(message == 'DE'):
        derecha(control,10)

    if(message == 'IZ'):
        izquierda(control,10)


if __name__ == '__main__':
    # Calling AMSpi() we will use default pin numbering: BCM (use GPIO numbers)
    # if you want to use BOARD numbering do this: "with AMSpi(True) as amspi:"
    with AMSpi() as amspi:
        # Set PINs for controlling shift register (GPIO numbering)
        amspi.set_74HC595_pins(21, 20, 16)
        # Set PINs for controlling all 4 motors (GPIO numbering)
        amspi.set_L293D_pins(5, 6, 13, 19)

        control = amspi

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_adress = ('192.168.0.28', 55555)

        sock.bind(server_adress)

        sock.listen(1)

        while True:
            print >>sys.stderr, 'waiting for a connection'
            connection, client_adress = sock.accept()

            try:
                print >>sys.stderr, 'connection from', client_adress

                while True:
                    data= connection.recv(2)
                    print >>sys.stderr, 'received "%s"' % data
                    if data:
                        print >>sys.stderr, 'sending data back to the client'
                        on_message(data)
                    else:
                        print >>sys.stderr, 'no more data from ', client_adress
                        break

            finally:
                connection.close()