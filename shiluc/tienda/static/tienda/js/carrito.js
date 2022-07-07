var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action: ', action)
        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('Usuario no autenticado')


        } else {
            updateOrdenCliente(productId, action)
        }


    })

}

function updateOrdenCliente(productId, action) {


    var url = '/update_item/'
    console.log('URL', url)

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'productId': productId, 'action': action })


        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('data:', data)
        })
}