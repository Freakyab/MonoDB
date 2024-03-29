import pymongo

from decouple import config

class client_name:
   
    client = pymongo.MongoClient(f"mongodb+srv://{config('client')}@cluster0.cqjgwxp.mongodb.net/?retryWrites=true&w=majority")
    Db = client['PassDb']
    collection = Db['Pass']

# encryption
def encryption(str):
    pass

# to fetch particular data

def fetch_data(website_name):
    Tofind = {'website_name':website_name}
    results = client_name.collection.find(Tofind)

    for result in results:
        final_keys=list(result.keys())
        final_values=list(result.values())
        if(website_name in final_values):
            position_of_website_name = final_values.index(website_name)
            passwords =  final_values[position_of_website_name+1]
            username = input("Enter the username: ")

            if username in passwords:

                position_of_username = passwords.index(username)
                return passwords[position_of_username+1],position_of_username,username,passwords
            else:
                return False
    else:
        return False

# to insert data

def insert_data():
    password_lists=[]
    website_name=input("Enter the name of website: ")
    results = client_name.collection.find()
    for result in results:
        final_values=list(result.values())
    if website_name in final_values:
        print("Website already exists")
    else:
        Number_of_account =input("Enter the no. of account you have: ")
        for i in range(int(Number_of_account)):
            password_lists.append(input("Enter the name of username: "))
            password_lists.append(input("Enter the name of password: "))
        
        main_pass = [{'website_name':website_name,'account_data':password_lists}]
        
        client_name.collection.insert_many(main_pass)

# to print db

def print_db():
    result = client_name.collection.find()
    for i in result:
        print(i)

# to change the password
def change_password(password,passwords,username):
    
    new_password = input("Enter the new password: ")
    check = input("Do you want to save the password? (y/n): ")
    if check == 'y':
        position_of_password = passwords.index(username)
        passwords[position_of_password+1] = new_password
        new_main_dict={'account_data':passwords}
        client_name.collection.update_one({'website_name':website_name},{'$set':new_main_dict})
    else:
        print("Password not saved")

# to delete the data

def delete_data(website_name,password,passwords,username):
   
    passwords.remove(username)
    passwords.remove(password)
    new_main_dict={'account_data':passwords}
    permission = input("Are you sure you want to delete the data? (y/n): ")
    if permission == 'y':
        client_name.collection.update_one({'website_name':website_name},{'$set':new_main_dict})
        print("Data deleted")
    else:
        print("Data not deleted")
    
# print password

def print_password(password,position_of_username,username):
    print(f"Your username : {username}")    
    print(f"Your password : {password}")    

#insert data inside specific website

def insert_data_inside_website(website_name):
    results = client_name.collection.find()
    for result in results:
        final_values=list(result.values())
        if(website_name in final_values):
            position_of_website_name = final_values.index(website_name)
            passwords =  final_values[position_of_website_name+1]    
        Number_of_account =input("Enter the no. of account you have: ")
        for i in range(int(Number_of_account)):
            NewUsername = input("Enter the name of username: ")
            NewPassword = input("Enter the name of password: ")
            if NewUsername in passwords:
                print("Username already exists")
            else:
                passwords.append(NewUsername)
                passwords.append(NewPassword)
                main_pass = {'account_data':passwords}
                client_name.collection.update_one({'website_name':website_name},{'$set':main_pass})

# main code

main_key = input("Enter the key: ")
if main_key == '0112':
    action = int(input("1.Insert_data\n2.Fetch_data\n3.quit\nEnter: "))
    if action == 1:
        insert_data()
    elif action == 2:  
        website_name = input("Enter the name of website: ")
        result,position_of_username,username ,passwords= fetch_data(website_name)
        if result == False:
            print("Invalid")
        else:
               
            action1 = int(input("Enter the action you want to perform:\n1.change_password\n2.delete_data\n3.print_password\n4.print_db\n5.Insert_data\nEnter: "))
            if action1 == 1:
                change_password(result,passwords,username)
            elif action1 == 2:
                delete_data(website_name,result, passwords, username)
                print_db()
            elif action1 == 3:
                print_password(result, position_of_username, username)
            elif action1 == 4:
                print_db()
            elif action1 == 5:
                insert_data_inside_website(website_name)
            else:
                 print("Invalid")
else:
    print("Invalid Password")
