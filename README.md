# 🚀 Installation Guide

Follow these steps to get the project up and running on your system.

---

## 1. Install Python
  The project requires Python to run. Follow the instructions for your operating system:

### **Windows**
  1. Visit the [Python website](https://www.python.org/downloads/windows/).
  2. Click on **Python 3.14.3** (or the latest version) to download the `.exe` installer. 
     > **Note:** Do not download the "Install Manager."
     
     <img width="652" height="217" alt="image" src="https://github.com/user-attachments/assets/a7535049-2e15-4349-8d3e-41edc5456b79" />
  
  3. **Crucial:** When you run the `.exe`, make sure to check the boxes at the bottom:
     * **Use admin privileges when installing py.exe**
     * **Add python.exe to PATH**
     
     <img width="653" height="246" alt="image" src="https://github.com/user-attachments/assets/8cc547b7-1bd9-4af5-978c-85c81660f5af" />

4. Click **Install Now**.

### **Linux (Debian/Ubuntu)**
  Open your terminal and run:
  ```bash
  sudo apt update && sudo apt install python3
   ```

## 2. Download the Project
  1. Click the green **Code** button at the top of this repository.
  2. Select **Download ZIP**.
  3. **Extract** the ZIP file to a folder of your choice.
  4. Right-click inside the folder and select **Open in Terminal**.
    <img width="682" height="626" alt="image" src="https://github.com/user-attachments/assets/94671a4a-f915-460b-bf31-8401a28e8ea0" />
---

## 3. Run the Script
  In the terminal window you just opened, run the command for your operating system:

### **Windows (PowerShell)**
  ```powershell
  ./setup_windows.bat
  ```
### **Linux (Terminal)**
  ```terminal
  bash ./setup_linux.sh
  ```
  Exit the terminal for now
  
---

## 4. Create a Free Groq Account for API Key
1. Go to [groq.com](https://groq.com/).
2. Create an account and navigate to **API Keys** on the top right.
   
   <img width="566" height="566" alt="image" src="https://github.com/user-attachments/assets/c9cae88e-e8aa-4a23-bbbb-3ac674af526f" />

3. Create your key and **copy** it.
4. Open your `.env` file in a text editor and paste your key in the area shown below:

   <img width="603" height="325" alt="image" src="https://github.com/user-attachments/assets/1b517a66-5c6f-4fd4-883d-aae299db7252" />

> [!CAUTION]
> **IMPORTANT:** Do NOT delete the quotation marks `""`. Your key must stay inside them to work properly!


