import FaBo9Axis_MPU9250
import time
import sys

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

try:
    z = 0
    y = 0
    x = 0

    while True:
        # accel = mpu9250.readAccel()
        # print (") ax = " , ( accel['x'] ))
        # print (" ay = " , ( accel['y'] ))
        # print (" az = " , ( accel['z'] ))
        gyro = mpu9250.readGyro()
        # print (" gx = " , ( gyro['x'] ))
        # print (" gy = " , ( gyro['y'] ))
        # print (" gz = " , ( gyro['z'] ))
        z = gyro['z']
        y = gyro['y']
        x = gyro['x']
        # mag = mpu9250.readMagnet()
        # print (" mx = " , ( mag['x'] ))
        # print (" my = " , ( mag['y'] ))
        # print (" mz = " , ( mag['z'] ))
        print(x,y,z)

        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()