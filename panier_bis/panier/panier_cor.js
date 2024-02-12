document.addEventListener("DOMContentLoaded", function () {
  const cardData = [
    { title: "BANANE", text: "15 DH/KG" },
    { title: "CAROTTE", text: "8 DH/KG" },
    { title: "POIRE", text: "45 DH/KG" },
    { title: "POMME DE TERRE", text: "11 DH/KG" },
    { title: "POMME", text: "32 DH/KG" },
    { title: "TOMATE", text: "5 DH/KG" },
  ];

  // Sélectionner tous les éléments .card
  const cards = document.querySelectorAll(
    '.contenu_panier > div[class^="card"]'
  );

  // Parcourir chaque carte et affecter les valeurs de cardData
  cards.forEach((card, index) => {
    const titleElement = card.querySelector(".card-body .card-title");
    const textElement = card.querySelector(".card-body .card-text");
    titleElement.textContent = cardData[index].title;
    textElement.textContent = cardData[index].text;
  });

  const cart = {};

  const plusButtons = document.querySelectorAll(".btn-plus");

  plusButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
      const title = cardData[index].title;
      if (!cart[title]) {
        cart[title] = 1;
        button.disabled = true; // Désactive le bouton après la sélection
        button.parentElement.style.filter = "blur(5px)"; // Rend l'élément flou
        button.style.cursor = "unset"; // Rend l'élément flou

        updateCartDisplay();
      }
    });
  });

  function updateCartDisplay() {
    const rectangle = document.querySelector(".rectangle");
    rectangle.innerHTML = Object.entries(cart)
      .map(([title, quantity]) => `<div>${quantity} ${title}</div>`)
      .join("");
  }

  // Fonction pour créer la fenêtre pop-up
  function createPopup() {
    const popup = document.createElement("div");
    popup.classList.add("popup");
    popup.style.display = "none";
    popup.style.position = "fixed";
    popup.style.top = "0";
    popup.style.right = "0";
    popup.style.width = "25%";
    popup.style.height = "100%";
    popup.style.backgroundColor = "lightblue";
    popup.style.boxShadow = "-4px 0 5px rgba(0, 0, 0, 0.1)";
    popup.style.zIndex = "1";
    popup.style.overflowX = "hidden";
    popup.style.transition = "0.3s";

    document.body.appendChild(popup);
    return popup;
  }

  // Création de la fenêtre pop-up latérale
  const sidebarPopup = createPopup();

  // Écouteur d'événement pour l'ouverture de la fenêtre pop-up latérale
  const openBtn = document.querySelector(".btn-panier");
  openBtn.addEventListener("click", () => {
    sidebarPopup.style.display = "block";
    renderSidebarPopupContent();
  });

  // Fonction pour rendre le contenu de la fenêtre pop-up latérale
  function renderSidebarPopupContent() {
    const popupContent = document.createElement("div");
    popupContent.classList.add("popup-content");
    sidebarPopup.innerHTML = ""; // Efface le contenu précédent
    sidebarPopup.appendChild(popupContent);

    Object.entries(cart).forEach(([title, quantity]) => {
      const cardElement = document.createElement("div");
      cardElement.classList.add("card");
      cardElement.textContent = `${quantity} ${title}`;

      // Boutons pour augmenter et diminuer la quantité
      const increaseButton = document.createElement("button");
      increaseButton.textContent = "+";
      increaseButton.addEventListener("click", () => {
        cart[title]++;
        renderSidebarPopupContent();
      });

      const decreaseButton = document.createElement("button");
      decreaseButton.textContent = "-";
      decreaseButton.addEventListener("click", () => {
        if (cart[title] > 1) {
          cart[title]--;
        } else {
          delete cart[title];
        }
        renderSidebarPopupContent();
      });

      cardElement.appendChild(increaseButton);
      cardElement.appendChild(decreaseButton);
      popupContent.appendChild(cardElement);
    });

    // Ajout du bouton pour afficher la fenêtre pop-up au centre de l'écran
    const centerPopupButton = document.createElement("button");
    centerPopupButton.textContent = "Vérifiez et Validez votre commande";
    centerPopupButton.addEventListener("click", () => {
      renderCenterPopupContent();
      centerPopup.style.display = "block";
    });
    popupContent.appendChild(centerPopupButton);
  }

  // Création de la fenêtre pop-up au centre de l'écran
  const centerPopup = createPopup();
  centerPopup.style.width = "50%";
  centerPopup.style.height = "50%";
  centerPopup.style.backgroundColor = "paleturquoise";
  centerPopup.style.top = "25%";
  centerPopup.style.left = "25%";

  // Fonction pour rendre le contenu de la fenêtre pop-up au centre de l'écran
  function renderCenterPopupContent() {
    const popupContent = document.createElement("div");
    popupContent.classList.add("popup-content");
    centerPopup.innerHTML = ""; // Efface le contenu précédent
    centerPopup.appendChild(popupContent);

    Object.entries(cart).forEach(([title, quantity]) => {
      const cardElement = document.createElement("div");
      cardElement.textContent = `${quantity} ${title}`;
      popupContent.appendChild(cardElement);
    });
  }
});
