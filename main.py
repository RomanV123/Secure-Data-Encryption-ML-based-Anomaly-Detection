# main.py
from encryption import encrypt_password, decrypt_password
from dataset_encryption import encrypt_dataset, decrypt_dataset

def main_menu():
    print("\nWelcome to AI-Driven CryptoVault")
    print("Select an option:")
    print("1. Encrypt a password")
    print("2. Decrypt a password")
    print("3. Encrypt a dataset (CSV)")
    print("4. Decrypt a dataset")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            password = input("Enter the password to encrypt: ")
            encrypted = encrypt_password(password)
            print(f"Encrypted password: {encrypted.decode()}")
        
        elif choice == '2':
            encrypted = input("Enter the encrypted password: ")
            try:
                decrypted = decrypt_password(encrypted.encode())
                print(f"Decrypted password: {decrypted}")
            except Exception as e:
                print("Failed to decrypt password. Please check your input and key.")
        
        elif choice == '3':
            csv_path = input("Enter the path to your CSV file: ")
            output_path = input("Enter the output file name for encrypted data: ")
            encrypt_dataset(csv_path, output_path)
        
        elif choice == '4':
            encrypted_file_path = input("Enter the path to the encrypted dataset file: ")
            try:
                df = decrypt_dataset(encrypted_file_path)
                print("Decrypted Dataset:")
                print(df.head())
            except Exception as e:
                print("Failed to decrypt dataset. Please check your file and key.")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
