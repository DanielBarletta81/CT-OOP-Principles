#main

#: You are required to build a Personal Budget Management application. 
# The application will manage budget categories like food, entertainment, utilities, etc.,
#  ensuring that budget details remain private and are accessed or modified through public methods.

#Task 1: Define Budget Category Class Create a class `BudgetCategory` 
# with private attributes for category name and allocated budget. 
# - Initialize these attributes in the constructor.

# Expected Outcome: A `BudgetCategory` class capable of storing category details securely.

# Task 2: Implement Getters and Setters -
#  Write getter and setter methods for both the category name and the allocated budget.
#  - Ensure that the setter methods include validation (e.g., budget should be a positive number).

# Expected Outcome: Methods that allow controlled access and 
# modification of the private attributes, with validation checks in place.

#class BudgetCategory:
    # Constructor and private attributes
    # ...

    # Getters and setters for category name and budget
    # ...

 #   def add_expense(self, amount):
        # Method to add an expense to the category
        # ...

 #   def display_category_summary(self):
        # Method to display the budget category details
        # ...

#food_category = BudgetCategory("Food", 500)
#food_category.add_expense(100)
#food_category.display_category_summary()

class BudgetCategory:
  
    def __init__(self, category, budget_amt):
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

#Task 3: Add Budget Functionality Implement a method to add expenses to a category and adjust
#  the budget accordingly.
#  Validate the expense amount before making deductions from the budget.

#Expected Outcome: Ability to track expenses per category and update the remaining budget safely.



    def show_category_summary(self):
       
       print(f'Budget Category: {self.get_category()}\n Balance: {self.get_budget_amt()}')
       
    
    def incur_expense(self,amount):
       if amount > 0:
           self.set_budget_amt(self.get_budget_amt() - amount)
           print(f'Budget {self.__category} decreased by {amount}.')
       else:
           print("Error.")
       
       


    def add_to_budget(self,amount):
       if amount > 0:
           self.set_budget_amt(self.get_budget_amt() + amount)
           print(f'Budget {self.__category} increased by {amount}.')
       else:
           print("Error.")
            
   

budget = BudgetCategory("Entertainment", 1000)
print(f'Category: {budget.get_category()}')
print(f'Budgeted Amount: {budget.get_budget_amt()}')



food_budget = BudgetCategory("Food", 1200)
print(f'Category: {food_budget.get_category()}')
print(f'Budgeted Amount: {food_budget.get_budget_amt()}')

travel_budget = BudgetCategory("Travel", 3500)

travel_budget.incur_expense(2500)

travel_budget.show_category_summary()


food_budget.show_category_summary()
























""" def main():
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

main() """