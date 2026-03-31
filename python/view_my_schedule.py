import json
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
STUDENTS_FILE = DATA_DIR / "students.json"
COURSES_FILE = DATA_DIR / "courses.json"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def index_by(items, key):
    return {item[key]: item for item in items}


def print_schedule(student, courses_by_code):
    enrolled_codes = student.get("enrolledCourses", [])

    print("=" * 60)
    print(f"VIEW MY SCHEDULE - {student['name']} [{student['id']}]")
    print("=" * 60)

    if not enrolled_codes:
        print("You are not enrolled in any courses.")
        return

    total_credits = 0
    print(f"{'Code':<10} {'Title':<30} {'Credits':<8} Time")
    print("-" * 60)

    for code in enrolled_codes:
        course = courses_by_code.get(code)
        if not course:
            continue

        credits = course.get("credits", 0)
        total_credits += credits

        time_slot = course.get("timeSlot") or {}
        days = time_slot.get("days", "TBA")
        start = time_slot.get("startTime", "")
        end = time_slot.get("endTime", "")
        time_text = f"{days} {start}-{end}".strip()

        print(f"{course['code']:<10} {course['title']:<30} {credits:<8} {time_text}")

    print("-" * 60)
    print(f"Total Credits Enrolled: {total_credits}")


def main():
    students = load_json(STUDENTS_FILE)
    courses = load_json(COURSES_FILE)

    students_by_id = index_by(students, "id")
    courses_by_code = index_by(courses, "code")

    student_id = input("Enter your Student ID: ").strip()
    student = students_by_id.get(student_id)

    if not student:
        print("Student ID not found.")
        return

    print_schedule(student, courses_by_code)


if __name__ == "__main__":
    main()
