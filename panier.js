// Définition du panier initial

let cart = [
    {id: 1, name:'Nom de 1\'article 1', quantity: 1, price: 10.00, liked:false},
    // Ajouter d'autres articles de la même manière
];


// Fonction pour mettre à jour l'affichage du panier
function updateCart() {
    const cartElement = document.getElementById('cart');
    const totalAmountElement = document.getElementById('totalAmount');
    let totalAmount = 0;

    //Nettoie le contenu du panier avant de le réafficher
    cartElement.innerHTML = '';

    //Parcourt tous les articles dans le panier
    cart.forEach(item =>{
        //Crée un élément pour chaque article
        const itemElement = document.createElement('div');
        itemElement.classList.add('col-md-4','mb-3','card');
        itemElement.setAttribute('data-item-id',item.id);

        //Ajoute la classe 'added-to-cart' si l'article vient d'être ajouté
        if(item.addedToCart) {
            itemElement.classList.add('added-to-cart');
            //Réinitialise la propriété addedToCart
            item.addedToCart = false;
        }

        //Remplit l'élément avec les informations de l'article
        itemElement.innerHTML =`
            <div class = "card-body">
                <h5 class="card-title">${item.name}</h5>
                <button class="btn btn-outline-primary" onclick="adjustQuantity(${item.id},'increase')">+</button>
                <span class="quantity">${item.quantity}<\span>
                <button class="btn btn-outline-primary" onclick="adjustQuantity(${item.id},'decrease')">-</button>
                <button class="btn btn-outline-danger" onclick="removeItem({item.id})">Supprimer</button>
                <button class="btn btn-outline-dark" onclick="toggleLike(${item.id})">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                        <path d="M8 14s-1-1.5-3-1.5S2 14 2 11s3-6 4-7 1-2 2-2 3 1 4 2 2.5 3.5 2.5 6-1 7-3-3 9-8 9z"/>
                    </svg>
                </button>
            </div>

        `;

        //Ajoute l'élément à la section du panier
        cartElement.appendChild(itemElement);

        //Calcule le coût total de chaque article
        totalAmount += item.quantity * item.price;
        

    });

    //Met à jour le coût total affiché
    totalAmountElement.textContent = totalAmount.toFixed(2);
}



//Fonction pour ajuster la quantité d'un article
function adjustQuantity(itemId,action) {
    const item = cart.find(item => item.id === itemId);


    //Incrémente ou décrémente la quantité en fonction de l'action
    if(action === 'increase') {
        item.quantity++;
    } else if (action==='decrease' && item.quantity > 1) {
        item.quantity--;
    }


    //Ajoute la propriété addedToCart pour déclencher l'effet visuel d'ajout au panier
    item.addedToCart = true;

    //Met à jour l'affichage du panier
    updateCart();
}


//Fonction pour supprimer un articledu panier
function removeItem(itemElement) {
    //Filtrer les articles pour ne conserver que ceux qui ne correspondent pas à l'ID spécifié
    cart = cart.filter(item => item.id !== itemId);

    //Met à jour l'affichage du panier
    updateCart();
}


//Fonction pour activer/désactiver l'option "j'aime" d'un article
function toggleLike(itemId) {
    const item = cart.find(item => item.id === itemId);
    item.liked = !item.liked;


    //Met à jour l'affichage du panier
    updateCart();
}


//Initialiser le panier au chargement de la page
document.addEventListener("DOMContentLoaded", function(){
updateCart();
});