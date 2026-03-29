import random
choice = ['r','p','s']
while True:
    cust_choice = input("Enter your choice (r/p/s):").lower()
    if  cust_choice not in choice:
        print("Invalid choice")
        continue
    comp_choice = random.choice(choice)
    print("your choice : ",cust_choice)
    print(" computer choice :",comp_choice)
    if cust_choice == comp_choice:
        print("Tie!")
    elif ( (cust_choice =='r' and comp_choice == 's') or
          (cust_choice =='s' and comp_choice == 'p') or
          (cust_choice =='p' and comp_choice == 'r') ):
        print("YOU WIN")
    else:
        print("YOU LOSE!")
        should_continue = input("Enter your choice(y/n)").lower()
        if should_continue == 'n':
            break

        
