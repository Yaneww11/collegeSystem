// Core Application Logic
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});

function initializeApp() {
    loadData();
    setupEventListeners();
    checkAuthStatus();
    renderHomePage();
}

function setupEventListeners() {
    // Navigation
    document.querySelectorAll('a[data-page]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const page = e.target.dataset.page;
            renderPage(page);
        });
    });

    // Modals
    document.querySelectorAll('.modal .close').forEach(closeBtn => {
        closeBtn.addEventListener('click', () => {
            closeAllModals();
        });
    });

    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal')) {
            closeAllModals();
        }
    });

    // Auth Buttons
    document.getElementById('login-btn').addEventListener('click', () => {
        showModal('login-modal');
    });

    document.getElementById('register-btn').addEventListener('click', () => {
        showModal('register-modal');
    });

    document.getElementById('logout-btn').addEventListener('click', logout);
}

function renderPage(page) {
    const content = document.getElementById('content');
    content.innerHTML = '';

    switch(page) {
        case 'departments':
            renderDepartmentsPage(content);
            break;
        case 'courses':
            renderCoursesPage(content);
            break;
        case 'teachers':
            renderTeachersPage(content);
            break;
        case 'students':
            renderStudentsPage(content);
            break;
        case 'grades':
            renderGradesPage(content);
            break;
        default:
            renderHomePage(content);
    }
}

function renderHomePage(container = document.getElementById('content')) {
    container.innerHTML = `
        <section class="hero">
            <h1>Welcome to College Management System</h1>
            <p>Manage academic operations efficiently with our comprehensive platform</p>
        </section>
    `;

    if (state.currentUser) {
        const dashboard = createRoleDashboard(state.currentUser.role);
        container.appendChild(dashboard);
    }
}

function createRoleDashboard(role) {
    const dashboard = document.createElement('div');
    dashboard.className = 'dashboard';
    
    switch(role) {
        case 'admin':
            dashboard.innerHTML = `
                <div class="admin-stats">
                    <h2>Administrator Dashboard</h2>
                    <div class="stats-grid">
                        <div class="stat-card">
                            <h3>Departments</h3>
                            <p>${state.entities.departments.length}</p>
                        </div>
                        <div class="stat-card">
                            <h3>Students</h3>
                            <p>${state.entities.students.length}</p>
                        </div>
                        <div class="stat-card">
                            <h3>Teachers</h3>
                            <p>${state.entities.teachers.length}</p>
                        </div>
                    </div>
                </div>
            `;
            break;
        case 'teacher':
            dashboard.innerHTML = `
                <div class="teacher-view">
                    <h2>My Courses</h2>
                    <div class="courses-list">
                        ${state.entities.courses.filter(c => c.teacherId === state.currentUser.id)
                            .map(course => `
                                <div class="course-card">
                                    <h3>${course.name}</h3>
                                    <p>Students: ${course.students.length}</p>
                                </div>
                            `).join('')}
                    </div>
                </div>
            `;
            break;
        case 'student':
            dashboard.innerHTML = `
                <div class="student-view">
                    <h2>My Academic Record</h2>
                    <div class="grades-summary">
                        <h3>Current GPA: 3.75</h3>
                        <div class="grades-chart"></div>
                    </div>
                </div>
            `;
            break;
    }
    
    return dashboard;
}
