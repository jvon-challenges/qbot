from rlbotenv import *
from qvbot import *
from qhwbot import *


########### Train virtually, then run physically ###############################

########### Train the q-table using a virtual bot ##############################
e = RlBotEnv(QvBot(3,12))  # sensor reads @ 360/3=120 degrees per reading
                           # robot turns @ 360/12=30 degrees per turn

# create the q-table
q = np.random.rand(e.bot.observation_space(), e.bot.action_space())

# try changing these hyper-parameters...
explore = 0.1   # exploration rate (odds of taking a random action)
alpha = 0.1     # learning rate (proportional weight of new v. old information)
gamma = 0.9     # discount rate (relative value of future v. current reward)

for n in range(1000):
    state = e.reset()
    done = False
    while not done:
        if np.random.random() < explore:   # explore the state-action space
            action = e.bot.sample()        # ...random action
        else:                              # exploit the info in the q-table
            action = np.argmax(q[state])   # ...best known action
        next_state, reward, done = e.step(action)
        # update the q-table (see https://en.wikipedia.org/wiki/Q-learning)
        q[state][action] = (1-alpha) * q[state][action] + alpha * (reward + gamma * np.max(q[next_state]))
        state = next_state
    print(n)
print(q)

########### Use the resulting q-table to run the physical bot ##################
physical_bot = QHwBot(3,12))

for n in range(100):
    done = False
    while not done:
        observation = physical_bot.get_distance()
        state = np.argmin(observation)
        action = np.argmax(q[state])
        physical_bot.move(action)
        done = min(observation) < physical_bot.goal()
