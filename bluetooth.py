from machine import Pin,UART,ADC
import utime


class HC05:
    
    uart = None
    READ_TIMEOUT = None
    
    def __init__(self, READ_TIMEOUT = 60, BAUDRATE = 9600):
        self.READ_TIMEOUT = READ_TIMEOUT
        self.uart = UART(0, BAUDRATE)
        
        
    def _read_data(self):
        data = b""
        if self.uart.any():
            header = self._read_header()
            data = b""
            read = self.uart.read(int(header))
            if not read == None:
                data = b"".join([data, read])
        return data.decode('utf-8')
    
    
    def _read_header(self):
        header = b""
        while True:
            read = self.uart.read(1)
            if read == b":":
                break
            elif not read == None:
                header = b"".join([header, read])
        return header.decode('utf-8')


    def wait_for_data(self):
        data = ""
        start_time = utime.ticks_ms()
        while len(data) < 1:
            if utime.ticks_ms() - start_time > self.READ_TIMEOUT * 1000:
                raise TimeoutException()
            data = self._read_data()
        return data
    
    def _write_data(self, data):
        str_data = str(data)
        self.uart.write(str(len(str_data)) + ":" + str_data)
        
        
    def send_data(self, data):
        self._write_data(data)


class TimeoutException(Exception):
    pass
