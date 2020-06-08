file_name = "./Datasets/IRIS.csv"




def getPosition(value, base_min, base_max,h_min,h_max):
    position = (int) (((h_max - h_min) * (value - base_min) / (base_max - base_min)) + h_min)
    return position

def showResults(labels,results):
    print("*********Analyse of final results*********")
    print("First is ground truth, second is final results:")
    print("label=",labels)
    print("result=",results)
    print("grps = bestMap(label,result);")
    print("missrateTot1 = sum(label(:) ~= grps(:)) / length(label);")
def readDataset(file_name):
    import csv
    points = []
    labels = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            lst = []
            for col_isx, data in enumerate(row):
                if col_isx == 0:
                    labels.append(int(data))
                else:
                    lst.append(float(data))
            points.append(lst)
    #print("number of samples:",len(points)," number of dimensions:",len(points[0]), "real k:",max(labels)+1)
    return points,labels