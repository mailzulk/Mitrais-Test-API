This project is created using Python 3.6

``` bash
Steps to run this project:

# Install virtual-env
    virtualenv <virtual-env-name>
    
# Activate virtualenv
    #### For Linux:
        source <virtual-env-name>/bin/activate
    #### For Windows:
        <virtual-env-name>/Scripts/Activate.bat
        
# Get into project folder
    cd <project-folder>
    
# Install project dependencies
    pip install -r requirements.txt
    
# Migrate models to database
    #### !! Make sure to fill your database credentials first in config.py !!
    python migrate.py db init
    python migrate.py db migrate
    python migrate.py db upgrade
    
# Run the project
    python run.py
```