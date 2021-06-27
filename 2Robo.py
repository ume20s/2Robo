#! /usr/bin/env python
import webiopi
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

def setup():
	m_deg = int((650-150)*90/180+150)
	pwm.set_pwm(0, 0, m_deg)
	pwm.set_pwm(1, 0, m_deg)
	pwm.set_pwm(2, 0, m_deg)
	pwm.set_pwm(3, 0, m_deg)
	pwm.set_pwm(4, 0, m_deg)
	pwm.set_pwm(5, 0, m_deg)

@webiopi.macro
def MoveServo( Pos, Ang ):
	pwm.set_pwm(int(Pos), 0, int(Ang))
