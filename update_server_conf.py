Task: You are to update the "Max Connections" key in the server.conf file. Write a python script that will 
- open the file
- copy the file content into a variable
- Write into the file using the variable
- Input a new value for "Max Connections"

---
def update_server_config(file_path, key, value):
    #"open" is an in-built funtion to read files and it starts with the statement "with". "r" denotes read mode
    with open(file_path, "r") as file: 
        #After saving the file as a variable, convert the content of the file once read into a list # "readlines" is an in-built function for this task.
        lines = file.readlines()  

    with open (file_path, "w") as file: #open file to edit content ("write") in it
        for line in lines:
            #(the "key" variable here will represent the key for the key/value pair in the server.conf file you want to change)
            if key in line: 
                # "\n" represents the new value you want to enter in the key/value pair.
                file.write(key + "=" + value + "\n") 
            else:
                file.write(line) 
 
update_server_config ("server.conf", "MAX_CONNECTIONS", "1000") # Input the new data for key/value pair in the file you want to change
