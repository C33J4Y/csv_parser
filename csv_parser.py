import csv
#from datetime import datetime,timedelta

path = "menu_items.csv"
file = open(path, newline ='')
reader = csv.reader(file)

#data = [row for row in reader]
#using enumerate method to be able to access index in for loop
for count, line in enumerate(reader):
    #mi_seq = int(line[0])
    #obj_num = int(line[1])
    #mi_name = str(line[2])
    mi_seq = line[0]
    obj_num = line[1]
    mi_name = line[2]
    #last_name = str(line[1])
    #first_name = str(line[2])
    #date_str = str(line[10])
    #if date_str == '':
        #date_str = 'NULL'
        # NUll values for dates are being represented with date 1900-01-01
        #date = datetime.strptime(date_str,'NULL') 
    #else:
        #date = datetime.strptime(date_str[:10],'%Y-%m-%d')
    
    #date = x.strftime(line[10])
    #print(line[0],line[1],line[2],line[10])
    #print(type(date))
    #print(count,obj_num, last_name, first_name, date)
    print(mi_seq,obj_num,mi_name)
    
#print(dir(csv))


