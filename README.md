# PicoPackages
## Intro
This repository contains different packages, drivers and modules for Raspberry Pi Pico written in MicroPython

## bluetooth.py
### HC05
HC05 is simple driver for HC-05 bluetooth module that implements simplified data reads and writes to module. Data is written with header that defines actual data message length delimited with colon (:).
Sample data = 13:thatGreenFrog.
#### Constructor parameters
- state_pin_num - state pi number of HC-05 module. Used to check if connection has been established to another BT device. DEFAULT: None
- CHECK_CONNECTION - boolean parameter. If set to false driver will not check connection prior to writing or reading data regardless if state_pin_num has been passed. If state_pin_num is not passed then CHECK_CONNECTION will be set to False. DEFAULT: True
- BAUDRATE - currently not in use. DEFAULT: 9600
#### Available methods
- read_data(READ_TIMEOUT = 60) - Will block current thread until any data is read from buffer or READ_TIMEOUT is exceeded. If state_pin_num is passed and CHECK_CONNECTION set to True method will wait until connection is established.
- send_data() - will write data to HC-05 module buffer to be sent to paired device. If state_pin_num is passed and CHECK_CONNECTION set to True method will wait until connection is established.
- wait_for_connection(WAIT_CONNECTION_TIMEOUT = 60) - method will wait until connection is established with another BT device (state_pin.value() == 1) and either raise ConnectionTimeoutException if WAIT_CONNECTION_TIMEOUT is exceeded or unblock thread if connection is established. If state pin is not initialized, method will raise StatePinNotInitializedException