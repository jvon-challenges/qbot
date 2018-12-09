import math
import numpy as np

################################################################################
#                                                                              #
# Learning environment for Q-Bot:                                              #
#    - creates discrete observations from continous sensor readings:           #
#         - sensor = [1000,1200,1110,90,1150,880]                              #
#         - observation = argmin(senor) = 3 (the index of the lowest reading)  #
#    - calculates reward based on change in distance to nearest object         #
#    - relies on robot to provide sensor readings, action space, actions       #
#                                                                              #
################################################################################

class RlBotEnv:

    def __init__(self, bot):
        self.bot = bot                  # could be a physical or virtual robot

    def reset(self):
        self.bot.reset()
        obs = self.bot.get_distance()   # returns continous distances
        self.min_distance = min(obs)    # for use in first call to step()
        return np.argmin(obs)           # convert to discrete observation

    def step(self, action):
        self.bot.move(action)
        obs = self.bot.get_distance()        # get continous distances
        reward = self.min_distance-min(obs)  # reward = reduction in distance
        self.min_distance = min(obs)         # for use in next call to step()
        state = np.argmin(obs)               # convert to discrete state
        done = min(obs) < self.bot.goal()    # find an object?
        return state, reward, done
