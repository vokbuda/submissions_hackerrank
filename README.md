# submissions_hackerrank
Tool for hackerrank submissions which creates a PDF with submitted solutions<br>(includes also creation of python files with all solutions) - ADM

**Now with support for both Windows and macOS!**

---
## Recent Updates
- **[10/2025]**: Added full support for **macOS**, including automatic sleep prevention. 

---

---
## Prerequisites
Before you start, make sure you have the following installed on your computer:
* **Python 3**: If you don't have it, download it from [python.org](https://www.python.org/).
* **Google Chrome**: The script uses Chrome to automate the process, so you'll need the browser installed.


## Installation & Setup

Follow these steps to get the tool ready to run.

### Step 1: Get the Code
Clone this repository or download the ZIP file and unzip it to a dedicated folder on your computer.

### Step 2: Create a Virtual Environment (Optional but Recommended)
Using a virtual environment is the best way to manage project dependencies and avoid conflicts with other Python projects.

1.  **Open your terminal** (Command Prompt on Windows, Terminal on macOS) and navigate to the project folder.
2.  **Create the environment** by running:
    ```bash
    python -m venv venv
    ```
3.  **Activate the environment**. This command is different for each OS:

    <details>
    <summary><b>► On Windows (Command Prompt)</b></summary>
    
    ```bash
    venv\Scripts\activate
    ```
    </details>

    <details>
    <summary><b>► On macOS</b></summary>
    
    ```bash
    source venv/bin/activate
    ```
    </details>

    You'll know it's active when you see `(venv)` at the beginning of your terminal prompt.

### Step 3: Install Required Libraries
With your environment active, install all the necessary packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```


---
## How to Run the Script

1.  Make sure your virtual environment is **active**.
2.  Run the script from your terminal:
    ```bash
    python start.py
    ```
    *(Note: On macOS, you may need to use `python3 start.py`)*

3.  Follow the on-screen prompts:
    * First, enter the **number of submission pages** you want to scrape.
      ![image](https://github.com/user-attachments/assets/c8b7033d-4dea-4f41-ab62-aa508e0b7647)
    * Next, choose your desired **output format** (.py, .ipynb, or both).
    * Finally, enter your HackerRank **username** and **password**.

    > **What if I use Google/Facebook to log in?**
    > If you use a social login, you can set a password for your HackerRank account by using the "Forgot Password" feature with the email associated with your social account.

    **Your credentials are safe.** The script only uses them to log in to HackerRank and does not store or send them anywhere. You can review the code to verify this.


---
## Expected Output
Once the script finishes, you will find the following files in your project folder:

* **`merged_output.pdf`**: A single, consolidated PDF file containing screenshots of all your submission pages.

* **`scripts.py`** *(Optional)*: A Python script containing all your scraped code solutions. Each solution is preceded by a comment with the problem's title, making it easy to search. This file is generated if you selected the `.py script` or `both` option.

* **`scripts.ipynb`** *(Optional)*: A Jupyter Notebook for a more organized view of your solutions. Each problem is placed in its own section, with the title in a Markdown cell followed by the code in a code cell. This file is generated if you selected the `.ipynb notebook` or `both` option.

---
## Important Usage Notes

* **Execution Time**: The script will take approximately **20 minutes** to complete. This is not due to hardware limitations but because of intentional delays added to prevent HackerRank from detecting and blocking the script as a bot.
* **Do Not Use Your Computer**: It is highly recommended to let the script run without using your computer. The most critical point of failure is using the **copy-paste function** (`Ctrl+C`/`Cmd+C`), as the script relies on your system's clipboard to scrape the code.
* **Sleep Prevention**:
    * **macOS**: The script automatically calls `caffeinate` to prevent your Mac from sleeping during execution.
    * **Windows**: You must **manually change your power settings** to prevent your PC from sleeping. Go to `Settings > System > Power & sleep` and set "Sleep" to "Never" while plugged in.

---
##  troubleshooting

If you run into issues, check these common solutions.

<details>
<summary><b>► Windows Troubleshooting</b></summary>

* **Problem:** The command `python` is not recognized.
    * **Cause:** Python was not added to your system's PATH during installation.
    * **Solution:** The easiest fix is to **reinstall Python**. Run the official installer again and make sure to check the box at the bottom that says **"Add python.exe to PATH"**.

* **Problem:** When activating the environment in PowerShell, you get a red error message about `Execution Policies`.
    * **Cause:** PowerShell has a security feature that blocks scripts from running by default.
    * **Solution:** You can either **use Command Prompt (`cmd`)** instead, or run the following command in PowerShell to allow scripts for your current session only (it's safe and resets when you close the window):
        ```powershell
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
        ```
</details>