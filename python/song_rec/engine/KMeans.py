

def normalize():
    '''reads the file SongCSV.csv and returns a dataframe with the 
    csv data and appended columns with normalized quantitative columns'''
    import pandas as pd
    import numpy as np
    
    dataframe = pd.read_csv('SongCSV.csv')
    width = len(dataframe.loc[0, :])
    height = len(dataframe.loc[:,:])
    array = ["Duration", "KeySignature", "KeySignatureConfidence", "Tempo", "TimeSignature", "TimeSignatureConfidence"]
    for i in array:
        temp = i +('_normal')
        std_1 = dataframe.loc[:,i].std()
        mean = dataframe.loc[:,i].mean()
        dataframe[temp] = (dataframe[i]-mean)/std_1

    return dataframe;

def inertia_plot():
    from normalize import normalize
    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_samples, silhouette_score
    import matplotlib.pyplot as plt
    #data_set_1 = pd.read_csv("SongCSV.csv")

    new_data = normalize()
    data = new_data.iloc[:,18:19]
    temp_1 = 10**8;
    x = np.linspace(1,20, num = 20)
    array = []

    for i in range(1,21):
        kmeans = KMeans(n_clusters = i, max_iter=200, random_state=0,verbose=0).fit(data)
        array.append(kmeans.inertia_)

    plt.plot(x, array, '-x')
    return plt.show


def normal_att(y):
    d = normalize()
    for i in range(9001, 10000, 1) :
        if d.Title[i] == y :
            break;
    X = [[d.Tempo_normal[i], d.Duration_normal[i], d.KeySignature_normal[i], d.KeySignatureConfidence_normal[i], d.TimeSignature_normal[i], d.TimeSignatureConfidence_normal[i]]]
    return(X)
    



def kmeans(y):
    '''takes input as the index of the song i.e SongNumber, and uses
    the index to access the different quantitative columns.'''
    
    import numpy as np
    import pandas as pd
    from sklearn.cluster import KMeans
    d = normalize()
    df = d[['Tempo_normal', 'Duration_normal', 'KeySignature_normal', 'KeySignatureConfidence_normal', 'TimeSignature_normal', 'TimeSignatureConfidence_normal']]
    df = df[0:9000]

    kmeans = KMeans(n_clusters = 5, max_iter = 300).fit(df)
    #print(kmeans.cluster_centers_)
    labels = kmeans.labels_
    X = normal_att(y)
    ans = int(kmeans.predict(X))
    print(ans)
    
    l = []
    
    for i in range(0,9000):
        if(labels[i] == ans):
            l.append(normal_att(i))
    #print(l)
    
    
kmeans("b'Down In Dixie'")
    




