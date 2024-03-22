
// Start when the document is ready
if (document.readyState == "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
  
// Fonction pour ajouter une nouvelle tâche
function ajout_tache() {
    var input = document.getElementById('fenetre_dialogue'); // Obtenir l'élément d'entrée
    var newTaskText = input.value; // Obtenir la valeur de l'élément d'entrée
    if (newTaskText !== '') { // Vérifier si l'entrée n'est pas vide
        // Créer les éléments de la nouvelle tâche
        var abc = document.createElement('div');
        div.className = 'tache-container';
        
       var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
     /*   checkbox.addEventListener('change', function() { // Ajouter une fonction pour barrer la tâche lorsque cochée
            if (this.checked) {
                taskContent.style.textDecoration = 'line-through';
            } else {
                taskContent.style.textDecoration = 'none';
            }
        });
        */
        var taskContent = document.createElement('span');
        taskContent.textContent = newTaskText;

        // Bouton pour supprimer la tâche
        var deleteButton = document.createElement('button');
        deleteButton.textContent = 'Supprimer';
        deleteButton.className = 'btn btn-danger btn-sm';
        deleteButton.onclick = function() { // Ajouter une fonction pour supprimer la tâche
            div.remove();
        };

        // Assembler les éléments de la tâche
        div.appendChild(checkbox);
        div.appendChild(taskContent);
        div.appendChild(deleteButton);

        // Ajouter la nouvelle tâche à la liste des tâches
        var tasksContainer = document.querySelector('.tasks');
        tasksContainer.appendChild(div);

        // Réinitialiser la valeur de l'entrée
        input.value = '';
    }
}

// Ajouter l'écouteur d'événement pour le bouton d'ajout
document.querySelector('button').addEventListener('click', ajout_tache);

// Permettre l'ajout de tâche avec la touche Entrée
document.getElementById('fenetre_dialogue').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        ajout_tache();
    }
});
