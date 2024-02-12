document.addEventListener("DOMContentLoaded", function () {
  const cardData = [
    { title: "BANANE", text: "15 DH/KG" },
    { title: "CAROTTE", text: "8 DH/KG" },
    { title: "POIRE", text: "45 DH/KG" },
    { title: "POMME DE TERRE", text: "11 DH/KG" },
    { title: "POMME", text: "32 DH/KG" },
    { title: "TOMATE", text: "5 DH/KG" },
  ];

  // Fonction pour créer une carte HTML à partir des données
  function createCardHTML(title, text) {
    return `
        <div class="card" style="width: 18rem">
          <img src="C:\Users\eptec\Desktop\MonDossier\images\${title.toLowerCase()}.jpg" class="card-img-top" alt="..." />
          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <p class="card-text">${text}</p>
            <a href="#" class="btn btn-plus"><i class="fas fa-plus plus"></i></a>
            <a href="#" class="btn btn-coeur"><i class="fas fa-heart coeur"></i></a>
          </div>
        </div>
      `;
  }

  // Fonction pour afficher un pop-up
  function showPopup(popupElement) {
    popupElement.style.display = "block";
  }

  // Fonction pour cacher un pop-up
  function hidePopup(popupElement) {
    popupElement.style.display = "none";
  }

  // Fonction pour ajouter un élément au panier et mettre à jour l'affichage
  function addToCart(title) {
    if (!cart[title]) {
      cart[title] = 1;
    } else {
      cart[title]++;
    }
    updateCartDisplay();
  }

  // Sélectionner le conteneur des cartes
  const contenuPanier = document.querySelector(".contenu_panier");

  // Générer les cartes dynamiquement à partir des données
  cardData.forEach(({ title, text }) => {
    const cardHTML = createCardHTML(title, text);
    contenuPanier.insertAdjacentHTML("beforeend", cardHTML);
  });

  // Écouteurs d'événements pour les boutons d'ajout au panier
  const plusButtons = document.querySelectorAll(".btn-plus");
  plusButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
      addToCart(cardData[index].title);
      showPopup(sidebarPopup);
    });
  });

  // Écouteur d'événement pour le bouton du panier
  const openCartBtn = document.querySelector(".btn-panier");
  openCartBtn.addEventListener("click", () => {
    showPopup(centerPopup);
    renderCenterPopupContent();
  });

  // Écouteur d'événement pour le bouton de fermeture du pop-up central
  const closeCenterPopupBtn = document.getElementById("closeCenterPopupBtn");
  closeCenterPopupBtn.addEventListener("click", () => {
    hidePopup(centerPopup);
  });

  // Votre code JavaScript dynamique va ici

  // Création de la fenêtre pop-up latérale
  const sidebarPopup = createPopup();

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
        updateCartDisplay();
      });

      const decreaseButton = document.createElement("button");
      decreaseButton.textContent = "-";
      decreaseButton.addEventListener("click", () => {
        if (cart[title] > 1) {
          cart[title]--;
        } else {
          delete cart[title];
        }
        updateCartDisplay();
      });

      cardElement.appendChild(increaseButton);
      cardElement.appendChild(decreaseButton);
      popupContent.appendChild(cardElement);
    });
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
