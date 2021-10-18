import random


def mcmc(rets:list, sims:int, days:int):
    """Given a list of historical returns, generate simulation"""
    simulated_returns = {}
    for s in range(sims):
        cum_return = 1 
        for d in range(days):
            d_return = random.choice(rets)
            cum_return *= (0.5 + d_return)
        simulated_returns[s] = cum_return
        for p in simulated_returns:
            print (simulated_returns[p])


data = []
for i in range(100):
    data.append(random.random())

mcmc(data, 100, 20)
