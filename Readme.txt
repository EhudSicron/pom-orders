This project includes 2 main folders:
1.	Project Orders
2.	Project Tasks
testing the site http://www.saucedemo.com
This was written by Playwright Object Oriented.
All class pages are in classes directory.
All tests’ files are in the test’s directory.
Each test uses the methods from the relevant classes.
All classes inherited from the Basepage class which had the basic Page functions

Install requierments:
pip install requierments

Install Allure
1. Open powershell as adimn 
2. Install scoop - used for installing Allure
	"Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')"
3. Install Allure - "scoop install allure"
4. Run Allure to display the allure-results reports - "allure serve allure-results"
5. Running maualy click modify run configuration and go to Edit run configuration - In 'Additional arguments' enter "--alluredir=allure_results"
6. Run tests

Runing 1 test with reports using treminal comand:
1. In terminal run : "pytest allure serve allure-results test_file_name::test_class::test_fun"
2. example: pytest --alluredir=allure_results test_2_add_2prod.py::Test_2_add_2prod::test_2_add_2prod


Install Chocolaty - tool to install Doker
1. Open powershell as adimn 
2. Run Get-ExecutionPolicy to verify admin prev
3. Run  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
4. Run choco install docker-desktop
5. Run "choco" to verify version  


Install Jenkins 
1. Download https://www.jenkins.io/download/thank-you-downloading-windows-installer-stable/
2. Run installtion, Select correct JAVA version (17-21)
3. If not install - Go to https://www.oracle.com/java/technologies/javase/jdk21-archive-downloads.html
4. Open Charome and go to "http://localhost:8080" jenkins setting
5. Copy the PSW from the text file in the path
6. Select Install suggested plugin





# 1. Create a file called config.py
# 2. Copy this code to the file (config.py)
# 3. Call this function to get values from the config.ini file (Ex. user = ConfigReader.read_config('email', 'user'))
import configparser
import sys



config file should be at the tests dir
class ConfigReader:

    @staticmethod
    def read_config(section, key):
        root_dir = sys.path[0]
        print("start url")
        print(root_dir)

        config = configparser.ConfigParser()
        config.read(root_dir + '\config.ini')

        # Check that the Section & key exists
        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]
        else:
            raise KeyError(f"Section '{section}' or key '{key}' not found in config.ini")
