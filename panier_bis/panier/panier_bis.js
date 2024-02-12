document.addEventListener("DOMContentLoaded", function () {
  // Tableau d'objets avec les valeurs pour card-text et card-title
  const cardData = [
    {
      title: "BANANE",
      text: "15 DH/KG",
    },
    {
      title: "CAROTTE",
      text: "8 DH/KG",
    },
    {
      title: "POIRE",
      text: "45 DH/KG",
    },
    {
      title: "POMME DE TERRE",
      text: "11 DH/KG",
    },
    {
      title: "POMME",
      text: "32 DH/KG",
    },
    {
      title: "TOMATE",
      text: "5 DH/KG",
    },
  ];

  // Créer un nouveau tableau d'objets où la partie 'text' ne comprendra que la partie numérique
  const newData = cardData.map((item) => {
    const numericPart = item.text.match(/\d+/); // Recherche des nombres dans la chaîne 'text'
    const numericValue = numericPart ? parseInt(numericPart[0]) : null; // Convertir en nombre entier
    return { title: item.title, text: numericValue }; // Retourne un nouvel objet avec le titre et la partie numérique de 'text'
  });

  // Sélectionner tous les éléments avec les classes card-text et card-title
  const cardTextElements = document.querySelectorAll(".card-text");
  const cardTitleElements = document.querySelectorAll(".card-title");

  // Mettre à jour le texte dans les éléments card-text et card-title
  cardTextElements.forEach((element, index) => {
    element.textContent = newData[index].text;
  });

  cardTitleElements.forEach((element, index) => {
    element.textContent = newData[index].title;
  });




    const cart = {}; // Objet pour stocker les articles dans le panier

    // Sélectionner l'élément "rectangle" où la liste des objets sélectionnés sera affichée
    const rectangle = document.querySelector('.rectangle');

    // Fonction pour mettre à jour l'affichage des objets sélectionnés dans le rectangle
    function updateCartDisplay() {
        // Générer la liste des objets sélectionnés
        const cartItems = Object.entries(cart).map(([title, quantity]) => {
            return `${quantity} ${title}`;
        });

        // Mettre à jour le contenu de l'élément "rectangle" avec la liste en colonne
        rectangle.innerHTML = cartItems.map(item => `<div>${item}</div>`).join('');
    }

    const plusButtons = document.querySelectorAll('.btn-plus, .btn-plusbis');
    const minusButtons = document.querySelectorAll('.btn-minus');

    plusButtons.forEach((button, index) => {
        button.addEventListener('click', () => {
            const title = cardData[index].title;
            if (cart[title]) {
                cart[title]++;
            } else {
                cart[title] = 1;
            }
            updateCartDisplay(); // Mettre à jour l'affichage des objets sélectionnés
            console.log(cart);
        });
    });

   

    // Gestionnaire d'événement pour le bouton de panier
    const cartButton = document.querySelector('.btn-panier');
    cartButton.addEventListener('click', () => {
        // Générer la liste de la commande et le total des prix
        const orderList = Object.entries(cart).map(([title, quantity]) => {
            const item = cardData.find(item => item.title === title);
            const total = quantity * parseInt(item.text.match(/\d+/)[0]);
            return `${quantity} ${title}: ${total} DH`;
        });
        const totalPrice = Object.entries(cart).reduce((acc, [title, quantity]) => {
            const item = cardData.find(item => item.title === title);
            const price = parseInt(item.text.match(/\d+/)[0]);
            return acc + (quantity * price);
        }, 0);
        
        // Afficher une fenêtre avec la liste de la commande et le total des prix
        alert(`CONTENU DE VOTRE PANIER :\n\n${orderList.join('\n')}\n\nTotal : ${totalPrice} DH`);
    });




});
