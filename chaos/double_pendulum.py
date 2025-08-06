from math import cos, sin, pi
import time
import pygame
import numpy as np

# Initial conditions
d = 0.1 / 360
rotations = (
    [pi / 2, pi / 2],
    [pi / 2, pi / 2 + d]
)

# Constants
SCREEN_DIMENSION = (600, 600)
BACKGROUND_COLOR = (0, 0, 0)
PIVOT_COLOR = (1, 1, 1)
ARM_COLORS = (
    (
        (50, 50, 255),
        (100, 100, 255)
    ),
    (
        (255, 50, 50),
        (255, 100, 100)
    )
)
G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.5  # length of pendulum 1 in m
L2 = 1  # length of pendulum 2 in m
L = L1 + L2  # maximal length of the combined pendulum
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg
P = 100  # Meter to pixel conversion scale

screen = pygame.display.set_mode(SCREEN_DIMENSION)
pygame.init()
pygame.display.set_caption("Double Pendulum")
font = pygame.font.Font(None, 72)


def format_time(s):
    seconds = s // 1
    milliseconds = (s - seconds) * 1000
    minutes = seconds // 60
    seconds %= 60
    second_repr = f"{int(seconds)}" if seconds >= 10 else f"0{int(seconds)}"
    return f"{int(minutes)}:{second_repr}.{int(milliseconds)}"


def derivs(state):
    """From https://matplotlib.org/stable/gallery/animation/double_pendulum.html"""
    dydx = [0 for _ in range(len(state))]
    dydx[0] = state[1]
    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)
    dydx[2] = state[3]
    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)
    return dydx


def display_arms(r, colors):
    origin = (SCREEN_DIMENSION[0] / 2, SCREEN_DIMENSION[0] / 2)
    thetaA = r[0] + pi / 2
    a = (
        origin[0] + cos(thetaA) * L1 * P,
        origin[1] + sin(thetaA) * L1 * P,
    )
    thetaB = r[1] + pi / 2
    b = (
        a[0] + cos(thetaB) * L2 * P,
        a[1] + sin(thetaB) * L2 * P,
    )
    pygame.draw.line(screen, colors[0], origin, a, width=8)
    pygame.draw.line(screen, colors[1], a, b, width=8)
    pygame.draw.circle(screen, (255, 255, 255), origin, 5)
    pygame.draw.circle(screen, (255, 255, 255), a, 5)
    pygame.draw.circle(screen, (255, 255, 255), b, 5)


states = [
    np.array([r[0], 0, r[1], 0]) for r in rotations
]
delta = 0
elapsed_time = 0
while True:
    a = time.time()
    screen.fill(BACKGROUND_COLOR)
    for i in range(len(states)):
        y = states[i]
        y = y + np.array(derivs(y)) * delta
        states[i] = y
        rotations[i][0], rotations[i][1] = y[0], y[2]
        display_arms(rotations[i], ARM_COLORS[i])
    time_str = format_time(elapsed_time)
    time_text = font.render(time_str, True, (255, 255, 255))
    screen.blit(time_text, (SCREEN_DIMENSION[0] / 3, 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    b = time.time()
    delta = b - a
    if delta > 0.1:
        delta = 0.1
    elapsed_time += delta
