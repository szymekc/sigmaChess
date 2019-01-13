from pymunk import *

class Physics:
    def __init__(self):
        self.space=Space()
        self.space.gravity= 0.0,-900.0

        shape= Segment(self.space.static_body,(0,0),(10,0),1.0)
        shape.friction=1.0
        self.space.add(shape)


        self.figures= [[None for s in range(8)] for p in range(8)]
        

    def initFigures(self):
        for x in range(8):
            for y in range(8):
                field= self.board.getPiece(x,y)
                if(field is not None):
                    body= Body(10,10)
                    body.position=x,y

                    self.figures[x][y]=body

                    shape= Circle(body,1)
                    shape.collision_type=2
                    self.space.add(body,shape)
                    


    def BindToBoard(self, board):
        self.board= board
        self.initFigures()

    def run(self):
        self.space.step(0.0001)

    def BoardChanged(self):
        self.initFigures()



PhysicsSingleton= Physics()