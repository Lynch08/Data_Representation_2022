from inter_api import getAll

data = getAll()

total_area = 0

for entry in data: 
    valuationReps = entry["ValuationReport"]
    #print(valuationReps)
    for valuationrep in valuationReps:
        #print (valuationrep)
        if valuationrep['FloorUse'] == "HAIR SALON":
            total_area += valuationrep["Area"]

print (total_area)