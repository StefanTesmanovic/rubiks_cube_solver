from environment import environment
import numpy as np
import tensorflow as tf
import random
from constants import *
import cube


draw = False
epochs = 10000
tries = 10
gamma = 1
epsilon = 0.3

model = tf.keras.Sequential([
    tf.keras.layers.Dense(5000, activation='relu', input_shape=(480,)),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(1000, activation='relu'),
    tf.keras.layers.Dense(500, activation='relu'),
    tf.keras.layers.Dense(250, activation='relu'),
    tf.keras.layers.Dense(12, activation='softmax')
])
optimizer = tf.keras.optimizers.Adam(learning_rate=0.05)

def reinforce_loss(states, actions, rewards):
    log_probs = []
    discounted_rewards = []
    cumulative_reward = 0
    for reward in reversed(rewards):
        cumulative_reward = reward + gamma * cumulative_reward
        discounted_rewards.insert(0, cumulative_reward)
    discounted_rewards = tf.convert_to_tensor(discounted_rewards, dtype=tf.float32)
    for state, action in zip(states, actions):
        probs = model(state)
        log_prob = tf.math.log(probs[0, action])
        log_probs.append(log_prob)
    log_probs = tf.convert_to_tensor(log_probs, dtype=tf.float32)
    loss = tf.reduce_mean(-log_probs * discounted_rewards)
    return loss

def test(model, scr_cnt):
    env = environment(0)
    solved = 0
    for i in range(100):
        env.reset(scr_cnt)
        while True:
            state = env.cube
            state = np.concatenate([np.eye(24)[ord(c) - ord('a')] for c in state[:-6]])
            state = state.reshape(1, -1)
            probs = model(state)
            action = tf.argmax(probs[0]).numpy()
            env.move(action)
            if env.moves_made >= min(scr_cnt+5, 30):
                break
            if env.solved():
                solved += 1
                break
    return solved/100


env = environment(0)
for scr_cnt in range(1, 30):
    print("scramble count: ", scr_cnt)
    if scr_cnt == 1: epochs = 5000
    elif scr_cnt == 2: epochs = 10000
    else: epochs = 20000
    solved = 0
    for epoch in range(epochs):
        
        if epoch % 100 == 0:
            print(epoch)
        rewards = []
        states = []
        actions = []
        env.reset(scr_cnt)
        while True:
            state = env.cube
            state =  np.concatenate([np.eye(24)[ord(c) - ord('a')] for c in state[:-6]])
            state = state.reshape(1, -1)
            states.append(state)
            probs = model(state)
            if random.random() < epsilon:
                action = tf.argmax(probs[0]).numpy()
            else:
                action = np.random.choice(np.arange(12), p=probs.numpy().flatten())
            actions.append(action)
            next_state, reward = env.move(action)
            rewards.append(reward)
            #print(env.cube)
            if env.moves_made >= min(scr_cnt+5, 30):
                break
            if env.solved():
                solved += 1
                break
        with tf.GradientTape() as tape:
            loss = reinforce_loss(states, actions, rewards)

        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    percentage = test(model, scr_cnt)
    print(percentage)
    model.save(f"my_model{percentage}-{scr_cnt}.h5")






    
    