
from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from smoot_motors import SmooteDrive


class Motors:

    def __init__(self):
        # "X_x_r" means rear motor
        # "X_x_f" means front motor
        factory = PiGPIOFactory(host='192.168.88.255')
        self.PWM_l_r = PWMLED(17, pin_factory=factory)
        self.DIR_l_r = PWMLED(4, pin_factory=factory)
        self.PWM_r_r = PWMLED(3, pin_factory=factory)
        self.DIR_r_r = PWMLED(2, pin_factory=factory)
        # "X_x_x_f" means forward direction
        # "X_x_x_b" means backward direction
        self.DIR_l_l = PWMLED(26, pin_factory=factory)
        self.PWM_l_f = PWMLED(19, pin_factory=factory)
        self.DIR_r_l = PWMLED(13, pin_factory=factory)
        self.PWM_r_f = PWMLED(6, pin_factory=factory)

        self.Servo_r = Servo(27, pin_factory=factory)
        self.Servo_l = Servo(22, pin_factory=factory)
        self.value = 0
        self.div = 6.25
        self.s = SmooteDrive()

    def move_forward(self):
        pwm = self.s.run(100)
        self.DIR_r_r.off()
        self.DIR_l_r.off()
        self.PWM_r_r.value = pwm
        self.PWM_l_r.value = pwm

        self.DIR_r_l.on()
        self.PWM_l_f.value = pwm
        self.DIR_l_l.off()
        self.PWM_r_f.value = pwm

    def move_backward(self):
        pwm = self.s.run(100)
        self.DIR_r_r.on()
        self.DIR_l_r.on()
        self.PWM_r_r.value = pwm
        self.PWM_l_r.value = pwm

        self.DIR_l_l.on()
        self.PWM_l_f.value = pwm
        self.DIR_r_l.off()
        self.PWM_r_f.value = pwm

    def rotate_left(self):
        self.DIR_r_r.off()
        self.DIR_l_r.on()
        self.PWM_r_r.on()
        self.PWM_l_r.on()

        self.DIR_l_l.on()
        self.PWM_l_f.on()
        self.DIR_r_l.on()
        self.PWM_r_f.on()

    def rotate_right(self):
        self.DIR_r_r.on()
        self.DIR_l_r.off()
        self.PWM_r_r.on()
        self.PWM_l_r.on()

        self.DIR_l_l.off()
        self.PWM_l_f.on()
        self.DIR_r_l.off()
        self.PWM_r_f.on()

    def stop(self):
        self.s.run(0)
        self.PWM_r_r.off()
        self.PWM_l_r.off()
        self.PWM_l_f.off()
        self.PWM_r_f.off()

    def set_servo_value(self, value_l, value_r):
        self.Servo_r.value = value_r
        self.Servo_l.value = value_l

    def set_servo_max(self):
        self.Servo_r.max()
        self.Servo_l.min()

    def set_servo_min(self):
        self.Servo_r.min()
        self.Servo_l.max()

