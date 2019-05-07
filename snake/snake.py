import pygame
import random


class Board:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.body=[[0,0]]
        self.length=3
        self.dir=2
        self.isDead=False
        self.food=[0,10]
    def turn(self, dir):
        self.dir+=dir
        self.dir=self.dir%4
        if(self.dir==-1):
            self.dir=3
    def die(self):
        self.isDead=True
    def randomizeFood(self):
        self.food=[random.randint(0,self.width),random.randint(0,self.height)]
    def run(self):
        prevHead=self.body[0];
        newHead=[]
        if(self.dir==0):
            newHead=[prevHead[0],prevHead[1]-1]
        elif(self.dir==1):
            newHead=[prevHead[0]+1,prevHead[1]]
        elif(self.dir==2):
            newHead=[prevHead[0],prevHead[1]+1]
        elif(self.dir==3):
            newHead=[prevHead[0]-1,prevHead[1]]

        if(newHead[0]<0 or newHead[1]<0 or newHead[0]>=self.width or newHead[1]>=  self.height):
            self.die()

        if(newHead[0]==self.food[0] and newHead[1]==self.food[1]):
            self.length+=2
            self.randomizeFood()

        for tile in self.body:
            if(tile[0]==newHead[0] and tile[1]==newHead[1]):
                self.die();

        self.body.insert(0,newHead)

        while(len(self.body)>self.length):
            del self.body[-1]
    def draw(self):
        pygame.draw.rect(screen, (0,   255,   0), [self.food[0]*10,self.food[1]*10,10,10])

        for tile in self.body:
            pygame.draw.rect(screen, (255,   0,   0), [tile[0]*10,tile[1]*10,10,10])
        pygame.display.flip();

    def getOutput():
        #food is -1, body is 1, head is 2
        output=[0]*(width*height);

        output[food[1]*width+food[0]]=-1#head

        for tile in self.body:
            output[tile[1]*width+tile[0]]=1

        output[body[0][1]*width+body[0][0]]=2#head








board=Board(10,10)
print(board.getOutput)
pygame.init()
screen = pygame.display.set_mode((500,500))
done = False
if __name__ == "__main__":
    while not done:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((255, 255, 255))
        if(not board.isDead):
            board.run();
        board.draw();
    pygame.quit()
