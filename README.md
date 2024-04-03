# PythonProj
Blood Donation Project

INTRO:
The patients in need of the blood are able to request for the blood. Users can register themselves to become a donor. All users are also able to see all the donors list according to different blood groups as well as the list of all requested blood by different users or patients.
DBS acts as the bottom line database to store all the data of the donors and patients, maintains the proper records of the past few decades, regulate the various operation modules. Managing the critical tasks, efficiently handling the administrative processes.


WORKING OF THE CODE:
1. The patient in need gets the blood instantly if there is availability of that particular blood group and the blood table is updated by -1 in availability, else they are on waiting.
2. when a donor is donating, the person is waiting gets the blood and there is no change in the blood table. If no patient is on waiting the blood table gets updated by +1.


MODULES USED:
1. mysql.connector
2. json
