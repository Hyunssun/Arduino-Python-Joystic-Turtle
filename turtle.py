from Arduino import Arduino
import time
import turtle as t

board = Arduino('115200')

JOY_Y = 0
JOY_X = 1
JOY_SW = 2

BUTTON_A = 3
BUTTON_B = 4

RED = 9
GREEN = 10
BLUE = 11

board.pinMode(JOY_X, "INPUT")
board.pinMode(JOY_Y, "INPUT")
board.pinMode(JOY_SW, "INPUT")

board.digitalWrite(JOY_SW, "HIGH")

board.pinMode(BUTTON_A, "INPUT")
board.pinMode(BUTTON_B, "INPUT")

board.pinMode(RED, "OUTPUT")
board.pinMode(GREEN, "OUTPUT")
board.pinMode(BLUE, "OUTPUT")


t.title("turtle")
t.shape("turtle")
t.speed(0)
t.penup()

r = 0
g = 0
b = 0
cnt1 = 0
cnt2 = 0

while True:
    # 초기화 #################################
    if (board.digitalRead(JOY_SW)==0):
        t.clear()
        t.goto(0,0)
        t.penup()
        t.color("black")
        board.digitalWrite(RED, "LOW")
        board.digitalWrite(GREEN, "LOW")
        board.digitalWrite(BLUE, "LOW")

    # 방향 ###################################
    if (board.analogRead(JOY_X)<=10):
        t.left(10)
    elif (board.analogRead(JOY_X)>=1000):
        t.right(10)
    if (board.analogRead(JOY_Y)<=10):
        t.backward(10)
    elif (board.analogRead(JOY_Y)>=1000):
        t.forward(10)

    # 펜 #####################################
    if (board.digitalRead(BUTTON_A)):
        cnt1 += 1
        time.sleep(0.2)
        if (cnt1 % 2 == 0):
            t.penup()
        elif (cnt1 % 2 == 1):
            t.pendown()

    # 색상 ###################################
    if (board.digitalRead(BUTTON_B)):
        cnt2 += 1
        time.sleep(0.2)
        if (cnt2 % 4 == 0):
            t.color("black")
            board.digitalWrite(RED, "LOW")
            board.digitalWrite(GREEN, "LOW")
            board.digitalWrite(BLUE, "LOW")
        elif (cnt2 % 4 == 1):
            t.color("red")
            board.digitalWrite(RED, "HIGH")
            board.digitalWrite(GREEN, "LOW")
            board.digitalWrite(BLUE, "LOW")
        elif (cnt2 % 4 == 2):
            t.color("green")
            board.digitalWrite(RED, "LOW")
            board.digitalWrite(GREEN, "HIGH")
            board.digitalWrite(BLUE, "LOW")
        elif (cnt2 % 4 == 3):
            t.color("blue")
            board.digitalWrite(RED, "LOW")
            board.digitalWrite(GREEN, "LOW")
            board.digitalWrite(BLUE, "HIGH")
