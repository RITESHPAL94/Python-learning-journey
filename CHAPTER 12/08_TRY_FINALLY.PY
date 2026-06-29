def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Thank you, I am inside finally")

main()

# FINALLY IS USED TO OVERWRITE THE RETURN ARGUMENTS 