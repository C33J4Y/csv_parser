import csv
#from datetime import datetime,timedelta

path = "lunch_csv.csv"
file = open(path, newline ='')
reader = csv.reader(file)

newFile = open('new_menu.csv', 'w', newline='')
writer = csv.writer(newFile)

object_num = 30000



#data = [row for row in reader]
#using enumerate method to be able to access index in for loop
for count, line in enumerate(reader):
    
    object_num += 1
    section_name = line[0]
    dish_name = line[1]
    dish_price = line[2]
    line = [[object_num, section_name, dish_name, dish_price]]
    #if date_str == '':
        #date_str = 'NULL'
        # NUll values for dates are being represented with date 1900-01-01
        #date = datetime.strptime(date_str,'NULL') 
    #else:
        #date = datetime.strptime(date_str[:10],'%Y-%m-%d')
    
    #date = x.strftime(line[10])
    #print(line[0],line[1],line[2],line[10])
    #print(type(date))
    writer.writerows(line)
    
#print(dir(csv))


