class parent():
    def __init__(self):
       print("This is parent class")
       
       def menu(dish):
         if dish == "burger":
             print("You can add following toppins")
             print("More cheese | Add jalapeno")
         elif dish == "iced_americano":
             print("You can add following toppins")
             print("Add chocolate flavour | Add caramel flavour")
         else:
             print("please enter valid dish or else...")
             
             def final_amount(dish,add_ons):
                 if dish=="burger" and add_ons =="chesse":
                     print("price is gonna be 200.00")
                 elif dish == "burger" and add_ons == "jalapenos":
                     print("we demand 300.00 ruppes from you for that burger or else...")
                 elif dish == "iced_americano" and add_ons == "chocolate":
                     print("we demand 250.00 ruppes from you for that iced americano or else...")
                 elif dish == "iced_americone" and add_ons == "caramel":
                         print("we demand 450.00 ruppes from you for that burger or else")
                         
                         class child1(parent):
                             def __init__(self,dish):
                                 self.new_dish = dish
                             def get_menu(self):
                                 parent.menu(self.new_dish)
                                 
                                 class child2(parent):
                                     def __init__(self,dish,addons):
                                         self.new_dish = dish 
                                         self.addons = addons
                                         def get_final_amount(self):
                                             parent.final_amount(self.new_dish,self.addons)
                                             
                                             child1_object = child1("burger")
                                             child1_object.get_menu()
                                             
                                             child2_object = child2("burger","cheese")
                                             child2_object.get_final_amount()