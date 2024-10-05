# submissions_hackerrank
Tool for hackerrank submissions which creates a PDF with submitted solutions<br>(includes also creation of python file with all solutions) - ADM

before start you should have **Python** and **Chrome** installed on pc(I tested only on **Windows**)
## Recent Updates
- **[01/10/2024]**: Added only support of exercises **Python/PyPy3**, thanks to [@LinCanNerd](https://github.com/LinCanNerd)


## Execute the following instructions<br/> 

- in command line ```pip install selenium webdriver-manager PyPDF2 pyperclip nbformat inquirer```<br/><br/>
- Position in folder where you put _start.py_. 
It is recommended to create a dedicated folder for this purpose, as having other .pdf files in the same directory may not yield the expected results. <br/><br/>
- Then execute in command line ```python start.py```<br/><br/>
- After completing all steps, you will see the following screen:<br/><br/>
![image](https://github.com/user-attachments/assets/044aba67-dbc3-41c1-9191-eaa0a2938903)
- Insert the **number of pages** from HackerRank that you need to submit. In my case, I have _20 pages_, but I only need to submit _15_, so I will enter _15_<br/><br/>
![image](https://github.com/user-attachments/assets/c8b7033d-4dea-4f41-ab62-aa508e0b7647)
- Now the program will ask you if you want to save your submissions in a .py script, a .ipynb notebook or both. <br/><br/>
- After that, the program will ask for your HackerRank **username** and **password**. <br/><br/>

- If you signed in using Google or another service (e.g., Facebook, GitHub), you can retrieve your password by following the password recovery process using the email associated with your account. <br/><br/>

- Enter your **credentials** (make sure you input them correctly, otherwise close everything and run  ```python start.py``` the second time). <br/><br/>
$${\color{green}Don’t\space worry\space about\space your\space credentials;you\space can\space check\space my\space code, and\space I\space won't\space send\space them\space anywhere.}$$
<br/></br>
- Once these steps are done, the program will start working (it takes approximately **23 minutes** on my laptop with 16GB RAM and an Intel i7 processor). Do not close the Chrome window during this operation. You can continue using your computer for other tasks while the program runs, but please refrain from using the copy-paste functionality. Using copy-paste during this time may result in incorrect text being processed, as the program relies on the clipboard to manage content.</br></br>
- After the process is complete last two lines in prompt are about merged files and elapsed time, you will find the files _scripts.py_ and _merged_output.pdf_ in the same directory as _start.py_

