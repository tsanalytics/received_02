radio.onReceivedString(function (receivedString) {
    if (receivedString == "Up") {
        if (angle > 10) {
            maqueen.servoRun(maqueen.Servos.S1, 10)
            angle += -3
            basic.pause(100)
        }
    } else if (receivedString == "Down") {
        if (angle < 170) {
            maqueen.servoRun(maqueen.Servos.S1, 170)
            angle += 3
            basic.pause(100)
        }
    } else if (receivedString == "Stop") {
        maqueen.motorStop(maqueen.Motors.All)
    }
})
radio.onReceivedValue(function (name, value) {
    if (name == "F") {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, Math.map(value, 550, 1024, 10, 255))
    } else if (name == "B") {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, Math.map(value, 1, 450, 255, 10))
    } else if (name == "L") {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, Math.map(value, 1, 450, 255, 40))
    } else if (name == "R") {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, Math.map(value, 550, 1024, 40, 255))
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
    }
})
let angle = 0
radio.setGroup(1)
angle = 90
maqueen.servoRun(maqueen.Servos.S1, 90)
