# dataset_encryption.py
import pandas as pd
from cryptography.fernet import Fernet
from encryption import load_key

def encrypt_dataset(csv_path: str, output_path: str):
    """
    Reads a CSV file, converts it to a JSON string,
    encrypts the data, and saves the encrypted blob to an output file.
    """
    key = load_key()
    fernet = Fernet(key)
    df = pd.read_csv(csv_path)
    df_json = df.to_json(orient="records")
    encrypted_data = fernet.encrypt(df_json.encode())
    
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    
    print(f"Dataset encrypted and saved to {output_path}.")

def decrypt_dataset(encrypted_file_path: str) -> pd.DataFrame:
    """
    Reads an encrypted dataset file, decrypts it,
    and returns the original data as a pandas DataFrame.
    """
    key = load_key()
    fernet = Fernet(key)
    
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_str = fernet.decrypt(encrypted_data).decode()
    df = pd.read_json(decrypted_str, orient="records")
    return df
