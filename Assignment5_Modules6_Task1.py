sts_marks = {"AyushMishra": 85,"VivekChaudhary": 72,"ManuChauhan": 90,"DheerajJatt": 65,"ElvishBharat": 78,"VirShow":44,"NickyAhl":68}
sts_name = input("Enter the student's name: ")
if sts_name in sts_marks:
    marks = sts_marks[sts_name]
    print(f"{sts_name}'s marks : {marks}")
else:
    print(f"Sorry,This user is not found.")
