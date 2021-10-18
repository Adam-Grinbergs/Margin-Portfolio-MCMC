import random


def mcmc(stock_price: float, i_margin: float, m_margin:float, rets:list,
         sims:int, days:int):
    """Given a list of historical returns, generate simulation and say whether
    the initial margin has been reduced to less than the maintenance margin
    requirement."""
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


def margin_call_price(price: float, initial_margin: float,
                      maintenance_margin: float, type: str = "long") -> float:
    """Calculates the margin call price a security based on its
    initial price, it's initial margin requirement, and its maintenance margin
    requirement, as well as the type of trade.

    Args:
        price (float): price in $/share of the security
        initial_margin (float): percentage (typically 40%) of the total
        value of the trade which must be paid for by the investor
        maintenance_margin (float): percentage requirement (typically 20%) of
        the value of the trade which the initial margin posted must exceed.
        type(str): if its a long trade or a short trade.

    Returns:
        float: share price below which a margin call is triggered and the
        investor must post additional margin or the brokerage will unwind their
        positions.
    """
    if price <= 0:
        raise ValueError("Stock price can't be negative")
    if initial_margin <= 0:
        raise ZeroDivisionError("Initial margin can't be zero")
    if maintenance_margin <= 0:
        raise ZeroDivisionError("Maintenance margin can't be zero")
    if initial_margin < maintenance_margin:
        raise ZeroDivisionError("Maintenance margin can't be greater than" +
                                " initial margin")
    if type == "long":
        margin_call_price = (price * (1 - initial_margin) /
                             (1 - maintenance_margin))
    if type == "short":
        margin_call_price = price * initial_margin / maintenance_margin
    return margin_call_price 