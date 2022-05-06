# student-management
python program for student management for attendance and entering student data, using tkinter for UI and sqlite for database 

student management data has two functunalities 
1) taking student details and storing in database
2) updating attendance

In the first window, the user is asked if they want to enter student data or update attendance,
![1_start](https://user-images.githubusercontent.com/80886593/167182878-8597d38b-7068-4b7e-948e-e0d932b265c6.png)
 
1)for the student data window
the entry fields like name, department, registration number and gender is to be filled and when submitted the entered data is updated to the database using sql commands 
![2_top_submit](https://user-images.githubusercontent.com/80886593/167183222-025a1f79-9f77-4793-8ba1-95116bf42eec.png)


when "fill another entry " is clicked the existing data that is entered by the user is cleared ,providing space for the new data to be uploaded 
![2_top_anotherfield](https://user-images.githubusercontent.com/80886593/167183039-d3909ed3-8094-4504-8dcf-d02e0c136ff4.png)

when " show data is clicked " the data stored in table is displayed in another window 
![2_top_show_data](https://user-images.githubusercontent.com/80886593/167183277-e650bd9a-4599-4999-954e-01ebaff9f3f8.png)


2)for the attendance window
a list of students is displayed as check buttons . The attendance( no of days) of "checked" student names is updated(incremented by one)
![3_att_StudentList](https://user-images.githubusercontent.com/80886593/167183396-35710b44-6afb-4255-a1a1-cc26dbf1aa56.png)

when button "updated list " is clicked the updated attendance table is displayed in a new window

![3_att_updatedList](https://user-images.githubusercontent.com/80886593/167183464-0b059e82-8096-436a-b1a4-0398e952a7be.png)
