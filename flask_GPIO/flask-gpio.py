from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
MOTOR_A_EN = 37
MOTOR_A_PWM = 35
MOTOR_B_EN = 38
MOTOR_B_PWM = 36
MOVETIME = 0.8
DEFAULT_SPEED = 50.0
GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTOR_A_EN,GPIO.OUT)
GPIO.setup(MOTOR_A_PWM,GPIO.OUT)
GPIO.setup(MOTOR_B_EN,GPIO.OUT)
GPIO.setup(MOTOR_B_PWM,GPIO.OUT)

motorA = GPIO.PWM(MOTOR_A_PWM,2000)
motorB = GPIO.PWM(MOTOR_B_PWM,2000)

motorA.start(0)
motorB.start(0)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html')

@app.route("/up", methods=['POST'])
def up():
    print("up")
    motorA.ChangeDutyCycle(DEFAULT_SPEED)
    motorB.ChangeDutyCycle(DEFAULT_SPEED)
    GPIO.output(MOTOR_A_EN, GPIO.HIGH)
    GPIO.output(MOTOR_B_EN, GPIO.LOW)
    time.sleep(MOVETIME)
    motorA.ChangeDutyCycle(0)
    motorB.ChangeDutyCycle(0)
    return render_template('main.html')

@app.route("/down", methods=['POST'])
def down():
    print("down")
    motorA.ChangeDutyCycle(DEFAULT_SPEED)
    motorB.ChangeDutyCycle(DEFAULT_SPEED)
    GPIO.output(MOTOR_A_EN, GPIO.LOW)
    GPIO.output(MOTOR_B_EN, GPIO.HIGH)
    time.sleep(MOVETIME)
    motorA.ChangeDutyCycle(0)
    motorB.ChangeDutyCycle(0)
    return render_template('main.html')

@app.route("/left", methods=['POST'])
def left():
    print("left")
    motorA.ChangeDutyCycle(DEFAULT_SPEED)
    motorB.ChangeDutyCycle(DEFAULT_SPEED)
    GPIO.output(MOTOR_A_EN, GPIO.LOW)
    GPIO.output(MOTOR_B_EN, GPIO.LOW)
    time.sleep(MOVETIME)
    motorA.ChangeDutyCycle(0)
    motorB.ChangeDutyCycle(0)
    return render_template('main.html')

@app.route("/right", methods=['POST'])
def right():
    print("right")
    motorA.ChangeDutyCycle(DEFAULT_SPEED)
    motorB.ChangeDutyCycle(DEFAULT_SPEED)
    GPIO.output(MOTOR_A_EN, GPIO.HIGH)
    GPIO.output(MOTOR_B_EN, GPIO.HIGH)
    time.sleep(MOVETIME)
    motorA.ChangeDutyCycle(0)
    motorB.ChangeDutyCycle(0)
    return render_template('main.html')

@app.route("/stop", methods=['POST'])
def stop():
    print("stop")
    return render_template('main.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
