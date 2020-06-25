import pickle
import numpy as np 

def get_tables(filename):
    #wgds,samples = []
    with open(filename, 'rb') as f:
        wgds,samples = pickle.load(f)

    wgd_sum=np.sum(wgds)
    samples_sum=np.sum(samples)
    #print("wgd sum:",wgd_sum," | samples_sum:",samples_sum)
    print("Normalized:",wgd_sum/samples_sum)
    #print("Old_normalized:",np.mean(wgds)/samples_sum)
    #print(filename,",",wgd_sum,",",samples_sum,",",wgd_sum/samples_sum,",",np.mean(wgds)/samples_sum)

files = []
files.append("15_1_backdoor_0-01.pickle")
files.append("15_1_no_backdoor_0-01.pickle")

files.append("15_1_backdoor_0-005.pickle")
files.append("15_1_no_backdoor_0-005.pickle")

files.append("15_1_backdoor_0-001.pickle")
files.append("15_1_no_backdoor_0-001.pickle")

for f in range(0,len(files)):
    get_tables(files[f])