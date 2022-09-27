# PPG_Clustering
tries to cluster ppg signals<br> 
**LDA and Autoencoder.ipynb** <br>	this notebook clusters peak to peak ppg signals using LDA and fully connected autoencoder as features extractor<br>
**general_pca_kmeans_notebook.ipynb** <br> this notebook cluster complete signals of ppg using PCA [2 PCA components] as a features reduction technique [no plots of signals and results was not satisfied]<br>
**heart_rate_equqlization.py**<br> this notebook contains functions able to divide PPG signal to peak to peak parts and then normalize each on beat to equal number of time steps<br>
**peak2peak_aug_2022_oneBeat_kmeans.ipynb**<br> this notebook contain clustering of Peak_to_peak data from Dr mostafa. algorithms used are DTW from tslearn library. for not good clusters there is subclustering and plotting
