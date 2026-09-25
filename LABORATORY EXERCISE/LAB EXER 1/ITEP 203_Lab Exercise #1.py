
#Incident Ticket, Bot, Short Description, status
columns = ["Incident ID", "Bot", "Short Description", "Status"]
TicketList = [
["INC1392939", "BOT-Inventory", "Failed to generate the daily report", "Active"],
["INC1392940", "BOT-Email", "Failed to send the scheduled notification", "Active"],
["INC1392941", "BOT-DataSync", "Encountered an error during data transfer", "Active"],
["INC1392942", "BOT-Invoice", "Failed to process an invoice", "Active"],
["INC1392943", "BOT-Report", "Failed to generate the weekly report", "Active"],
["INC1392944", "BOT-FileTransfer", "Failed to upload the required file", "Active"],
["INC1392945", "BOT-DataEntry", "Encountered an error while entering records", "Active"],
["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup", "Active"],
["INC1392947", "BOT-Validation", "Failed to validate the submitted records", "Active"],
["INC1392948", "BOT-Notification", "Failed to send the system alert", "Active"],
]

class IDGenerator:
    def __init__(self, prefix="INC", start=1392949, width=7):
        self.prefix = prefix
        self.current = start
        self.width = width

    def next_id(self):
        id_str = f"{self.prefix}{self.current:0{self.width}d}"
        self.current += 1
        return id_str

id_gen = IDGenerator(prefix="INC", start=1392949, width=7)  
def Add_Ticket(): 
    print("------------------------------")
    bot = input("Enter Bot: ")
    short_desc = input("Enter short description: ")
    new_id = id_gen.next_id() #dito is yung anes ginamit yung object na ginawa then yung function na nasa loob ng class
    TicketList.append([new_id, bot, short_desc, "Active"])
    print("Incident Ticked added succesfully!")
    print("------------------------------")
      
def Display_Active():
    for row in TicketList:
        status = row[3]
        if status == "Active":
            print(f"{row[0]:<15}{row[1]:<20}{row[2]:<45}{row[3]}") #padding lang yung kinmeberlu extra na nakalagay na nakakalito tingnan
    print()

def Search():
    print("------------------------------")
    id = input("Enter Incident ID: ")
    found = False
    for row in TicketList:
        if row[0] == id:
            print(f"{row[0]:<15}{row[1]:<20}{row[2]:<45}{row[3]}")
            found = True
    if not found:
        print("Incident ID does not exist.")
    print("------------------------------")

def Remove():
    print("------------------------------")
    id = input("Enter Incident ID: ")
    for row in TicketList:
        if row [0] == id:
            TicketList.remove(row)
            print(f"Incident ticket {id} has been removed succesfully!")
            print("------------------------------")
            return

def Total():
    count = 0
    for row in TicketList:
        if row[3] == "Active":
            count += 1
    print("------------------------------")
    print("The total number of active incident tickets are:", count)
    print("------------------------------")

def Exit():
    print("------------------------------")
    print("Thank you for using our system!")
    print("------------------------------")
    return True  # signal to the loop that it's time to stop

def Main():
    choice = input("Choose a function (1-6): ")
    if choice == "1":
        Add_Ticket()
    elif choice == "2":
        Display_Active()
    elif choice == "3":
        Search()
    elif choice == "4":
        Remove()
    elif choice == "5":
        Total()
    elif choice == "6":
        Exit()
        return False  # tell the while loop to stop
    else:
        print("Invalid choice.")
    return True  # keep looping

def Menu():
    print("------------------------------")
    print("   Incident Ticket Manager   ")
    print("------------------------------")
    print("1. Add incident ticket\n" \
          "2. Display all active incidents\n" \
          "3. Search incident ticket\n" \
          "4. Remove a resolved incident ticket\n" \
          "5. Display total active incidents\n" \
          "6. Exit")
    print("------------------------------")

# --- Program loop ---
running = True
while running:
    Menu()
    running = Main()


    

