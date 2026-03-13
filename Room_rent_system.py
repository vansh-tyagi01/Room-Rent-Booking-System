print("*..........ROOM RENT BOOKING SYSTEM..........*")
print(" ")
print("....WELCOME TO TYAGI_KANHAIYA HOTEL....*")
print(" ")
total_room=27
total_room_list=list(range(1,total_room+1))
print("Total Room :",total_room_list)
booked_rooms=[]
list_name_email_room=[]

rooms = {
    1:700,
    2:620,
    3:690,
    4:700,
    5:800,
    6:800,
    7:850,
    8:870,
    9:800,
    10:880,
    11:870,
    12:900,
    13:785,
    14:500,
    15:1000,
    16:1100,
    17:1000,
    18:950,
    19:1000,
    20:1150,
    21:1250,
    22:800,
    23:845,
    24:800,
    25:960,
    26:1500,
    27:1300
}



# Show Room Rent

def show_room_rent():
    for key,value in rooms.items():
        print(f"Room {key} : {value} rupee💵")


# Booked Room

def book_room():
    name=input("Enter your Name:").lower()
    email=input("Enter your Email:").lower()
    select_room=int(input("Enter your room to Book:"))

    if select_room not in total_room_list:
        print(f"Room {select_room} is Invalid Choice! It is out of range Total Room.")
        return
        
    if select_room in booked_rooms:
        print(f"Room {select_room} is Already Book✅")
        
    else:
        booked_rooms.append(select_room)
        list_name_email_room.append([name,email,select_room])
        print(f"{name} your Room {select_room} is Booked Successfully👍 , Room Rent : {rooms[select_room]} rupees🪙")



# Cancel Room

def cancel_room():
    name=input("Enter your Name:").lower()
    email=input("Enter your Email:").lower()
    select_room=int(input("Enter your room to Cancel:"))

    if select_room in booked_rooms and [name,email,select_room] in list_name_email_room:
        booked_rooms.remove(select_room)
        list_name_email_room.remove([name,email,select_room])
        print(f"{name} your Room {select_room} is Cancelled Successfully👍")
    else:
        print(f"{[name,email,select_room]} not Available✖️")



# Avalable Room

def available_room():
    available_Room=[]
    for total_room in total_room_list:
        if total_room not in booked_rooms:
            available_Room.append(total_room)
    print("Available Rooms :",available_Room)



# Show Booked Room

def show_booked_room():
    if len(booked_rooms)==0:
        print("Empty Booked Room List....!")
    else:
        print("Booked Room :",booked_rooms)



# show list of user --> name,email,room number

def show_user_data():
    if len(list_name_email_room)==0:
        print("Empty list of User name,email,room number.....")
    else:
        print("List of User :",list_name_email_room)



while True:
    print("1. Show Room Rent\n2. Booked Room\n3. Cancel Room\n4. Available Room\n5. Show Booked Room\n6. Show User Detail\n")
    print(" ")
    choice=int(input("Enter your choice?(0 to exit):"))

    if choice == 0:
        print("Program Exit...")
        break
    elif choice == 1:
        show_room_rent()
    elif choice == 2:
        book_room()
    elif choice == 3:
        cancel_room()
    elif choice == 4:
        available_room()
    elif choice == 5:
        show_booked_room()
    elif choice == 6:
        show_user_data()
    else:
        print("Invalid choice!")





#*................                                                         THANK YOU                                                       .......................*#
    
        
        

