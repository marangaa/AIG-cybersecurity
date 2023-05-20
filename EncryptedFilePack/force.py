import zipfile


def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except RuntimeError as e:
        if 'Bad password' in str(e):
            return False
        else:
            raise


def decrypt_zip(zip_path, password_file):
    with zipfile.ZipFile(zip_path) as zip_file:
        with open(password_file, 'r') as file:
            for line in file:
                password = line.strip()
                if extract_zip(zip_file, password):
                    print(f"Password found: {password}")
                    return True
    print("Password not found.")
    return False


# Example usage
zip_path = "enc.zip"
password_file = "rockyou.txt"

decrypt_zip(zip_path, password_file)
