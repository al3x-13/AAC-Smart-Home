import os
import serial
from time import sleep


class SerialController:
    controller = None
    # Serial object
    port = None
    # Baud rate
    baud_rate = 0
    # Read timeout in seconds
    timeout = 0

    # Serial Connection Setup
    def __init__(self, device_port=None, baud_rate = 9600, timeout = 0):
        self.port = device_port
        self.baud_rate = baud_rate
        self.timeout = timeout

        # Sets default device port values for windows and linux if not specified
        if self.port is None:
            if os.name == 'nt':
                self.port = 'COM3'
            
            if os.name == 'posix':
                self.port = '/dev/ttyUSB0'

        try:
            self.controller = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=self.timeout)
        except serial.SerialException:
            print("Could not connect to the specified device!\n"
                  "Try to pass the device port as a program argument and make sure the port has RW permissions "
                  "and that it isn't currently being used by any other application.")
            exit()

        sleep(3)

    # Close Serial Connection
    def close(self):
        self.controller.close()

    # Sends a command to the device
    def send_command(self, command: str):
        data = command + "\n"
        self.controller.write(data.encode())

    # Receives response to a command from the device
    def receive_command(self, op_code: str) -> str:
        data = self.controller.readline()
        data = data.decode().split('$')
        op_code = data[0]

        # Error handling
        try:
            cmd_data = data[1]

            if op_code == op_code:
                return cmd_data
        except IndexError:
            return None

        return None
