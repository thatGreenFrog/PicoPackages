# PicoPackages
## Intro
This repository contains different packages, drivers and modules for Raspberry Pi Pico written in MicroPython

## bluetooth.py
### HC05
HC05 is simple driver for HC-05 bluetooth module that implements simplified data reads and writes to module. Data is written with header that defines actual data message length delimited with colon (:).
Sample data = 13:thatGreenFrog.
#### Constructor parameters
- READ_TIMEOUT - data read timeout in seconds.
- BAUDRATE - currently not in use
#### Available methods
- wait_for_data() - will wait for data to be present in HC05 buffer. Will throw bluetooth.TimeoutException if data is not present in buffer after {READ_TIMEOUT} seconds
- send_data() - will write data to HC-05 module buffer to be sent to paired device.