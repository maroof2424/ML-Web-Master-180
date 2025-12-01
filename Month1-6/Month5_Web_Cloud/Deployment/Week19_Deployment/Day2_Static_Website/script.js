
// Theme toggle
const themeToggle = document.getElementById('themeToggle');
const root = document.documentElement;
const saved = localStorage.getItem('mini_theme');
if (saved === 'dark') document.documentElement.setAttribute('data-theme', 'dark');
themeToggle.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    if (cur === 'dark') {
        document.documentElement.removeAttribute('data-theme');
        localStorage.setItem('mini_theme', 'light');
        themeToggle.textContent = '🌙'
    } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('mini_theme', 'dark');
        themeToggle.textContent = '☀️'
    }
});

// Simple todo logic
const todoText = document.getElementById('todoText');
const addTodo = document.getElementById('addTodo');
const todoList = document.getElementById('todoList');

function renderTodos() {
    const todos = JSON.parse(localStorage.getItem('mini_todos') || '[]');
    todoList.innerHTML = '';
    todos.forEach((t, i) => {
        const li = document.createElement('li');
        const span = document.createElement('span'); span.textContent = t;
        const del = document.createElement('button'); del.textContent = 'Delete'; del.style.fontSize = '12px';
        del.addEventListener('click', () => { removeTodo(i) });
        li.appendChild(span); li.appendChild(del);
        todoList.appendChild(li);
    });
}
function addNewTodo() {
    const v = todoText.value.trim();
    if (!v) return alert('Please type a task');
    const todos = JSON.parse(localStorage.getItem('mini_todos') || '[]');
    todos.unshift(v);
    localStorage.setItem('mini_todos', JSON.stringify(todos));
    todoText.value = ''; renderTodos();
}
function removeTodo(index) {
    const todos = JSON.parse(localStorage.getItem('mini_todos') || '[]');
    todos.splice(index, 1);
    localStorage.setItem('mini_todos', JSON.stringify(todos));
    renderTodos();
}
addTodo.addEventListener('click', addNewTodo);
todoText.addEventListener('keydown', (e) => { if (e.key === 'Enter') addNewTodo(); });
renderTodos();

// Contact form validation (no server) — just frontend check
const contactForm = document.getElementById('contactForm');
const formResult = document.getElementById('formResult');
contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();
    // simple validations
    if (name.length < 2) { formResult.textContent = 'Name should be at least 2 characters.'; return; }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { formResult.textContent = 'Enter a valid email.'; return; }
    if (message.length < 5) { formResult.textContent = 'Message too short.'; return; }
    formResult.textContent = '✅ Form looks good — (this demo doesn\'t send to server)';
    contactForm.reset();
});
document.getElementById('clearForm').addEventListener('click', () => { contactForm.reset(); formResult.textContent = ''; });
