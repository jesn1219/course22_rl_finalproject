import numpy as np
from tqdm import tqdm

def calculate_performance(episodes, env, agent):

    episodic_returns = []
    
    for epi in tqdm(range(episodes)):
        
        s = env.reset()

        done = False
        cum_reward = 0.0

        while not done:    
            action = agent.action(s)
            ns, reward, done, _ = env.step(action)
            cum_reward += reward
            s = ns
        
        episodic_returns.append(cum_reward)
                    
    return np.sum(episodic_returns)

def calculate_sample_efficiency(episodes, env, agent):

    episodic_returns = []
    timestep = 0
    
    timestep = 0
    for epi in tqdm(range(episodes)):
        s = env.reset()
        done = False
        cum_reward = 0.0        


        while not done:  
            timestep += 1
            action = agent.action(s)
            ns, reward, done, _ = env.step(action)
            cum_reward += reward
            #s = ns
            # saving reward and is_terminals
            if s.any() :

                experience = [reward, done, s, ns]
                agent.buffer.update(experience)
            s = ns
            #####################
            # If your agent needs to update the weights at every time step, complete your update process in this area.
            # e.g., agent.update()
            if (timestep) % 5 ==0:
                agent.train()
        agent.buffer.trace_init()


            #####################
        #####################
        # elif your agent needs to update the weights at the end of every episode, complete your update process in this area.
        # e.g., agent.update()


        #####################
        if cum_reward > 0 :
            print(cum_reward)
        
        episodic_returns.append(cum_reward)
                
    return np.sum(episodic_returns)

