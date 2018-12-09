import numpy as np

################################################################################
#                                                                              #
# Base class for robots                                                        #
#    - robot has only 3 actions                                                #
#         - forward, turn left, turn right                                     #
#    - robot must provide an observation of continous distances to objects     #
#         - if readings are 90 degrees apart, observation space = 360/90 = 4   #
#         - if readings are 15 degrees apart, observation space = 360/15 = 24  #
#                                                                              #
################################################################################

class QBot:
    def action_space(self):         # forward, turn left, turn right
        return 3                    # change this if your robot has more moves!

    def observation_space(self):
        return self.sensor_sectors  # the number of sensor readings per sweep

    def sample(self):
        return np.random.randint(self.action_space())
