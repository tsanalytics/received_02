def on_received_string(receivedString):
    global angle
    if receivedString == "Up":
        if angle > 10:
            maqueen.servo_run(maqueen.Servos.S1, angle)
            angle += -3
            basic.pause(100)
    elif receivedString == "Down":
        if angle < 170:
            maqueen.servo_run(maqueen.Servos.S1, angle)
            angle += 3
            basic.pause(100)
    elif receivedString == "Stop":
        maqueen.motor_stop(maqueen.Motors.ALL)
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    if name == "F":
        maqueen.motor_run(maqueen.Motors.ALL,
            maqueen.Dir.CW,
            Math.map(value, 550, 1024, 10, 255))
    elif name == "B":
        maqueen.motor_run(maqueen.Motors.ALL,
            maqueen.Dir.CCW,
            Math.map(value, 1, 450, 255, 10))
    elif name == "L":
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.Motors.M2,
            maqueen.Dir.CW,
            Math.map(value, 1, 450, 255, 40))
    elif name == "R":
        maqueen.motor_run(maqueen.Motors.M1,
            maqueen.Dir.CW,
            Math.map(value, 550, 1024, 40, 255))
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
radio.on_received_value(on_received_value)

angle = 0
radio.set_group(1)
angle = 90
maqueen.servo_run(maqueen.Servos.S1, angle)