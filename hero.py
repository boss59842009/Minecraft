import base64


class Hero:  # клас для Гравця
    def __init__(self, pos, land):  # задаємо властивості гравцю
        self.mode = True
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(0.2, 0.4, 1, 1)
        self.hero.setScale(0.4)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):  # прикріпляємо камеру до гравця
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True

    def cameraUp(self):  # відкріпляємо камеру від гравця
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def switch_cam(self):  # перемикаємо камеру клавішою
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def check_dir(self, angle):
        ''' повертає заокруглені зміни координат X, Y,
        відповідні переміщенню у бік кута angle.
        Координата Y зменшується, якщо персонаж дивиться на кут 0,
        та збільшується, якщо дивиться на кут 180.
        Координата X збільшується, якщо персонаж дивиться на кут 90,
        та зменшується, якщо дивиться на кут 270.
            кут 0 (від 0 до 20) -> Y - 1
            кут 45 (від 25 до 65) -> X + 1, Y - 1
            кут 90 (від 70 до 110) -> X + 1
            від 115 до 155 -> X + 1, Y + 1
            від 160 до 200 -> Y + 1
            від 205 до 245 -> X - 1, Y + 1
            від 250 до 290 -> X - 1
            від 290 до 335 -> X - 1, Y - 1
            від 340 -> Y - 1
        '''
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)

    def look_at(self, angle):
        ''' повертає координати, в які переміститься персонаж, що стоїть у точці (x, y),
                 якщо він робить крок у напрямку angle'''
        x_from = int(self.hero.getX())
        y_from = int(self.hero.getY())
        z_from = int(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return x_from + dx, y_from + dy, z_from

    def just_move(self, angle):
        '''переміщається у потрібні координати у будь-якому випадку'''
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def up(self):
        self.hero.setZ(self.hero.getZ() + 1)

    def down(self):
        self.hero.setZ(self.hero.getZ() - 1)

    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True

    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)


    def accept_events(self):  # обробка подій клавіатури
        base.accept('c', self.switch_cam)
        base.accept('n', self.turn_left)
        base.accept('n' + '-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m' + '-repeat', self.turn_right)
        base.accept('w', self.forward)
        base.accept('w' + '-repeat', self.forward)
        base.accept('s', self.back)
        base.accept('s' + '-repeat', self.back)
        base.accept('a', self.left)
        base.accept('a' + '-repeat', self.left)
        base.accept('d', self.right)
        base.accept('d' + '-repeat', self.right)
        base.accept('e', self.up)
        base.accept('e' + '-repeat', self.up)
        base.accept('q', self.down)
        base.accept('q' + '-repeat', self.down)
        base.accept('z', self.changeMode)





