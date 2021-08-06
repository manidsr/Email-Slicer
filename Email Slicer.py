while(True):
    try:
        email = input("Enter 0 to exit\nEnter your email : ").strip()

        if(email == "0"):
            break

        username = email[:email.index("@")]
        domain = email[email.index("@")+1:]

        print(f"Your email username is {username} and domain is {domain}")

    except:
        print("Wrong Input")
    finally:
        print("---------------------")