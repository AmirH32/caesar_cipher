def encryption(SHIFT, password):
    encryptedPassword = ""
    asc_Z = ord("Z")
    asc_a = ord("a")
    asc_z = ord("z")
    
    for i in range(0, len(password)):
        # loops through the password's indexes
        asc = ord(password[i]) + SHIFT
        # Adds the shift onto the ascii value of the letter
        if (asc > asc_Z and asc < asc_a ) or asc > asc_z:
            # If the shift goes to a value beyond the alphabet, subtract 26 to go back to "a"/"A"
            # Using logic operations like this to see if the value is outside of boundraries for both upper and lowercase would be much faster than using isupper(), islower() functions.
            asc = asc - 26
        char = chr(asc)
        # Char becomes the character associated with the ascii value
        encryptedPassword += char
        # Adds each character to the encrypted password
        
    return encryptedPassword

def check(storedPassword, SHIFT):
    for attempts in range(2, -1, -1):
        password = input("Enter your password:")
        encryptedPassword = encryption(SHIFT, password)
        
        if encryptedPassword == storedPassword:
            access = True
            break
            # If encrypted password is the same as stored password, access is granted
        else:
            print(f"Invalid password - {attempts} attempts remaining...")
            access = False
            # Otherwise the password is invalid and the number of attempts remaining is displayed.
    return access
        
def main():
    storedPassword = "EHQAB6"
    SHIFT = 3
    access = check(storedPassword, SHIFT)
    if access == True:
        print("Access granted.")
    else:
        print("Access denied.")
    

main()