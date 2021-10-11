# PicoPackages
## Intro
This repository contains different packages, drivers and modules for Raspberry Pi Pico written in MicroPython

## bluetooth.py
### HC05
HC05 is simple driver for HC-05 bluetooth module that implements simplified data reads and writes to module.
#### Constructor parameters
- state_pin_num - state pi number of HC-05 module. Used to check if connection has been established to another BT device. DEFAULT: None
- CHECK_CONNECTION - boolean parameter. If set to false driver will not check connection prior to writing or reading data regardless if state_pin_num has been passed. If state_pin_num is not passed then CHECK_CONNECTION will be set to False. DEFAULT: True
- BAUDRATE - currently not in use. DEFAULT: 9600
#### Available methods
- read_data(READ_TIMEOUT = 60) - Will block current thread until any data is read from buffer or READ_TIMEOUT is exceeded. If state_pin is initialized and CHECK_CONNECTION set to True method will wait until connection is established.
- send_data() - Will write data to HC-05 module buffer to be sent to paired device. If state_pin initialized and CHECK_CONNECTION set to True method will wait until connection is established.
- wait_for_connection(WAIT_CONNECTION_TIMEOUT = 60) - Will wait until connection is established with another BT device (state_pin.value() == 1). Raises ConnectionTimeoutException if WAIT_CONNECTION_TIMEOUT is exceeded. Unblocks thread if connection is established. Raise StatePinNotInitializedException if state_pin is not initialized.