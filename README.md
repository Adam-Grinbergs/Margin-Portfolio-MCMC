# Margin-Portfolio-MCMC
A Markov Chain Monte Carlo simulator for your margin portfolio to estimate returns and margin call likelihood at different margin ratios.

The goal of this free package is to create a tool that will take in stock tickers and quantities and will compute a series of return distributions based on a few different initial margin to asset percentages (25%, 50%, 75%, etc.) and showcase the likelihood of margin call in each scenario. Hopefully it will be simple to determine an optimal amount of margin to use to invest in liquid, broad market ETFs to enhance investment returns based on your risk tolerance. 

## TODO:
- [ ] Choose schema for daily prices database of tickers and download for my stocks.
- [ ] Create distribution of returns from daily price database.
- [x] Write simulation function to randomly choose from distribution and create Markov Chain.
- [ ] Write function to calculate if margin is called, and "warning" (within 10% of margin call).
- [ ] Write function to run simulations for each scenario (no margin, 25%, 50%) and output results.
- [ ] Create visuals for each scenario and showcase differences.
- [ ] Compare this to various investment benchmarks.
