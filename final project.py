# Pandas is a powerful library for data manipulation and analysis. It provides data structures like DataFrames and Series, which are similar to Excel spreadsheets
import pandas as pd
# It provides a comprehensive set of tools for creating high-quality 2D and 3D plots, charts, and graphs.
import matplotlib.pyplot as plt
# The os library in Python provides a way to interact with the operating system and perform various tasks.
import os 

def calculate_total_marks(df):
    df['Total_Marks'] = df.iloc[:, 1:].sum(axis=1)
    return df

def calculate_average_marks(df):
    df['Average_Marks'] = df['Total_Marks'] / 6.0
    return df

def calculate_percentage(df):
    df['Percentage'] = (df['Total_Marks'] / 600.0) * 100
    return df

def calculate_grade(df):
    grades = []
    for index, row in df.iterrows():
        if row['Percentage'] >= 90:
            grades.append('A')
        elif row['Percentage'] >= 80:
            grades.append('B')
        elif row['Percentage'] >= 70:
            grades.append('C')
        elif row['Percentage'] >= 60:
            grades.append('D')
        else:
            grades.append('F')
    df['Grade'] = grades
    return df

def main():
    # 1. Initialize an empty list to store the data
    data = []

    # 2. Get user inputs for each student and append to the data list
    while True:
        name = input("Enter the student's name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        marks = []
        for subject in ["Science", "Maths", "English", "Hindi", "SST", "IT"]:
            while True:
                try:
                    mark = float(input(f"Enter marks in {subject} (out of 100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Invalid input. Please enter marks between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        data.append([name, *marks])

    # 3. Create a pandas DataFrame from the data list
    df = pd.DataFrame(data, columns=["Name", "Science", "Maths", "English", "Hindi", "SST", "IT"])

    # 4. Print the DataFrame
    print(df)

    # 5. Save the DataFrame to a CSV file
    name = input("Enter the name of the CSV file: ")
    location = input("Enter the location to save the CSV file: ")
    full_path = os.path.join(location, name + ".csv")
    df.to_csv(full_path, index=False)

    # 6. Plot a line chart of the marks for each student
    for i, row in df.iterrows():
        plt.plot(["Science", "Maths", "English", "Hindi", "SST", "IT"], row[1:], label=row[0])
    plt.legend()
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.title("Performance in Class 10 Board")
    plt.show()

    # 7. Subject toppers
    n = int(input('Enter the number of toppers you want for each subject: '))
    for subject in ["Science", "Maths", "English", "Hindi", "SST", "IT"]:
        top_n_toppers = df.nlargest(n, subject)
        print(f"Top {n} toppers in {subject}:")
        for i, row in top_n_toppers.iterrows():
            print(f"{row['Name']} with marks {row[subject]}")
        print()

    # 8. Calculate total marks
    df = calculate_total_marks(df)

    # 9. Calculate average marks
    df = calculate_average_marks(df)

    # 10. Calculate percentage
    df = calculate_percentage(df)

    # 11. Print total, average, and percentage
    for i, row in df.iterrows():
        print(f"Total marks for {row['Name']}: {row['Total_Marks']:.2f}")
        print(f"Average marks for {row['Name']}: {row['Average_Marks']:.2f}")
        print(f"Percentage for {row['Name']}: {row['Percentage']:.2f}")
        print()

    # 12. Overall topper
    n = int(input('Enter the number of toppers you want: '))
    overall_topper = df.nlargest(n, 'Total_Marks')
    print(f"Top {n} overall toppers:")
    for i, row in overall_topper.iterrows():
        print(f"{row['Name']} with total marks {row['Total_Marks']:.2f}")

    # 13. Data for the pie chart
    labels = ['Science', 'Maths', 'English', 'Hindi', 'SST', 'IT']
    sizes = [df[subject].sum() for subject in labels]
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%.2f%%')
    plt.axis('equal')
    plt.title("Percentage of Total Marks")
    plt.show()

    # 14. Bar chart of total marks
    plt.figure(figsize=(10, 6))
    plt.bar(df['Name'], df['Total_Marks'])
    plt.xlabel("Name")
    plt.ylabel("Total Marks")
    plt.title("Total Marks of Each Student")
    plt.show()

    # 15. Histogram of average marks
    plt.figure(figsize=(10, 6))
    plt.hist(df['Average_Marks'], bins=10)
    plt.xlabel("Average Marks")
    plt.ylabel("Frequency")
    plt.title("Histogram of Average Marks")
    plt.show()

    # 16. Calculate grade
    df = calculate_grade(df)

    # 17. Print grade
    for i, row in df.iterrows():
        print(f"Grade for {row['Name']}: {row['Grade']}")

if __name__ == "__main__":
    main()
