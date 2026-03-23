set1={"A", "B", "C", "D", "E"}
set2={"B", "D", "V", "X", "Y", "Z"}

inter=set1.intersection(set2)

total_guests=list(inter)

print("Total guests to be invited for party are : ", len(total_guests))
print("Guest List : ", total_guests)