from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
for x in range(0, 2):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for d in range(0, 2):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()