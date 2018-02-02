"""
in everyday work i save my projects in
c:\Folder\

But its so many files there
Therefore every month i remove files into subfolders
c:\Folder\Year\Year,Months\

This py script moves this auto

You can use it as to shedule
python arch_my_files.py c:\folder\

"""
def create_year_dir(folder, year, month, day):
    import os

    try:
        if day == 1 and month == 1: #if PC doesnt work anytime it can bo removed
            os.mkdir(folder + str(year))
            print('New folder ' + folder + str(year) + ' created')
    except:
        print("cannot create folder - " + folder + str(year))


def create_month_dir(folder, year, months, day):
    import os
    try:
        if day == 1: #if PC doesnt work anytime it can bo removed
            os.mkdir(folder + str(year)+'\\'+str(year)+','+str(months))
            print('New folder ' + folder + str(year) + '\\' + str(year) + ',' + str(months) + ' created')
    except:
        print("cannot create folder - " + folder + str(year) + '\\' + str(year) + ',' + str(months))

def main_proc(folder):
    import os
    import time
    from datetime import datetime, date, time
    import shutil

    day = date.today().day
    month = date.today().month
    months = date.today().strftime("%B")
    year = date.today().year
    if folder is None:
        raise RuntimeError("No such folder")

    create_year_dir(folder, year, month, day)
    create_month_dir(folder, year, months, day)

    files = os.listdir(folder)
    files = [os.path.join(folder,file) for file in files]
    files = [file for file in files if os.path.isfile(file)]

    for file in files:
        year_file = datetime.fromtimestamp(os.path.getctime(file)).year
        month_file = datetime.fromtimestamp(os.path.getctime(file)).month
        month_file_sd =  datetime.strptime('01.'+str(month_file)+'.'+str(year_file),'%d.%m.%Y')
        month_file_s = month_file_sd.strftime("%B")

        if month==1 or month==2:
            month_main = 12 + month
        else:
            month_main = month

        if (month_file+2) == month_main:
            print("Removed "+folder + str(year_file) + '\\'+str(year_file)+',' + str(month_file_s) + '\\' + file.split('\\')[-1])
            shutil.move(file, folder+str(year_file)+'\\'+str(year_file)+','+str(month_file_s)+'\\'+file.split('\\')[-1])


#********************next code runs from command line***********************************

if __name__ == '__main__':
    import sys

    try:
        folder = sys.argv[1]
    except:
        folder = "c:\\mdbs2\\"

    main_proc(folder)



