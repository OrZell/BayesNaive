naive-base : V0/
├── Data/
│   ├── Logs.txt
│   └── phishing.csv
├── Classifier.py
├── Cleaner.py
├── Loader.py
├── Logger.py
├── Manager.py
├── Server.py
├── Tester.py
├── Trainer.py
├── requirements.txt
└── README.txt


Logs: Logs of the system about what made and when
phishing: The csv the Model based on
Classifier: The class who check the data by the model
Cleaner: Clean the data from nans and duplicates and set the index column
Loader: Load The file for the model
Logger: Write logs about the services and the processes
Manager: Manage all of the processes of the program
Server: The API to insert the ata row to check
Tester: Test the model to check how Accurate
Trainer: Train the model to check if iys made correctly
requirements: The packages that required to install

You have to run the backend container then run the frontend container and visit https://127.0.0.1:8000/check?data=...
and put the values of the row splited by ','.