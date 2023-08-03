import random

dataDir = f"{__file__}\\..\\static\\names\\"

def get_random_name():
    dataFilePath = dataDir
    random_number = random.randint(0,1)
    # Male name
    if random_number == 0:
        return get_random_male()
    else:
        return get_random_female()
    
def get_random_male():
    return _get_random_name_from_file(dataDir + "males.txt")
    
def get_random_female():
    return _get_random_name_from_file(dataDir + "females.txt")

def _get_random_name_from_file(dataFilePath):
    # Read random line from file or return error if file not found
    try:
        with open(dataFilePath, "r") as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
            # Check if file is empty
            if len(lines) == 0:
                print(f"Error: File is empty: \'{dataFilePath}\'")
                return ""
            # Return random line
            random_line = random.choice(lines)
            return random_line
        
    except FileNotFoundError:
        print(f"Error: File not found: \'{dataFilePath}\'")
        return ""