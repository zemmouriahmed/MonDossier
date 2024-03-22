// Attend que le document HTML soit entièrement chargé avant d'exécuter le script
document.addEventListener('DOMContentLoaded', () => {
  // Sélectionne l'élément de l'écran de la calculatrice pour afficher les entrées et les résultats
  const display = document.getElementById('visible');
  // Initialise une variable pour stocker l'opération en cours sous forme de chaîne de caractères
  let currentOperation = '';
  // Initialise un booléen pour suivre si le résultat de l'opération précédente est actuellement affiché
  let resultDisplayed = false;

  // Définit une fonction pour gérer les appuis sur les boutons de la calculatrice
  function appuyerBouton(value) {
      // Vérifie si un résultat est affiché et si l'entrée actuelle n'est ni 'del', 'reset', ni '='
      if (resultDisplayed && value !== 'del' && value !== 'reset' && value !== '=') {
          // Si vrai, réinitialise l'écran et la variable d'opération pour une nouvelle entrée
          currentOperation = '';
          display.value = '';
          resultDisplayed = false;
      }

      // Gère les cas spécifiques selon la valeur du bouton appuyé
      if (value === 'reset') {
          // Réinitialise l'affichage et l'opération en cours
          display.value = '';
          currentOperation = '';
      } else if (value === 'del') {
          // Supprime le dernier caractère de l'affichage et de l'opération en cours
          display.value = display.value.slice(0, -1);
          currentOperation = currentOperation.slice(0, -1);
      } else if (value === '=') {
          // Tente d'exécuter l'opération en cours lorsqu'on appuie sur '='
          try {
              // Remplace 'x' par '*' pour permettre les calculs de multiplication
              currentOperation = currentOperation.replace(/x/g, '*');
              // Évalue l'expression mathématique et affiche le résultat
              display.value = eval(currentOperation);
              // Stocke le résultat comme nouvelle opération en cours
              currentOperation = display.value;
              // Indique qu'un résultat est désormais affiché
              resultDisplayed = true;
          } catch (e) {
              // Affiche 'Erreur' en cas d'expression invalide
              display.value = 'Erreur';
          }
      } else {
          // Pour tout autre bouton (nombres, opérateurs), ajoute la valeur au display et à l'opération
          display.value += value;
          currentOperation += value;
      }
  }

  // Ajoute un écouteur d'événements pour capturer les clics sur les boutons de la calculatrice
  document.querySelector('.calculatrice').addEventListener('click', (e) => {
      // Vérifie si l'élément cliqué est un bouton
      if (e.target.matches('button')) {
          // Récupère le texte du bouton et appelle la fonction `appuyerBouton` avec cette valeur
          const value = e.target.innerText;
          appuyerBouton(value);
      }
  });
});



/*
try {
  // Code à essayer, qui peut potentiellement générer une erreur
} catch (erreur) {
  // Code à exécuter si une erreur survient dans le bloc try
}
*/

/*

try {
  // Code à essayer
} catch (erreur) {
  // Code à exécuter en cas d'erreur
} finally {
  // Code qui s'exécute après les blocs try et catch, qu'une erreur ait été capturée ou non
}
*/
