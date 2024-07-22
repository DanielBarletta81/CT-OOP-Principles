#main

#: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc.,
#  ensuring that budget details remain private and are accessed or modified through public methods.

#Task 1: Define Budget Category Class Create a class `BudgetCategory` 
# with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.

# Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

class BudgetCategory:
  
    def __init__(self, budget_amt, category ):
        self.__budget_amt = budget_amt
        self.__category = category
    
    def get_category(self):
        return self.__category

    def set_category(self, new_category):
        self.__category = new_category

    def get_budget_amt(self):
        return self.__budget_amt

    def set_budget_amt(self, new_budget_amt):
        self.__budget_amt = new_budget_amt

def add_category(category):
       
    new_category = input("What category would you like to add? ")
    new_budget_amt = float(input(f"How much will you allocate to {new_category}?"))
    category[new_category] = BudgetCategory(new_category, new_budget_amt)
    print(new_category, new_budget_amt)


def add_transaction(category):
        select_budget = input('Which Budget would you like to modify? ')
        if select_budget in category:
            type_transaction = input("Are you adding or subtracting from this budget(add/subtract)?")
        
            if type_transaction == 'add':
                new_budget_amt = float(input("Please enter the amount. "))

                category[new_budget_amt] = new_budget_amt

            elif type_transaction == 'subtract':
                print("Subtract")
            else:
                print("Please enter a valid choice (add/subtract)")
        

def main():
    category = {}

    while True:

        print("\nMenu: \n1. View Budgets \n2. Add Expense Category \n3. Update Budget \n4. Exit")
        choice = input("Please make a choice: ") 

        try:
          
          if choice == '1':
              pass
          elif choice == '2':
              #create new category
              add_category(category)
          elif choice == '3':
              #update budget
              add_transaction(category)
          elif choice == '4':
              # exit
              break
          else:
              print("Invalid selection.") 

        except:
          print('An exception occurred')    

main()