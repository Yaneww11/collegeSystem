// Complete UI rendering functions
const UI = {
    renderDepartmentCard: function(dept) {
        const card = document.createElement('div');
        card.className = 'card department-card';
        card.innerHTML = `
            <h3>${dept.name}</h3>
            <p>Faculty: ${dept.faculty}</p>
            <p>Head: ${dept.head || 'Not assigned'}</p>
            <div class="card-actions">
                <button class="btn edit-btn">Edit</button>
                <button class="btn delete-btn">Delete</button>
            </div>
        `;
        return card;
    },

    renderCourseCard: function(course) {
        // Similar structure for course cards
    },

    showFormModal: function(formHTML) {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                ${formHTML}
            </div>
        `;
        document.body.appendChild(modal);
    },

    // Other rendering methods...
};

window.UI = UI;

function toggleNav() {
  var nav = document.getElementById("topNav");
  nav.classList.toggle("responsive");
}
