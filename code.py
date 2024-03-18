import json

from mysql.connector import (connection)
cnx = connection.MySQLConnection(user='root', password='1234', host='localhost', database='BLOODDONATION') 
mycursor=cnx.cursor(buffered=True)
mycursor.execute("use BloodDonation;")
mycursor.execute("show tables")
mycursor.fetchall()
mycursor.execute("""create table Blood(id int not null, BloodGroup varchar(50) not null,Availability int not null,
primary key(BloodGroup));""")
mycursor.execute("""create table Patient(id int not null auto_increment, PatientDetails varchar(6203),BloodGroup varchar(40)
,Status varchar(40) DEFAULT 'Waiting', primary key(id),FOREIGN KEY(BloodGroup) references BLood(BloodGroup))""")
mycursor.execute("""create table Donor(DonorId int(11) not null auto_increment PRIMARY KEY, DonorDetails varchar(6023),
BloodGroup varchar(40) not null,FOREIGN KEY(BloodGroup) references BLood(BloodGroup));""")
cnx.commit()

#patient name entering
def Patientinsert():
    print("WELCOME TO THE PATIENT DETAILS INSERTION!")
    details={}
    details['Patient name']=input("Enter The Name:")
    details['Disease']=input("Enter the disease separated by comma:")
    details['Age']=input("Enter the age:")
    data = json.dumps(details)
    bloodgrp=input("Enter bloodgroup:")
    sqlstat="insert into patient(PatientDetails,Bloodgroup) values(%s,%s);"
    value=(data,bloodgrp)
    mycursor.execute(sqlstat,value)
    cnx.commit()
    print("DATA INSERTED")

    mycursor.execute(f"Select id FROM patient where Status ='Waiting' ORDER BY id LIMIT 1")
    user_id=mycursor.fetchone()
    mycursor.execute(f"select BloodId,Availability from blood where BloodGroup='{bloodgrp}';")
    data=mycursor.fetchone()
    if data[1]>0:
        mycursor.execute(f"update patient set Status='Received' where id='{user_id[0]}';")
        mycursor.execute(f"update blood set Availability =Availability -1 where BloodId='{data[0]}';")
    else:
        print("YOU ARE ON WAITING!")
    

#donar checking
def Donorinsert():
    print("WELCOME TO THE DONOR DETAILS INSERTION")
    details={}
    details['Name']=input("Enter the name:")
    details['Age']=input("Enter the age")
    data = json.dumps(details)
    bloodgrp=input("Enter the bloodgroup:")
    sqlstat="insert into donor(DonorDetails,BloodGroup) values(%s,%s);"
    value=(data,bloodgrp)
    mycursor.execute(sqlstat,value)
    cnx.commit()
    print("DATA INSERTED!")
    try:
        mycursor.execute(f"Select id FROM patient where Status ='Waiting' and BloodGroup='{bloodgrp}' ORDER BY id LIMIT 1")
        user_id=mycursor.fetchone()
        mycursor.execute(f"update patient set Status='Received' where id='{user_id[0]}';")
        cnx.commit()
        print("BLOOD SENT TO THE NEEDY! YOU JUST SAVED A LIFE!")
    except:
        mycursor.execute(f"Select BloodGroup FROM donor ORDER BY DonorId DESC LIMIT 1;")
        user_blood=mycursor.fetchone()
        mycursor.execute(f"update blood set Availability=Availability+1 where BloodGroup='{user_blood[0]}';")
        cnx.commit()
        print("BLOOD TABLE UPDATED")


#main work
ch='y'
while ch=='y':
    print("Main menu \n1.Donor \n2.Patient")
    a=input("Enter your choice:")
    if a=='2':
        Patientinsert()
        break
    elif a=='1':
        Donorinsert()
        print("THANK YOU...BE A REGULAR BLOOD DONOR!!")
        break