read = []
def intro():
    count = 0
    print("Swallow Speed Analysis: Version 1.0")
    while True:
        count += 1
        data = input("Enter next reading: ")
        if data == "":
            break
        else:
            check(read,count)
        
def check(data,count):
    if data[0] == "U" :
        a = float(data[1:])*1.61
        read.append(a)
        print("Reading Saved")
    elif data[0] == "E":
        a = float(data[1:])
        read.append(a)
        print("Reading saved")
    my_fun(read,count)
    
def my_fun(read,count):
    
    max_km = max(read)
    con_km_to_miles = max_km/1.61
        
    min_km = min(read)
    min_km_to_miles = min_km/1.61
    sum = 0
    for i in range(len(read)):
        sum += read[i]
    avg = sum/len(read)
    convert = avg /1.61
    print("Result Summary")
    if count == 2:
        print(count-1," Reading saved")
    else:
        print(count-1," Reading saved")   
        
    print("Max speed is %.1f KPH and %.1f MPH"%(max_km,con_km_to_miles))
    print("Min speed is %.1f KPH and %.1f MPH"%(min_km,min_km_to_miles))
    print("Average speed is %.1f KPH and %.1f MPH"%(avg,convert))
                
intro()