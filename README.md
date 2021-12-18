# PlanRadarQATask
This Project is built to be run on any operating system that has Docker installed on it without any further configuration
The purpose of this project is to:
  - Go to "Amazon.com"
  - Select any product from "All Categories" >> "Computers" >> "Computers & Tablets"
  - Add this product to the cart >> Assert that it's added
  - Remove that Product from the Cart >> Assert that it's removed
  
 This project run on chromium instance on a remote selenium server with --headless configuration (No GUI)
 ----------------------------------------------------------------------------------------------------------
 # Running the Project
  - Clone this repository 
  - Make sure to install Docker from https://docs.docker.com/get-docker/
  - After the project is cloned to your local machine >> Go to the project folder location
  - Inside that folder (Where you can see a file named Dockerfile) >> Start your command prompt/Git Bash
  - On command prompt terminal type the following orders:
      - docker-compose build  --------------> // then wait for the build to be done
      - docker-compose up  -----------> // Project will start in headless mode, however you will be able to
      -  monitor the logs from the command prompt
----------------------------------------------------------------------------------------------------------  
# Reading Project Results
    - Since this project runs in headless mode, you can monitor project run logs from command prompt 
    after running the command --> docker-compose up
    - I've put a printed confirmation message after each element and colored messages to be easy to read/follow
    - in case of failure (Last Assertion in the project is left failed on purpose for demonstration purposes), 
    the script will terminate and will take a screenshot of the last 
      step it took before the script crashed
    - Screenshots are saved in /app folder along with main class and other classes
    ----------------------------------------------------------------------------------------------------------
 # Running without docker
      - You'll need to run the script from main.py and modify the .env file with "CHROMEDRIVER_PATH" on your machine
      - Then replace driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=chrome_options.to_capabilities()) 
      WITH driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options) 
      on the "driverInitialization.py" file
      - And you'll need to download latest chrome driver and add to the project folder and assign it's path to "CHROMEDRIVER_PATH"
      - Then you'll need to setup python-dotenv and selenium
----------------------------------------------------------------------------------------------------------     
# Important Note
      - Waits in this project are implicit waits and it's for 60 seconds, but sometimes due to slow network connection,
      selenium fails to find a certain element and the script crashes
      - Usually I investigate more in these situation to find the perfect solution to avoid unneccesary crashes 
      and I try to avoid using sleep() as much as possible for better performance but i didn't have enough time for 
      these investigation in this Task.
