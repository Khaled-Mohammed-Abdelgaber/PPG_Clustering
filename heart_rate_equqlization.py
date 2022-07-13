
from scipy.signal import find_peaks
def rescale(arr, factor=2):
    n = len(arr)
    return np.interp(np.linspace(0, n, int(factor*n+1)), np.arange(n), arr)

def heart_rate_equqlization(data_frame,n_signals = 10001,p_threshold = 0.7, rate = 9):
  eq_rate_data = pd.DataFrame()
  for i in range(n_signals):
    print(i)
    peaks, _ = find_peaks(data_frame.loc[i], height=p_threshold)
    if len(peaks) < rate:
      continue
    arr = data_frame.loc[i].values[:peaks[rate - 1]]
    scaled = rescale(arr, factor= 1024/peaks[rate - 1])
    df = pd.DataFrame(data = scaled )
    eq_rate_data = pd.concat([eq_rate_data , df],axis = 1)
  return eq_rate_data
