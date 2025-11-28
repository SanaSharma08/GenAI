1. python -m venv .venv
2. .venv\Scripts\activate
// create requirements.txt and store all dependencies there along with required versions. 
3. pip install -r requirements.txt
// Always work in Virtual Enviornment (venv) to make your software/package independent of your system setup so that the code can be shared across systems and the dependies can easily be installed on another client.
4. deactivate 
//deactivate venv at the end, delete the venv folder before shipping your code. The receiver client will create their venv and install dependencies from requirements.txt to use your software.