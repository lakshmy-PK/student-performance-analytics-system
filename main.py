import pandas as pd
df = pd.read_csv("students.csv")
def view_students():
    print("\n--- STUDENT DETAILS ---")
    print(df)
def find_topper():
    df["total"]=df["maths"]+df["physics"]+df["python"]
    topper = df.loc[df["total"].idxmax()]

    print("\nTOPPER DETAILS")
    print("ID:", topper["id"])
    print("Name:", topper["name"])
    print("Total Marks:", topper["total"])

def class_average():

    df["total"] = df["maths"] + df["physics"] + df["python"]

    avg = df["total"].mean()

    print("\nCLASS AVERAGE")
    print("Average Marks:", round(avg, 2))

def subject_averages():

    maths_avg = df["maths"].mean()
    physics_avg = df["physics"].mean()
    python_avg = df["python"].mean()

    print("\nSUBJECT-WISE AVERAGES")
    print("maths   :", round(maths_avg, 2))
    print("physics :", round(physics_avg, 2))
    print("python  :", round(python_avg, 2))
def pass_fail_analysis():

    passed = df[
        (df["maths"] >= 40) &
        (df["physics"] >= 40) &
        (df["python"] >= 40)
    ]

    failed = df[
        (df["maths"] < 40) |
        (df["physics"] < 40) |
        (df["python"] < 40)
    ]

    print("\nPASS / FAIL ANALYSIS")
    print("Passed Students :", len(passed))
    print("Failed Students :", len(failed))

def subject_toppers():

    maths_topper = df.loc[df["maths"].idxmax()]
    physics_topper = df.loc[df["physics"].idxmax()]
    python_topper = df.loc[df["python"].idxmax()]

    print("\nSUBJECT TOPPERS")

    print("Maths Topper   :", maths_topper["name"],
          "-", maths_topper["maths"])

    print("Physics Topper :", physics_topper["name"],
          "-", physics_topper["physics"])

    print("Python Topper  :", python_topper["name"],
          "-", python_topper["python"])

def students_above_average():

    df["total"] = df["maths"] + df["physics"] + df["python"]

    avg = df["total"].mean()

    above_avg = df[df["total"] > avg]

    print("\nSTUDENTS ABOVE CLASS AVERAGE")
    print("Class Average:", round(avg, 2))

    for _, row in above_avg.iterrows():
        print(row["name"], "-", row["total"])

def export_report():

    report_df = df.copy()

    report_df["total"] = (
        report_df["maths"] +
        report_df["physics"] +
        report_df["python"]
    )

    report_df["result"] = report_df.apply(
        lambda row: "Pass"
        if row["maths"] >= 40
        and row["physics"] >= 40
        and row["python"] >= 40
        else "Fail",
        axis=1
    )

    report_df.to_csv(
        "analysis_report.csv",
        index=False
    )

    print("Report Exported Successfully!")

while True:
    print("\nSTUDENT PERFORMANCE ANALYTICS")
    print("1. View Students")
    print("2. Find Topper")
    print("3. Class Average")
    print("4. Subject Averages")
    print("5. Pass/Fail Analysis")
    print("6. Subject Topper")
    print("7. Students Above Average")
    print("8. Export Report")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        view_students()
    elif choice == 2:
        find_topper()
    elif choice == 3:
        class_average()
    elif choice == 4:
        subject_averages()
    elif choice == 5:
        pass_fail_analysis()
    elif choice == 6:
        subject_toppers()
    elif choice == 7:
        students_above_average()
    elif choice == 8:
        export_report()
    elif choice == 9:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")