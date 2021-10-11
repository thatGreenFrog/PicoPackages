from machine import Pin,UART
import utime


class HC05:
    
    uart = None
    state_pin = None
    CHECK_CONNECTION = None
    
    def __init__(self, state_pin_num = None, CHECK_CONNECTION = True, BAUDRATE = 9600):
        self.CHECK_CONNECTION = CHECK_CONNECTION and state_pin_num is not None
        self.uart = UART(0, BAUDRATE)
        if state_pin_num is not None:
            self.state_pin = Pin(state_pin_num, Pin.IN)


    # Actual method to read data from buffer
    def _read_data(self):
        if self.CHECK_CONNECTION:
            # If state_pin is initialized and CHECK_CONNECTION passed to constructor as True 
            # method will wait until connection is estableshed to another BT device
            self.wait_for_connection()
        data = None
        if self.uart.any():
            data = b""
            read = self.uart.read()
            if not read == None:
                data = b"".join([data, read])
        return data.decode('utf-8') if data is not None else None


    # Read data from buffer. If READ_TIMEOUT > 0 method will block thread until data is received or timeout exceeded
    def read_data(self, READ_TIMEOUT = 60):
        data = None
        start_time = utime.ticks_ms()
        while True:
            data = self.read_data()
            if READ_TIMEOUT == 0 or len(data) > 0:
                # If any data has been read from buffer then we return this data immidiately
                # or if READ_TIMEOUT has been set to 0, then method assumes that the user 
                # doesn't want to block the thread and returns data regardless if anything has been read from buffer
                return data
            elif utime.ticks_ms() - start_time > READ_TIMEOUT * 1000:
                # If READ_TIMEOUT > 0, then we raise ReadTimeoutException (if the timeout has been exceede)
                # so that user can handle this gracefully
                raise ReadTimeoutException()
    
    # Write data to buffer.
    def send_data(self, data):
        if self.CHECK_CONNECTION:
            # If state_pin is initialized and CHECK_CONNECTION passed to constructor as True 
            # method will wait until connection is estableshed to another BT device
            self.wait_for_connection()
        self.uart.write(str(data))


    # When HC-05 modukle state pin returns value 1 it means that connection has been established to another BT device
    # This method will block current thread until state pin returns value 1 or WAIT_CONNECTION_TIMEOUT timeout is exceeded 
    def wait_for_connection(self, WAIT_CONNECTION_TIMEOUT = 60):
        if self.state_pin == None:
            # If state pin is not initialized then we cannot check connection
            # for this reason exception is raised, so that user can handle gracefully
            raise StatePinNotInitializedException()
        start_time = utime.ticks_ms()
        while not self.state_pin.value() == 1:
            if utime.ticks_ms() - start_time > WAIT_CONNECTION_TIMEOUT * 1000:
                raise ConnectionTimeoutException()
            utime.sleep(0.1)


class HC05Exception(Exception):
    pass


class ReadTimeoutException(HC05Exception):
    pass


class ConnectionTimeoutException(HC05Exception):
    pass


class StatePinNotInitializedException(HC05Exception):
    pass
