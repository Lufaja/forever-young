from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

for x in range(0,9):
    robotArm.moveRight()
for move in range(0, 9):
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()