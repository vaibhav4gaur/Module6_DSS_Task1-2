# Module6_DSS_Task1-2
## Data Structures and Strings in Python
---
-  ### <ins>  Task 1:- Create a Dictionary of Student Marks </ins>

**Problem Statement :- Write a Python Program that :**
1. Creates a dictionary where student names are keys and their marks are values
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks
4. if the student's name is not found, display an appropriate message.

   *Coding Solving :- List in Dictionaries*
```
   sts_marks = {"AyushMishra":85,"VivekChaudhary":72,"ManuChauhan":90,"DheerajJatt":65,"ElvishBharat":78,"VirShow":44,"NickyAhl":68}
   sts_name = input("Enter the student's name: ")

   if sts_name in sts_marks:
      marks = sts_marks[sts_name]
      print(f"{sts_name}'s marks : {sts_marks}")
   else:
     print(f"Sorry,This user is not found.")
``` 
   - #### 🖼️ Screenshots
     <img width="1123" height="404" alt="Screenshot 2025-07-27 at 18 41 37" src="https://github.com/user-attachments/assets/32e9d71e-4409-41a8-8d45-3e40fe206f30" />
     
  - #### 📖 If the student does not exist in the dictinary:
     <img width="1128" height="449" alt="Screenshot 2025-07-27 at 18 42 12" src="https://github.com/user-attachments/assets/bb0e6144-ec14-4dff-a5e4-1f43476f7b64" />
     
- ### <ins> Task 2:- Demonstrate List Slicing </ins>

**Problem Statement :- Write a Python Program that:**
1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements from the list.
3. Reverses these extracted elements.
4. Prints both extracted list and the reversed list

   *Coding Solving :- Demo List Sliced*
```
 list = [1,2,3,4,5,6,7,8,9,10]
 print(f"Original list: {list}")
 list_extracts = list[:5]
 print(f"Extracted first five elements:{list_extracts}")
 list.reverse()
 print(f"Reversed extracted elements: {list[-5:]})
```
- #### 🖼️ Screenshots
   <img width="1062" height="386" alt="Screenshot 2025-07-27 at 19 01 32" src="https://github.com/user-attachments/assets/7b5ec5d3-94a6-48f7-afae-a7e98deff646" />

  
