'''
Author: Seneca Greenwood
Description: Opens files and transfers data to a csv file by splitting up each part of data
Bugs: None that are aware
Features: Csv Files
Sources: Seneca Greenwood Election Data
'''
fhand = open("student_data_cs2.txt")      
    #opens file to access and read data

ohand = open("output_data_cs2.csv", "w")  
    #opens file to write in 

for line in fhand:
    id = (line[0:6]).strip()
    #print id's of students

    first_name = (line[6:21]).strip()
    #prints first names of students

    last_name = (line[21:36]).strip()
    #prints last name of students

    grade = (line[36:42]).strip()
    #prints grade's of students

    gpa = (line[42:48]).strip()
    #prints gpa's of students

    birth_date = (line[48:60]).strip()
    #prints birthday's of students

    gender = (line[60:67]).strip()
    #prints gender's of students

    class_rank = (line[67:76]).strip()
    #prints class rank's of students

    attend_pct = (line[76:86]).strip()
    #prints attendance percentage of students

    honors = (line[86:93]).strip()
    #prints honor's of students 

    sports = (line[93:102]).strip()
    #prints sport's of students

    club_count = (line[102:112]).strip()
    #prints club counts of students

    ohand.write(id + ", " + first_name + ", " + last_name + ", " + grade + ", " + gpa + ", " + birth_date + ", " + gender + ", " + class_rank + ", " + attend_pct + ", " + honors + ", " + sports + ", " + club_count + "\n")
    #prints all of the data in the new output file

    

