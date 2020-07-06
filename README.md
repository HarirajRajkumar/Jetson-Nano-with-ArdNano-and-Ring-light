# Jetson-Nano-with-ArdNano-and-Ring-light

Triggers Ring light with respective to Number of Persons detected.
1 Person -> Red
2 Person -> Green
3 Person -> Blue
0 Person -> Off

Here Jetson Nano is Master and Arduino Nano acts as I2C Slave at address 0x40.

I wired pins Jetson Nano's GND, 27 (SDA), 28 (SDL) to Arduino Nano GND, A4 (SDA), A5 (SCL) and ran i2cdetect -y -r 0.

Here’s my Python code (must first install smbus module with Python Pip) -> visualization.py
( follow this link for full setup https://github.com/jkjung-avt/tensorrt_demos and prerequisite from my https://github.com/HarirajRajkumar/Person-Detection-Using-TensorRT repository )

16 Bit Ring light is connected to Arduino's Digital Pin 6. 
Upload I2C_ring_light_slave.ino to your Arduino.

Use NeoPixel_test.py to enable Jetson as I2C Master for testing the ring light.
