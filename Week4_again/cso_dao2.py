import requests
import json

urlFull =  "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP001/JSON-stat/2.0/en"
urlBegin = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file = fp)

def getAll(dataset):
    url = urlBegin + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getFormattedAsFile(dataset):
    with open("cso_formatted1.json", "wt") as fp:
        print(json.dumps(getFormatted(dataset)), file = fp)

def getFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimentions = data["dimension"]
    sizes = data["size"]
    valueCount = 0
    result = {}
    currentDict = result

    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimentions[currentId]["category"]["index"][dim0]
        label0 = dimentions[currentId]["category"]["label"][index] 
        result[label0] = {}
        #print(label0)

        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimentions[currentId]["category"]["index"][dim1]
            label1 = dimentions[currentId]["category"]["label"][index]
            result[label0][label1] = {}
            #print("\t",label1)

            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimentions[currentId]["category"]["index"][dim2]
                label2 = dimentions[currentId]["category"]["label"][index]
                result[label0][label1][label2] = {}
                
                #print("\t\t",label)
                
                for dim3 in range(0, sizes[3]):
                    currentId = ids[3]
                    index = dimentions[currentId]["category"]["index"][dim3]
                    label3 = dimentions[currentId]["category"]["label"][index]
                    result[label0][label1][label2][label3] = values[valueCount]
                    #print("\t\t\t",label, " ", values[valueCount])
                    
                    valueCount += 1

    
    return result


if __name__ == "__main__":
    getFormattedAsFile("FP001")

