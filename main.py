from replit import db
match = 0 # Global variable to determine if match exists in DB

# Review existing credentials
def reviewCredential():
  # List all usernames available -- OPTIONAL
  for key in db.keys():
    print(key)

  # Check if user exists and output username & password
  user = input("\nEnter username you would like to view: ")
  checkCredentials(user)
  if (match == 1):
    print("\nYour credentials are:\n", 
          "Username: ", user, 
          "Password: ", db.get(user))
  else:
    print("There is no username in this database with this name.")

# Add a credential to DB
def addCredential():
  global match # Referencing global match
  user = input("Please enter the username you would like to add: ")
  checkCredentials(user)

  # If match, no add. If no match, ask for password & add
  if match == 1:
    print("This user already exists")
  else:
    password = input("Enter your password for this account: ")
    db[user] = password

    print("Successfully added an account!")
    
# Delete existing credentials under username.
def deleteCredential():
  # List all usernames -- OPTIONAL
  for key in db.keys():
    print(key)

  # Check if user exists and output username & password
  user = input("\nEnter username you would like to delete: ")
  checkCredentials(user)
  if (match == 1):
    del db[user]
    print("You successfully deleted the credentials for", user)
  else:
    print("There is no username in this database with this name.")
  

# Checks if username already exists
def checkCredentials(user):
  global match 
  
  if user in db.keys():
    match = 1
  else:
    match = 0
  
# Menu Loop
# User has to enter a number from the menu (1-4)
inMenu = True
while inMenu:
    print("\n~~~Menu~~~")
    print("1. Review Credential")
    print("2. Add Credential")
    print("3. Delete Credential")
    print("0. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        print("\nYou chose to review a credential!\n")
        reviewCredential()
    elif choice == 2:
        print("\nYou chose to add a credential!\n")
        addCredential()
    elif choice == 3:
        print("\nYou chose to delete a credential!\n")
        deleteCredential()
    elif choice == 0:
        print("\nHave a good day!")
        inMenu = False
        break
    else:
        print("Please enter a number on the list.")
