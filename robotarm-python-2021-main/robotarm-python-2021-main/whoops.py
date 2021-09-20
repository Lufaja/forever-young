from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

for x in range(0,9):
    robotArm.moveRight()
for move in range(0, 9):
    for left in range(0, move):
        robotArm.moveLeft()
    robotArm.grab()
    for right in range(0, move):
        robotArm.moveRight()
    robotArm.drop()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()