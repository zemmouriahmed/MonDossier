document.getElementById('add-task-btn').addEventListener('click', function() {
    var input = document.getElementById('todo-input');
    var newTask = input.value.trim();
    
    if (newTask) {
        var li = document.createElement('li');
        var taskText = document.createElement('span');
        taskText.textContent = newTask;
        li.appendChild(taskText);

        // Crée un conteneur pour les boutons
        var buttonsContainer = document.createElement('div');

        var deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.className = 'delete-btn';
        deleteBtn.addEventListener('click', function() {
            li.remove();
        });
        buttonsContainer.appendChild(deleteBtn);

        var editBtn = document.createElement('button');
        editBtn.textContent = 'Edit';
        editBtn.className = 'edit-btn';
        editBtn.addEventListener('click', function() {
            alert('Edit functionality to be implemented.');
        });
        buttonsContainer.appendChild(editBtn);

        // Ajoute le conteneur de boutons au li
        li.appendChild(buttonsContainer);

        document.getElementById('todo-list').appendChild(li);

        input.value = '';
    } else {
        alert('Please enter a task');
    }
});
