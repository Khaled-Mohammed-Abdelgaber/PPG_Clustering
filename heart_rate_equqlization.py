
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
==============================================================================
""" lastest version """
from scipy.signal import find_peaks
def rescale(arr, no_samples):
    n = len(arr)
    factor = no_samples/n
    return np.interp(np.linspace(0, n, int(factor*n+1)), np.arange(n), arr)

def heart_rate_equqlization(data_frame,no_samples,n_signals = 10001,threshold = 0.7):
  lengthes = []
  eq_rate_data = pd.DataFrame()
  for i in range(n_signals):
    p_threshold = threshold
    print("signal number ",i)
    while True:
      peaks, _ = find_peaks(data_frame.iloc[i,:], height=p_threshold)
      
      np_sig = data_frame.iloc[i,:].values
      #print("original signal : ")
      #print(np_sig)
      #print("=============================")

      mid_peak = peaks[int(len(peaks)/2)]
      start = mid_peak
      stop =peaks[int(len(peaks)/2)+1]
      length = stop - start
      if (length > 130):
        p_threshold = p_threshold - 0.1
      elif ( length < 50):
        p_threshold = p_threshold + 0.1
      else:
        break
    lengthes.append(length)
    print("length = ",stop - start)
    np_sig = np_sig[start:stop]
    #print("cuted signal [np_signale] \n ",np_sig)
    #print("=============================")
    
    
    scaled = rescale(np_sig,no_samples)
    df = pd.DataFrame(data = np.transpose(scaled) )
    #print("final shape is ",df.values.shape)
    #print(df.values)
    #print("**************************************")
    eq_rate_data = pd.concat([eq_rate_data , df],axis = 1,ignore_index=True)
  return eq_rate_data.transpose() , lengthes
