import numpy as np
from rlbotenv import *
from qhwbot import *

################################################################################
#                                                                              #
# Basic Q-Learning: Physical Robot                                             #
#                                                                              #
################################################################################

e = RlBotEnv(QHwBot(3,12))

# create the q-table
q = np.random.rand(e.bot.observation_space(), e.bot.action_space())

# try changing these hyper-parameters...
explore = 0.1  # exploration rate (odds of taking a random action)
alpha = 0.1    # learning rate (proportional weight of new v. old information)
gamma = 0.9    # discount rate (relative value of future v. current reward)

for n in range(10):
    state = e.reset()
    done = False
    while not done:
        if np.random.random() < explore:  # explore the state-action space
            action = e.bot.sample()       # ...random action
        else:                             # exploit the info in the q-table
            action = np.argmax(q[state])  # ...best known action
        next_state, reward, done = e.step(action)
        # update the q-table (see https://en.wikipedia.org/wiki/Q-learning)
        q[state][action] = (1-alpha) * q[state][action] + alpha * (reward + gamma * np.max(q[next_state]))
        state = next_state
