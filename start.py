import sys
import subprocess
import atexit
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.webdriver.chrome.options import Options
from PyPDF2 import PdfMerger
import getpass
import pyperclip
from selenium.webdriver.common.keys import Keys
import glob
import nbformat as nbf
import inquirer

print("\n\n")
print("*****************************************************************************************")
print("*****************************************************************************************")
print("*************                                                               *************")
print("*************       Welcome to Pdf Extractor for HackerRank Submissions     *************")
print("*************                    Tool created by                            *************")
print("*************                https://github.com/vokbuda                     *************")
print("*************                                                               *************")
print("*****************************************************************************************")
print("*****************************************************************************************")
print("\n\n")

# --- OS-Specific Setup Block ---
if sys.platform == "darwin":
    copy_paste_key = Keys.COMMAND
    try:
        caffeinate_proc = subprocess.Popen(['caffeinate', '-d'])
        atexit.register(caffeinate_proc.terminate)
        print("macOS detected: 'caffeinate' started automatically to prevent sleep.")
    except FileNotFoundError:
        print("Warning: 'caffeinate' command not found. Your Mac may sleep during execution.")
elif sys.platform == "win32":
    copy_paste_key = Keys.CONTROL
    print("\n" + "="*60)
    print("WARNING: WINDOWS DETECTED")
    print("   To ensure the script runs without interruption, please go to")
    print("   'Power & sleep settings' and set 'Screen' and 'Sleep'")
    print("   to 'Never' when your PC is plugged in.")
    print("="*60 + "\n")
else:
    copy_paste_key = Keys.CONTROL

start_time = time.time()

nb = nbf.v4.new_notebook()
current_directory = os.getcwd()

# Clean up previous run files
files_to_remove = glob.glob(os.path.join(current_directory, 'Submissions_Hackerrank*'))
if os.path.exists('merged_output.pdf'): os.remove('merged_output.pdf')
if os.path.exists('scripts.py'): os.remove('scripts.py')
if os.path.exists('scripts.ipynb'): os.remove('scripts.ipynb')

for file in files_to_remove:
    try:
        os.remove(file)
        print(f"Removed old file: {file}")
    except Exception as e:
        print(f"Error removing {file}: {e}")

