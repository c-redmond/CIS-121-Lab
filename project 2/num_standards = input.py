num_standards = input
if num_standards == 57:
    grade = "A+"
if num_standards >= 53:
    grade = "A"
if num_standards >= 51:
    grade = "A-"
if num_standards >= 49:
    grade = "B+"
if num_standards >= 47:
    grade = "B"
if num_standards >= 45:
    grade = "B-"
if num_standards >= 43:
    grade = "C+"
if num_standards >= 40:
    grade = "C"
if num_standards >= 35:
    grade = "D"
if num_standards < 35:
    grade = "F"
  print(grade)