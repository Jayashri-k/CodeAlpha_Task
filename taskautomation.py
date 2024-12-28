import os
import time

print("TASK AUTOMATION USING PYTHON SCRIPTS\n")
print("\tRENAMING THE FOLDER FILES\n")
print("1. The files in the folder starting with QP will change as Question Paper")
print("2. The files in the folder which have spaces will change to underscore")
print("3. It checks for every 5 minutes")

#ask the user to input the folder path

folder_path=input("Enter the folder path to automate: ")

#list all files in the folder
while True:
    files=os.listdir(folder_path)

    for a in files:
        try:    
            #replace spaces with underscores
            new_name=a.replace(" ","_")

            #replace QP with 'Question Paper
            new_name=a.replace("QP","Question Paper")
        
            old_path=os.path.join(folder_path,a)
            new_path=os.path.join(folder_path,new_name)
        
        #rename the file
            os.rename(old_path,new_path)
            print("Renamed: ",a,"AS: ",new_name)
        except Exception as e:
            print("Error renaming",a,":",e)
    time.sleep(20)
    
