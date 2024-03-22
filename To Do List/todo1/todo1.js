document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').addEventListener('click', ajout_tache);
    document.getElementById('fenetre_dialogue').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            ajout_tache();
        }
    });
});

function ajout_tache() {
    var input = document.getElementById('fenetre_dialogue');
    var newTaskText = input.value.trim();
    if (newTaskText) {
        var div = document.createElement('div');
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.addEventListener('change', function() {
            div.style.textDecoration = this.checked ? 'line-through' : 'none';
        });

        var taskContent = document.createElement('span');
        taskContent.textContent = newTaskText;

        var editButton = document.createElement('button');
        editButton.textContent = 'Éditer';
        
        var deleteButton = document.createElement('button');
        deleteButton.textContent = 'Supprimer';
        deleteButton.onclick = function() {
            div.remove();
        };

        div.appendChild(checkbox);
        div.appendChild(taskContent);
        div.appendChild(editButton);
        div.appendChild(deleteButton);
        
        var editMenu = createEditMenu(div);
        div.appendChild(editMenu);
        
        document.querySelector('.tasks').appendChild(div);

        input.value = ''; // Clear input field after adding
    }
}

function createEditMenu(taskDiv) {
    var editMenu = document.createElement('div');
    editMenu.className = 'edit-menu';
    editMenu.style.display = 'none'; // Initially hidden

    // Date
    var datePicker = document.createElement('input');
    datePicker.type = 'date';
    editMenu.appendChild(createOption('Date', datePicker));

    // Time
    var timePicker = document.createElement('input');
    timePicker.type = 'time';
    editMenu.appendChild(createOption('Heure', timePicker));

    // Location
    var locationInput = document.createElement('input');
    locationInput.type = 'text';
    locationInput.placeholder = 'Saisir une adresse';
    editMenu.appendChild(createOption('Endroit', locationInput));

    // Reminder
    var reminderCheckbox = document.createElement('input');
    reminderCheckbox.type = 'checkbox';
    var reminderLabel = document.createElement('label');
    reminderLabel.textContent = 'Rappel 24h avant';
    editMenu.appendChild(createOption('Rappel', reminderCheckbox, reminderLabel));

    // Toggle edit menu visibility
    taskDiv.querySelector('button').onclick = function() {
        editMenu.style.display = editMenu.style.display === 'none' ? 'block' : 'none';
    };

    return editMenu;
}

function createOption(text, input, label = null) {
    var container = document.createElement('div');
    var textNode = document.createTextNode(text + ': ');
    container.appendChild(textNode);
    container.appendChild(input);
    if (label) {
        container.appendChild(label);
    }
    return container;
}
