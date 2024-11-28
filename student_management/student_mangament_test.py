import unittest
from student_mangament import StudentManagement  # Import your main class

class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        """Set up test cases."""
        self.student_management = StudentManagement()

    def test_add_student(self):
        """Test adding a new student."""
        result = self.student_management.add_student("John", 21)
        self.assertEqual(result, "Student added successfully")

    def test_update_student(self):
        """Test retrieving a student."""
        self.student_management.add_student("Alice", 22)
        student = self.student_management.get_student("Alice")
        self.assertEqual(student, {"name": "Alice", "age": 22})

    def test_remove_student(self):
        """Test removing a student."""
        self.student_management.add_student("Bob", 20)
        result = self.student_management.remove_student("Bob")
        self.assertEqual(result, "Student removed successfully")

    def test_student_not_found(self):
        """Test when a student is not found."""
        result = self.student_management.get_student("Nonexistent")
        self.assertEqual(result, "Student not found")

if __name__ == '__main__':
    unittest.main()
