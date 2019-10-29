username = 'Sigrun'
password = 'SecretPassword'

usernameInput = input("Användarnamn? ")
if usernameInput != username:
    print("Ingen användare med detta namn finns  systemet")
else: 
    passwordInput = input("Lösenord? ")
    if passwordInput != password:
        print("Ogiltigt lösenord")
    else:
        print("Lyckad inloggning, välkommen!")