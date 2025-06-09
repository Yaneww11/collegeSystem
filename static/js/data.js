// Complete data management implementation
const DataManager = {
    // College Data
    collegeInfo: {
        name: localStorage.getItem('collegeName') || 'College Management System',
        address: localStorage.getItem('collegeAddress') || '123 Education Street'
    },

    // Departments
    departments: JSON.parse(localStorage.getItem('departments')) || [],
    
    // Courses
    courses: JSON.parse(localStorage.getItem('courses')) || [],
    
    // Teachers
    teachers: JSON.parse(localStorage.getItem('teachers')) || [],
    
    // Students
    students: JSON.parse(localStorage.getItem('students')) || [],
    
    // Grades
    grades: JSON.parse(localStorage.getItem('grades')) || [],
    
    // Save All Data
    saveAll: function() {
        localStorage.setItem('collegeName', this.collegeInfo.name);
        localStorage.setItem('collegeAddress', this.collegeInfo.address);
        localStorage.setItem('departments', JSON.stringify(this.departments));
        localStorage.setItem('courses', JSON.stringify(this.courses));
        localStorage.setItem('teachers', JSON.stringify(this.teachers));
        localStorage.setItem('students', JSON.stringify(this.students));
        localStorage.setItem('grades', JSON.stringify(this.grades));
    },
    
    // CRUD Operations
    addDepartment: function(dept) {
        dept.id = Date.now().toString();
        this.departments.push(dept);
        this.saveAll();
        return dept;
    },
    
    updateDepartment: function(id, updates) {
        const index = this.departments.findIndex(d => d.id === id);
        if (index > -1) {
            this.departments[index] = {...this.departments[index], ...updates};
            this.saveAll();
            return true;
        }
        return false;
    },
    
    // Similar CRUD methods for other entities...
    
    // Grade Management
    addGrade: function(studentId, courseId, grade) {
        const newGrade = {
            id: Date.now().toString(),
            studentId,
            courseId,
            grade,
            date: new Date().toISOString()
        };
        this.grades.push(newGrade);
        this.saveAll();
        return newGrade;
    }
};

// Initialize sample data if empty
if (DataManager.departments.length === 0) {
    DataManager.addDepartment({
        name: 'Computer Science',
        faculty: 'Engineering',
        head: 'Dr. Smith'
    });
}

// Export for other modules
window.DataManager = DataManager;
