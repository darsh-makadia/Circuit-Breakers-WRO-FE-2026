import RPi.GPIO as GPIO
from time import sleep

# ============================================================
# ROBOT SETTINGS
# ============================================================

PWM_PIN = 13
IN1_PIN = 5
IN2_PIN = 6
SERVO_PIN = 22

CENTER = 75
LEFT = 35
RIGHT = 115


# ============================================================
# GPIO
# ============================================================

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(IN1_PIN, GPIO.OUT)
GPIO.setup(IN2_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)

motor_pwm = GPIO.PWM(PWM_PIN, 1000)
motor_pwm.start(0)

servo_pwm = GPIO.PWM(SERVO_PIN, 50)
servo_pwm.start(0)


# ============================================================
# DRIVE FUNCTIONS
# ============================================================

def steer(angle):
    angle = max(LEFT, min(RIGHT, angle))
    duty = 2.5 + (angle / 180.0) * 10.0
    servo_pwm.ChangeDutyCycle(duty)
    sleep(0.05)
    servo_pwm.ChangeDutyCycle(0)


def forward(speed):
    GPIO.output(IN1_PIN, GPIO.LOW)
    GPIO.output(IN2_PIN, GPIO.HIGH)
    motor_pwm.ChangeDutyCycle(speed)


def backward(speed):
    GPIO.output(IN1_PIN, GPIO.HIGH)
    GPIO.output(IN2_PIN, GPIO.LOW)
    motor_pwm.ChangeDutyCycle(speed)


def stop():
    motor_pwm.ChangeDutyCycle(0)


def cleanup():
    stop()
    steer(CENTER)
    servo_pwm.stop()
    motor_pwm.stop()
    GPIO.cleanup()
