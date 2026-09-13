"""You are developing a Secure Password Vault for a computer system. The password must be protected from direct access while the user should still be able to verify and change it through appropriate methods. Design and implement a Python class named PasswordVault.
 The class should contain: ( username as a public variable,  vault_status as a protected variable, password 
as a private variable)
 Implement the following methods: [ change_password(),verify_password(),display_status()]
 The verify_password() method should check whether the entered password matches the stored password.
 If the password is correct, display: “Access Granted” , Otherwise, display: Access Denied"""

class PasswordVault():
    def __init__(self,username,vault_status,password):
        self.username=username
        self._vault_status=vault_status
        self.__password=password

    def change_password(self, newPassword):
        self.__password=newPassword
        print("Password changed.")

    def verify_password(self, eneterdPassword):
        if eneterdPassword==self.__password:
            print("Access Granted")
        else:
            print("Access Denied")

    def display_status(self):
        print("The vault status is: ", self._vault_status)

    
user = PasswordVault("Vinod114","Active","k250114")

user.display_status()
user.verify_password("k250114")
user.change_password("25k0114")