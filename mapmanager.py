from direct.showbase.ShowBase import ShowBase


class Mapmanager():

    def __init__(self):
        self.model = 'block'
        self.texture = 'stone.png'
        self.colors = [
            (0.4, 0.4, 0.4, 1),
            (0.2, 0.2, 0.3, 1),
            (0.1, 0.4, 0.4, 1),
            (0.4, 0.4, 0.1, 1)
        ]

        self.startnew()

    def getcolor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]

    def startnew(self):
        self.land = render.attachNewNode("Land")

    def add_block(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color = self.getcolor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startnew()

    def loadLand(self, filename):
        self.clear()
        with open(filename, 'r') as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.add_block((x, y, z0))
                    x += 1
                y += 1
        return x, y







