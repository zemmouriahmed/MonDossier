// Attend que le DOM soit entièrement chargé avant de lancer le script
document.addEventListener('DOMContentLoaded', () => {
    // Sélectionne l'élément qui affichera les entrées et résultats (écran de la calculatrice)
    const display = document.getElementById('display');
    // Variable de contrôle pour savoir si on attend une nouvelle valeur après une opération
    let awaitingNextValue = false;

    // Écoute les clics sur l'ensemble des boutons de la calculatrice
    document.querySelector('.buttons').addEventListener('click', e => {
        // Vérifie si l'élément cliqué est un bouton
        if (e.target.matches('button')) {
            const button = e.target;
            // Récupère la classe indiquant le type d'action du bouton ('number', 'operation', etc.)
            const action = button.classList[1];

            switch (action) {
                case 'number':
                    // Si on attend une nouvelle valeur, remplace l'affichage par le nombre cliqué
                    // Sinon, ajoute le nombre à l'affichage actuel
                    if (awaitingNextValue) {
                        display.value = button.textContent;
                        awaitingNextValue = false;
                    } else {
                        display.value += button.textContent;
                    }
                    break;
                case 'operation':
                    // Ajoute l'opérateur à l'affichage avec des espaces pour séparer les nombres
                    display.value += ' ' + button.textContent + ' ';
                    break;
                case 'decimal':
                    // Ajoute un point décimal s'il n'y en a pas déjà un dans l'affichage actuel
                    if (!display.value.includes('.')) {
                        display.value += '.';
                    }
                    break;
                case 'delete':
                    // Supprime le dernier caractère de l'affichage
                    display.value = display.value.slice(0, -1);
                    break;
                case 'reset':
                    // Réinitialise l'affichage
                    display.value = '';
                    break;
                case 'equals':
                    // Tente de calculer l'expression dans l'affichage. Affiche 'Error' en cas d'exception
                    try {
                        display.value = eval(display.value);
                    } catch {
                        display.value = 'Error';
                    }
                    break;
            }
        }
    });

    // Écoute les frappes au clavier pour gérer les entrées sans clic
    document.addEventListener('keydown', e => {
        // Permet d'entrer des nombres et le point décimal via le clavier
        if ((e.key >= 0 && e.key <= 9) || e.key === '.') {
            if (awaitingNextValue) {
                display.value = e.key;
                awaitingNextValue = false;
            } else {
                display.value += e.key;
            }
        } else if (e.key === 'Backspace') {
            // Supprime le dernier caractère en appuyant sur Backspace
            display.value = display.value.slice(0, -1);
        } else if (e.key === 'Enter' || e.key === '=') {
            // Calcule le résultat en appuyant sur Entrée ou égal
            e.preventDefault(); // Empêche le comportement par défaut (soumission de formulaire)
            try {
                display.value = eval(display.value);
            } catch {
                display.value = 'Error';
            }
        } else if (['+', '-', '*', '/'].includes(e.key)) {
            // Permet d'entrer des opérateurs via le clavier
            display.value += ' ' + e.key + ' ';
        } else if (e.key === 'Escape') {
            // Réinitialise l'affichage en appuyant sur Échap
            display.value = '';
        }
    });
});
