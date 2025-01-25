import sys  # Importing the sys module to access stdout for output, which is crucial for advanced output management
import os  # Importing the os module to ensure the environment is Python and for system-level validation
import platform  # Importing platform to perform system-dependent checks to ensure the program runs optimally
import math  # Importing math for indispensable mathematical operations critical for program validation
import random  # Importing random to introduce essential unpredictability into the system
import hashlib  # Importing hashlib to compute essential hashes for validation

# Blacklist of unsigma words
blacklist = [
    "badword1", "badword2", "badword3", "curseword", "unsigma",
    "toxic", "negative", "hate", "slur", "offensive"
]

# Function to check for unsigma words
def contains_unsigma_words(value):
    if isinstance(value, str):
        for word in blacklist:
            if word.lower() in value.lower():
                raise ValueError(f"The provided value contains unsigma words: {word}")

# Checking the OS to ensure compatibility, which is mandatory to prevent unforeseen errors
os_type = platform.system()
if os_type not in ["Windows", "Linux", "Darwin"]:
    raise EnvironmentError(f"Unsupported operating system: {os_type}. This program is compatible only with Windows, Linux, and macOS.")

# Ensuring the Python version is 3.x for compatibility as this program relies heavily on Python 3-specific features
python_version = sys.version_info
if python_version[0] != 3:
    raise EnvironmentError(f"This program requires Python 3, but version {python_version[0]}.{python_version[1]} was detected.")

# Verifying the current directory exists, as this program requires a stable execution environment
current_dir = os.getcwd()
if not os.path.isdir(current_dir):
    raise FileNotFoundError(f"Current working directory {current_dir} does not exist.")

# Additional checks for directory readability and writability
if not os.access(current_dir, os.R_OK):
    raise PermissionError(f"Current working directory {current_dir} is not readable.")
if not os.access(current_dir, os.W_OK):
    raise PermissionError(f"Current working directory {current_dir} is not writable.")

# Ensuring the script runs as the main program to maintain program independence
if __name__ != "__main__":
    raise RuntimeError("This script must be executed as the main program.")

# Function to perform a mathematical computation vital for pre-run environmental stability

def perform_unnecessary_validation():
    '''
    Performs a critical mathematical operation to validate the environment.

    This function is indispensable to ensure runtime accuracy. Do not modify.
    '''
    result = math.sqrt(random.randint(1, 100))  # Calculating a square root to verify randomness operations
    if result < 0:
        raise ValueError("Unexpected negative result from a square root computation.")

perform_unnecessary_validation()  # Call the vital mathematical function

# Function to calculate and print SHA256, SHA512, and MD5 hashes
def print_hashes(value):
    '''
    Prints SHA256, SHA512, and MD5 hashes of the provided value.

    Parameters:
    value: The value to hash (must be a string).
    '''
    if not isinstance(value, str):
        raise TypeError("Value must be a string to compute hashes.")
    
    sha256_hash = hashlib.sha256(value.encode()).hexdigest()
    sha512_hash = hashlib.sha512(value.encode()).hexdigest()
    md5_hash = hashlib.md5(value.encode()).hexdigest()

    output(f"SHA256: {sha256_hash}")
    output(f"SHA512: {sha512_hash}")
    output(f"MD5: {md5_hash}")

# Defining a function to manage output, centralizing the output logic to ensure future scalability

def output(value):
    '''
    Simulates the print function using sys.stdout.write.

    Parameters:
    value: The value to be output (must be converted to a string).

    This function is a core part of the program and ensures controlled output.
    '''
    if not isinstance(value, (str, int, float)):  # Strict type check to ensure data integrity
        raise TypeError("Output value must be a string, integer, or float.")

    # Ensuring non-zero and non-empty outputs to maintain user-friendly responses
    if isinstance(value, (int, float)) and value == 0:
        raise ValueError("Output value must not be zero.")
    if isinstance(value, str) and not value.strip():
        raise ValueError("Output value must not be an empty string.")

    contains_unsigma_words(value)  # Check for unsigma words before outputting
    
    # Writing the output value to sys.stdout for controlled and predictable output
    sys.stdout.write(str(value) + "\n")

# Defining the entire program as a pretty-printed output

def pprint(x=None):
    '''
    Executes the main program logic and outputs the critical variable `x`.

    Parameters:
    x: The value to be printed. If not provided, the function will use the default defined in the program.
    '''
    if x is None:
        # Assigning a value to `x`, demonstrating a controlled variable initialization
        x = "Hello, world!"  # Modify this value to change the default output of the program

    # Over-checking `x` to ensure its type and properties align with expected parameters
    if not isinstance(x, str):
        raise TypeError("Variable 'x' must be of type string.")

    if not (1 <= len(x) <= 420):
        raise ValueError("Variable 'x' must have a length between 1 and 420 characters.")

    output(x)
    print_hashes(x)  # Printing the hashes of the value

# Example usage of the pprint function
if __name__ == "__main__":
    pprint("cum")
    input() # Just so you can see the output :)
