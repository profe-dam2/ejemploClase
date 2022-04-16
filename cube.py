from math import asin


import smbus
import time
# kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

# kivy3
from kivy3 import Renderer, Scene
from kivy3 import PerspectiveCamera

# geometry
from kivy3.extras.geometries import BoxGeometry
from kivy3 import Material, Mesh



# slave address
DEV_ADDR = 0x68  # device address
# register address
ACCEL_XOUT = 0x3b
ACCEL_YOUT = 0x3d
ACCEL_ZOUT = 0x3f
TEMP_OUT = 0x41
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47
PWR_MGMT_1 = 0x6b  # PWR_MGMT_1
PWR_MGMT_2 = 0x6c  # PWR_MGMT_2

bus = smbus.SMBus(1)

bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

class My3D(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.xAxisValue = 0
        self.zAxisValue = 0
        self.yAxisValue = 0
        self.zGyroAngleValue = 0
        self.yAngleValue = 0
        self.xAngleValue = 0
        self.xAxisAngleValue = 0
        self.yAxisAngleValue = 0

    def _adjust_aspect(self, *args):
        rsize = self.renderer.size
        aspect = rsize[0] / float(rsize[1])
        self.renderer.camera.aspect = aspect

    def rotate_cube(self, anglex):
        print("CAMBIANDO ANGULO")
        print((anglex * 180) / 3.1416)
        self.cube.rotation.x = (anglex * 180) / 3.1416

    def build(self):


        layout = FloatLayout()

        # create renderer
        self.renderer = Renderer()

        # create scene
        scene = Scene()

        # create default cube for scene
        cube_geo = BoxGeometry(1, 1, 1)
        cube_mat = Material()
        self.cube = Mesh(
            geometry=cube_geo,
            material=cube_mat
        )  # default pos == (0, 0, 0)
        self.cube.pos.z = -5

        # create camera for scene
        self.camera = PerspectiveCamera(
            fov=75,    # distance from the screen
            aspect=0,  # "screen" ratio
            near=1,    # nearest rendered point
            far=10     # farthest rendered point
        )

        # start rendering the scene and camera
        scene.add(self.cube)
        self.renderer.render(scene, self.camera)

        # set renderer ratio is its size changes
        # e.g. when added to parent
        self.renderer.bind(size=self._adjust_aspect)

        layout.add_widget(self.renderer)
        Clock.schedule_interval(self.myBucle, .01)

        return layout

    # 2byte read
    def read_word(adr):
        high = bus.read_byte_data(DEV_ADDR, adr)
        low = bus.read_byte_data(DEV_ADDR, adr + 1)
        val = (high << 8) + low
        return val


    # Sensor data read
    def read_word_sensor(self, adr):
        val = self.read_word(adr)
        if (val >= 0x8000):  # minus
            return -((65535 - val) + 1)
        else:  # plus
            return val


    # temperture
    def get_temp(self):
        temp = self.read_word_sensor(TEMP_OUT)
        x = temp / 340 + 36.53
        return x


    # gyro data
    # full scale range ±250 deg/s LSB sensitivity 131 LSB/deg/s -> ±250 x 131 = ±32750 LSB
    def get_gyro_data_deg(self):
        x = self.read_word_sensor(GYRO_XOUT)
        y = self.read_word_sensor(GYRO_YOUT)
        z = self.read_word_sensor(GYRO_ZOUT)

        x = x / 131.0
        y = y / 131.0
        z = z / 131.0
        return [x, y, z]


    # accel data
    # full scale range ±2g LSB sensitivity 16384 LSB/g) -> ±2 x 16384 = ±32768 LSB
    def get_accel_data_g(self):
        x = self.read_word_sensor(ACCEL_XOUT)
        y = self.read_word_sensor(ACCEL_YOUT)
        z = self.read_word_sensor(ACCEL_ZOUT)

        x = x / 16384.0
        y = y / 16384.0
        z = z / 16384.0
        return [x, y, z]

    def myBucle(self, *dt):
        temp = self.get_temp()  # temperture
        gyro_x, gyro_y, gyro_z = self.get_gyro_data_deg()  # gyro
        accel_x, accel_y, accel_z = self.get_accel_data_g()  # accel

        xGyroValue = float(gyro_x * 100) / 100 * 3.142 / 180
        yGyroValue = float(gyro_y * 100) / 100 * 3.142 / 180
        zGyroValue = float(gyro_z * 100) / 100 * 3.142 / 180
        xAxisValue = float(accel_x * 100) / 100
        yAxisValue = float(accel_y * 100) / 100
        zAxisValue = float(accel_z * 100) / 100

        # print(xGyroValue)
        # print(yGyroValue)
        # print(zGyroValue)
        # print(xAxisValue)
        # print(yAxisValue)
        # print(zAxisValue)

        self.zGyroAngleValue = self.zGyroAngleValue + zGyroValue * 0.05

        try:
            self.xAxisAngleValue = asin(min(0, max(self.yAxisValue / self.zAxisValue, -1)))
            self.yAxisAngleValue = asin(min(0, max(self.xAxisValue / self.zAxisValue, -1)))
        except:
            print("ERROR")
        self.xAngleValue = 0.98 * (
                self.xAngleValue + xGyroValue * 0.05) + 0.02 * self.xAxisAngleValue
        yAngleValue = 0.98 * (
                self.yAngleValue - yGyroValue * 0.05) + 0.02 * self.yAxisAngleValue

        print(self.xAngleValue)
        print(self.yAngleValue)
        print(self.zGyroAngleValue)

        # rotateX(xAngleValue)
        # rotateY(zGyroAngleValue)
        # rotateZ(yAngleValue)

        my3d.rotate_cube(self.xAngleValue)

        time.sleep(0.05)


my3d = My3D()
my3d.run()






s.close()
