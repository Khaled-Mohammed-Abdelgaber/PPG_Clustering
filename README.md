# PPG_Clustering
## table of most important contents<br> 
**LDA and Autoencoder.ipynb** <br>	this notebook clusters peak to peak ppg signals using LDA and fully connected autoencoder as features extractor. datasets from Dr mostafa peak2peak_aug_2022<br>
**general_pca_kmeans_notebook.ipynb** <br> this notebook cluster complete signals of ppg using PCA [2 PCA components] as a features reduction technique [no plots of signals and results was not satisfied]<br>
**heart_rate_equqlization.py**<br> this notebook contains functions able to divide PPG signal to peak to peak parts and then normalize each on beat to equal number of time steps<br>
**peak2peak_aug_2022_oneBeat_kmeans.ipynb**<br> this notebook contain clustering of Peak_to_peak data from Dr mostafa. algorithms used are DTW from tslearn library. for not good clusters there is subclustering and plotting<br>
**peak2peak_aug_2022_oneBeat_kmeans_1.ipynb**<br> this notebook uses PCA but contains error of shuffling<br>
**peak2peak_aug_2022_oneBeat_softDTW.ipynb**<br> this notebook uses softDTW to cluster first 50000 of peak2peak datasets but no plots and no blood pressure available because of the memory leakage<br>
**revese_approach.ipynb** this notebook proof that ppg signal shape not depend on blood pressure only but there are another factors such as heart rate
