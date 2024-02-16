#%%
import yfinance as yf
import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from preprocess import *
# %%
stock_code = '005930.KS'
start_date = '2020-07-30'
end_date = '2023-07-30'
#%%
def find_pattern(stock_code, start_date, end_date, seq_len=7, k=5):
    data = yf.download(stock_code, start = start_date, end = end_date)
    close = data['Close']
    seq_len = 7
    k = 5

    window_data = windowDataset(data = close, input_window = seq_len, output_window = 1, input_size = 1, stride = 1)
    window_data = MinMax(window_data)

    dist = pd.DataFrame(data = torch.sum(torch.sqrt((window_data.x[-1] - window_data.x)**2), dim = (1,2)), columns = ['Values'])
    dist_sort = dist.sort_values(by = 'Values')
    dist_ind = dist_sort.index[1:k+1].tolist()
    
    pattern = torch.cat([window_data.x[i] for i in dist_ind],dim=1)
    pattern = pattern.permute(1,0)
    
    after_pattern = torch.cat([window_data.x[i+seq_len] for i in dist_ind],dim=1)
    after_pattern = after_pattern.permute(1,0)
    
    current_data = window_data.x[-1]
    for i in range(k):
        after_pattern[i] = after_pattern[i] - after_pattern[i][0] + current_data[-1]


    plt.figure(figsize=(10, 6))
    plt.plot(range(seq_len), current_data, label='Current Data')

    for i, pattern_data in enumerate(after_pattern):
        plt.plot(range(seq_len - 1, seq_len - 1 + seq_len), pattern_data, label=f'Pattern {i + 1}', linestyle='--')

    plt.legend()
    plt.yticks([])
    plt.xticks(range(2 * seq_len), range(1, 2 * seq_len + 1))
    plt.show()    
    








# %%
