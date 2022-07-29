#
# from gpiozero import PWMLED
# from gpiozero.pins.pigpio import PiGPIOFactory
# import time
#
# class Motors:
#
#     def __init__(self, img_width):
#         factory = PiGPIOFactory(host='192.168.88.254')
#         self.PWM_l = PWMLED(17, pin_factory=factory)
#         self.DIR_l = PWMLED(4, pin_factory=factory)
#         self.PWM_r = PWMLED(3, pin_factory=factory)
#         self.DIR_r = PWMLED(2, pin_factory=factory)
#         self.value = 0
#         self.div = 6.25
#         self.current_time = time.time()
#         self.last_time = self.current_time
#
#
#     def set_current_time(self):
#         self.current_time = time.time()
#
#     def run_motors(self):
#         self.PWM_r.value = round(self.value) / 100
#         self.PWM_l.value = round(self.value) / 100
#
#     def soft_run(self):
#         if 0 < self.value < 100:
#             if self.current_time - self.last_time >= 0.0625:
#                 self.value = self.value + self.div
#                 self.run_motors()
#
#     def main(self, dir):
#
#             if dir == "LEFT":
#                 self.PWM_r.off()
#                 self.PWM_l.on()
#                 self.value_r = 0
#                 self.value_l = 0
#
#             elif dir == "RIGHT":
#                 self.PWM_r.on()
#                 self.PWM_l.off()
#                 self.value_r = 0
#                 self.value_l = 0
#
#             elif dir == "FORWARD":
#                 self.PWM_r.on()
#                 self.PWM_l.on()
#                 self.value_r = 0
#                 self.value_l = 0
#
#             elif dir == "BACKWARD":
#                 self.PWM_r.off()
#                 self.PWM_l.off()
#                 self.value_r = 0
#                 self.value_l = 0

import time

class SmooteDrive:
    def __init__(self):
        self.current_value = 0
        self.set_value = 0
        self.current_time = time.time()
        self.initial_value = 0
        self.k = 100 / 16
        self.set_value = 0
        self.dir = 0

    def set_k(self):
        self.k = (self.set_value - self.initial_value) / 16

    def run(self, speed_value):
        if self.set_value != speed_value:
            self.set_value = speed_value
            self.set_k()
        if x := self.motors():
            return x / 100
        else:
            return speed_value / 100

    def motors(self):
        if self.initial_value != self.set_value:
            if time.time() - self.current_value >= 0.0625:
                self.initial_value += self.k
                self.current_value = time.time()
            return self.initial_value



# from multiprocessing import Process, Pipe
#
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())  # prints "[42, None, 'hello']"
#     p.join()
