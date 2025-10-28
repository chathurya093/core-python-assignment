class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

def main():
    students = []
    while True:
        name = input("Enter student's name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        marks = input(f"Enter marks for {name} separated by commas: ").split(',')
        marks = [float(mark.strip()) for mark in marks]
        students.append(Student(name, marks))

    averages = {student.name: student.average() for student in students}
    top_performer = max(averages, key=averages.get)
    top_score = averages[top_performer]

    print("\nAverage Marks:")
    for name, avg in averages.items():
        print(f"{name}: {avg:.2f}")
    print(f"\nTop Performer: {top_performer} with an average of {top_score:.2f}")

if __name__ == "__main__":
    main()
