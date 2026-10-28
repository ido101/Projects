import pyxel

BALL_SIZE = 5
HANDLE_HEIGHT = 24
HANDLE_WIDTH = 5
HANDLE_SPEED = 4
BALL_SPEED = 2

p1 = {'x': 10, 'y': 10, 'vy': 0}
p2 = {'x': 240, 'y': 10, 'vy': 0}
ball = {'x': 113, 'y': 113, 'vx': BALL_SPEED, 'vy': BALL_SPEED}

def update():
    if pyxel.btn(pyxel.KEY_UP):
        p1['vy'] = -HANDLE_SPEED
    if pyxel.btn(pyxel.KEY_DOWN):
        p1['vy'] = HANDLE_SPEED
    if pyxel.btn(pyxel.KEY_W):
        p2['vy'] = -HANDLE_SPEED
    if pyxel.btn(pyxel.KEY_S):
        p2['vy'] = HANDLE_SPEED

    if (ball['y'] - BALL_SIZE) <= 0:
        ball['vy'] = BALL_SPEED

    if (ball['y'] + BALL_SIZE) >= pyxel.height:
        ball['vy'] = -BALL_SPEED

    if (p1['y'] < ball['y'] < p1['y'] + HANDLE_HEIGHT) and (p1['x'] < (ball['x'] - BALL_SIZE) < p1['x'] + HANDLE_WIDTH):
        ball['vx'] = BALL_SPEED

    if (p2['y'] < ball['y'] < p2['y'] + HANDLE_HEIGHT) and (p2['x'] < (ball['x'] + BALL_SIZE) < p2['x'] + HANDLE_WIDTH):
        ball['vx'] = -BALL_SPEED

    for player in [p1, p2]:
        if 0 < player['vy'] + player['y'] < (pyxel.width - HANDLE_HEIGHT):
            player['y'] += player['vy']

    ball['x'] += ball['vx']
    ball['y'] += ball['vy']


def draw():
    pyxel.cls(0)
    pyxel.circ(ball['x'], ball['y'], BALL_SIZE, 3)
    for player in [p1, p2]:
        pyxel.rect(player['x'], player['y'], HANDLE_WIDTH, HANDLE_HEIGHT, 5)


pyxel.init(256, 256)
pyxel.run(update, draw)