while True:
    try:
        number_of_pages_hacker_rank = int(input("Please insert number of pages you want to extract: \n"))
        if number_of_pages_hacker_rank <= 0:
            raise ValueError("The number of pages must be a positive integer.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

question = [
        inquirer.List('option',
                      message="Select the output format for saving your submissions: ",
                      choices=['.py script',
                               '.ipynb notebook (every task in a separate cell)',
                               ' both'],
                      ),
    ]
answer = inquirer.prompt(question)
output_mapping = {
        '.py script': ('py', "Your submissions will be saved in a .py script."),
        '.ipynb notebook (every task in a separate cell)': ('ipynb', "Your submissions will be saved in a .ipynb notebook."),
        ' both': ('both', "Your submissions will be saved in both a .py script and a .ipynb notebook.")
    }
output_choice, message = output_mapping[answer['option']]
print(message, "\n")

username = input("Enter your HackerRank username: \n")
password = getpass.getpass("Insert your HackerRank password: \n")

current_directory = os.getcwd()
chrome_options = Options()
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument("--log-level=3")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

prefs = {
    "printing.print_preview_sticky_settings.appState": '{"recentDestinations":[{"id":"Save as PDF","origin":"local","account":""}],"selectedDestinationId":"Save as PDF","version":2}',
    "savefile.default_directory": current_directory
}
chrome_options.add_experimental_option("prefs", prefs)

def login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://www.hackerrank.com/login')
    
    username_field = driver.find_element(By.XPATH, "//*[@aria-label='Your username or email']")
    username_field.send_keys(username)
    
    password_field = driver.find_element(By.XPATH, "//*[@aria-label='Your password']")
    password_field.send_keys(password)
    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    
    driver.implicitly_wait(5)
    return driver

driver = login()
time.sleep(1)
main_dict = dict()

for i in range(number_of_pages_hacker_rank - 1, -1, -1):
    current_url = 'https://www.hackerrank.com/submissions/all/' + str(i + 1)
    driver.get(current_url)
    
    try:
        data_field = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//tbody[@role='rowgroup']"))
        )
        child_elements = data_field.find_elements(By.XPATH, "./*")
    except Exception as e:
        print(f"Could not find the submissions table on page {i+1}. It might be the last page. Stopping.")
        break

    if not child_elements:
        break

    rows = driver.find_elements(By.XPATH, "//tbody[@role='rowgroup']/tr[@role='row']")
    s_idx = len(rows) - 1
    for row in reversed(rows):
        row = driver.find_elements(By.XPATH, "//tbody[@role='rowgroup']/tr[@role='row']")[s_idx]
        s_idx -= 1

        a_element = row.find_element(By.TAG_NAME, 'a')
        a_property = a_element.get_attribute('href')
        columns = row.find_elements(By.TAG_NAME, 'td')
        
        if len(columns) >= 5 and (columns[1].text.strip().lower() in ['python3', 'pypy3']):
            fifth_column = columns[4]
            if a_property not in main_dict:
                main_dict[a_property] = float(fifth_column.text)
                modified_url = a_property + '/submissions'
                driver.get(modified_url)
                time.sleep(1.5)
                
                internal_cols = driver.find_elements(By.XPATH, "//div[@class='ellipsis submission-result']")
                for internal_col in internal_cols:
                    a_internal_element = internal_col.find_element(By.TAG_NAME, 'a')
                    a_property_internal = a_internal_element.get_attribute('href')
                    driver.get(a_property_internal)
                    
                    screen_code = driver.find_element(By.XPATH, "//div[@class='CodeMirror-cursor']")
                    driver.execute_script("arguments[0].scrollIntoView();", screen_code)

                    actions = ActionChains(driver)
                    actions.move_to_element(screen_code).click()
                    
                    actions.key_down(copy_paste_key).send_keys('a').key_up(copy_paste_key)
                    actions.key_down(copy_paste_key).send_keys('c').key_up(copy_paste_key)
                    actions.perform()

                    exname = driver.find_element(By.XPATH, "//h1[@class='ui-icon-label page-label']")
                    
                    copied_text = pyperclip.paste()
                    cleaned_text = copied_text.replace('\r\n', '\n').replace('\n\n', '\n')

                    if output_choice in {"py", "both"}:
                        with open("scripts.py", "a", encoding="utf-8") as file:
                            file.write(f'# {exname.text}\n')
                            file.write(cleaned_text)
                            file.write("\n\n")
                        print(f"'{exname.text}' has been saved to scripts.py")

                    if output_choice in {"ipynb", "both"}:
                        nb.cells.append(nbf.v4.new_markdown_cell(f"# {exname.text}"))
                        nb.cells.append(nbf.v4.new_code_cell(cleaned_text))
                        with open('scripts.ipynb', 'w', encoding="utf-8") as f:
                            nbf.write(nb, f)
                        print(f"'{exname.text}' has been saved to scripts.ipynb")
                    
                    break
                
                driver.get(current_url)
                time.sleep(0.5)

    time.sleep(0.5)
    driver.execute_script('window.print();')
    time.sleep(0.5)

current_directory = os.getcwd()
merger = PdfMerger()

def extract_number(filename):
    """Extracts the number from parenthesis in a filename for proper sorting."""
    match = re.search(r'\((\d+)\)', filename)
    if match:
        return int(match.group(1))
    # If no number (the base file), return 0 to ensure it's first
    return 0

all_pdf_files = [f for f in os.listdir(current_directory) if f.startswith('Submissions _ HackerRank') and f.endswith('.pdf')]

pdf_files = sorted(all_pdf_files, key=extract_number)

for pdf_file in pdf_files:
    if os.path.exists(pdf_file):
        with open(pdf_file, 'rb') as f:
            merger.append(f)
        os.remove(pdf_file)

output_filename = "merged_output.pdf"
with open(output_filename, 'wb') as output_file:
    merger.write(output_file)
merger.close()
print(f"\nAll PDFs merged into {output_filename}")

driver.quit()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total elapsed time: {elapsed_time:.2f} seconds")