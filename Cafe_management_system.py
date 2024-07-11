from Cafe import Cafe

class CafeManagementSystem:
    def __init__(self):
        self.Cafe = Cafe()    
        self.main_menu()
        
    def main_menu(self):
        while True:
            print("\n Here's the Main Menu. Select one of the options below: ")
            print(" 1   User Input ")
            print(" 2   Order Food ")
            print(" 3   Manage Inventory")
            print(" 4   Billing Receipt")
            print(" 5   Exit")
        
            option = input("Enter your choice 1-5: ") 
            if option.isdigit():
                option=int(option)
            else:
                print("Invalid Option! Enter a valid number. ")
                continue
            
            if option == 1:
                self.userinput()
            elif option == 2:
                self.orderfood()   
            elif option ==3:
                self.manage_inventory()  
            elif option == 4:
                self.billing()
            elif option == 5:
                print("Exiting the Cafe System. Goodbye! ")
                quit()  
            else:
                print("Invalid Option! Please enter a valid number. ")
    
    def userinput(self):
        print("\nUser Input section is called. Now waiting for user to place order: ")
                    
    def orderfood(self):
        while True:
            print("\nOrderFood Section is selected. Now waiting for user to place an order: ")
            print("\n Beverages: ")
            print("1.  Coffee    - 1500")
            print("2.  Tea       - 800")
            print("3.  Latte     - 1500")
            print("4.  Smoothie  - 1000")
            print("\n Snacks: ")
            print("5.  Salad     - 500")
            print("6.  Muffin    - 800")
            print("7.  Crossant  - 1500")
            print("8.  Sandwitch - 1500")
            print("9.  Finish order and Return to Main Menu")
            
            choice = input("\nEnter the number of the Item you want to order (1-9): ")
            if choice.isdigit():
                choice = int(choice)
                if choice in self.Cafe.menu:
                    item,price = self.Cafe.menu[choice]   
                    self.Cafe.order.append((item,price))
                    print(f" Added {item} to your order.")  
                elif choice == 9:
                    print("Finishing order and Returning to Main Menu. ")
                    return         
                else:
                    print("Invalid Choice! Enter digit from 1 to 9. ")           
            else:
                print("Invalid Choice! Enter digit from 1 to 9. ")           
                self.main_menu()
            
            more = input("Do you want to Order more items? yes/no: ")                       
            if more.lower() == "yes":
                self.orderfood()
                
            self.main_menu()

    def manage_inventory(self):
        while True:
            print("\n1. View Inventory ")
            print("2. Display Order Items")
            print("3. Remove Inventory Item ")
            print("4. Update Inventory ")
            print("5. Return to Main Menu ")
            
            choice = input("Enter your choice:  ")
            if choice.isdigit():
                choice = int(choice)     
                if choice == 1:
                    self.viewing_inventory()    
                elif choice == 2:
                    self.display_items()    
                elif choice == 3:
                    self.remove_items()
                elif choice == 4:
                    self.update_items()
                elif choice == 5:
                    self.main_menu()
                else:
                    print("Invalid Choice! Please choose right option")  
                    self.manage_inventory()
            else:
                print("Invalid Choice! Please choose right option")              
                
    def viewing_inventory(self): 
        print("\nCurrent Inventory: ")
        for key, (item,price) in self.Cafe.menu.items():
            print(f"{key}.{item} - {price}")
    
    def display_items(self):
        print("\nDisplay Order Items is selected. ")
        if not self.Cafe.order:
            print("No item in Order. ")
        else:
            for item,price in self.Cafe.order:
                print(f"{item} - {price}")
            
    def remove_items(self):
        print("\nCurrent Inventory: ")
        for key,(item,price) in self.Cafe.menu.items():
            print(f"{key}. {item} - {price}")
            
        choice = input("Enter the number of the Item you want to delete: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print("Item deletion cancelled. ")
                return
            if choice in self.Cafe.menu:
                removed_item = self.Cafe.menu.pop(choice)   
                print(f" Removed {removed_item[0]} from Inventory. ")   
            else:
                print("Invalid number! Please enter a valid number. ")
        else:
            print("Invalid number! Please enter a valid number. ")
        
        more = input("Any other item you want to remove? yes/no: ")
        if more.lower() == "yes":
            self.remove_items()
        
        self.manage_inventory()       
              
    def update_items(self):
        print("Update Item Section is Selected. ")
        self.viewing_inventory()
        
        choice = input("Enter the number '0' to add new item: ")  
        if not choice.isdigit():
            print("Invalid Choice! Please enter a Valid number")
            return
        choice=int(choice)
        
        if choice==0:
            new_item = input("Enter the Name of new item: ")
            new_price = input("Ente the price of new item: ")

            if not new_price.isdigit():
                print("Invalid price! Please enter a valid number. ")
                return
            
            new_key = max(self.Cafe.menu.keys(), default=0) +1
            self.Cafe.menu[new_key] = (new_item,int(new_price))
            print(f"Added new item {new_item} with new price {new_price}.") 
            self.viewing_inventory()
   
    def billing(self):
        print("\n Billing Section is called. Now Processing your Billing Reciept: ")
        total = 0
        for item,price in self.Cafe.order:
                print(f"{item}: {price}")
                total += price
        print(f"Total: {total}")
        self.Cafe.order.clear()
        self.main_menu()