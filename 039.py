# LEVEL 039

# ----------------------
# -- GROUPING STUDENTS-- 
# ----------------------

def main():
        students = int(input("How many students you pretend group? R: "))
        num = int(input("How many students per group? R: "))
        groups = students // num
        remain = students % num
        print(f"You have {groups:.0f} groups of students, with a remain of {remain:.0f}")

if __name__ == "__main__":
    main()