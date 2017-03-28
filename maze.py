import cellular
import random
import time

class Cell(cellular.Cell):
  wall=False
  trail=False
  goal=False

  def colour(self):
    if self.wall: return 'black'
    elif self.goal: return 'magenta'
    elif self.trail: return 'green'
    else: return 'white'

  def load(self,text):
    if text==' ':
      self.wall=False
    elif text=='G':
      self.goal=True
    elif text=='S':
      self.world.addAgent(agent,cell=self)
    else:
      self.wall=True


class Agent(cellular.Agent):
  colour='blue'

  def update(self):
    self.cell.trail=True

    if self.leftCell.wall==False:
      self.turnLeft()
      self.goForward()
    elif self.aheadCell.wall==False:
      self.goForward()
    elif self.rightCell.wall==False:
      self.turnRight()
      self.goForward()
    else:
      self.turnAround()




agent=Agent()
world=cellular.World(Cell,filename='maze1.txt',directions=4)

world.display.activate(size=5)
world.display.pause()

while 1:
  world.update()
  if agent.cell.goal==True:
    world.display.pause()
    break



