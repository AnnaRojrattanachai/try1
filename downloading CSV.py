import pandas as pd
import numpy as np

# with open ("M24028_20240426_File1_Shank0_goodSpikeTimes.csv", "r") as f:
#    for line in f:
#        print (line)

file1 = "/Users/pitsinee/PycharmProjects/HelloWorld/research project/M24028_20240426_File1_Shank0_goodSpikeTimes.csv"

def openfile (file_path):
    global df
    df = pd.read_csv(file_path, names = ["unit_id", "spikeTime"])
    print (df)
openfile(file1)

def group(file):
    global grouped_df
    grouped_df = file.groupby('unit_id')['spikeTime'].apply(list).reset_index()
    grouped_df.to_csv('rearranged_output.csv', index=True)
    global maxtime
    maxtime = max(df[df.columns[1]].tolist())
    print(grouped_df)
    print ("max time:", maxtime)

group(df)

def groupBin(binwidth):
    bins = np.arange(0, maxtime, binwidth) #returns array of bin edges
    allcount = [0] *(grouped_df.shape[0]) #list of lists of counts in each bin
    for i in range(grouped_df.shape[0]):
        x = grouped_df.iloc[i]['spikeTime'] #get the list of values of spike time for row i
        # print ("x:", x) #check for spike times
        counts, bin_edges = np.histogram(x, bins = bins)
        allcount[i] = counts
        # print ("all count:", len(allcount), "column[0]:", grouped_df.shape[0]) #check numbers of items if the same
        #print("Counts per bin for row", i, ":", counts)
    data = {
        "unit_id": grouped_df[grouped_df.columns[0]].tolist(),
        "spike number in each bin": allcount
    }
    binned_df = pd.DataFrame(data)
    binned_df.to_csv ("binnedData.csv", index = False)
    print (binned_df)
groupBin(100)

    # for i in df[grouped_df.columns[0]].tolist():
    #     counts, bin_edges = np.histogram(df[df.columns[1]].tolist(), bins=bins)
    #     print("Counts per bin:", counts)  # Output: [2, 2, 3]
    #     print("Bin edges:", bin_edges)

    # for i in range (len(bins)-1):
    #     for x in df[df.columns[1]].tolist():
    #         if bins[i] <= x < bins[i+1]:
    #
    # print (bins)











