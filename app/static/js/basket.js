function changePrice(itemId, minusButton, plusOrMinus) {
    let subtotal = document.getElementById(`subtotal-${itemId}`);
    let price = document.getElementById(`price-${itemId}`).innerHTML;
    let quantity = document.getElementById(`quantity-${itemId}`).value;
    if (plusOrMinus === 'plus') {
        quantity = parseInt(quantity) + 1
    } else {
        quantity -= 1
    }
    if ((parseInt(quantity)) === 1 && plusOrMinus === 'minus') {
        minusButton.disabled = true;
    } else if (parseInt(quantity) > 1 && plusOrMinus === 'plus') {
        $(`#minusButton-${itemId}`).removeAttr('disabled');
    }
    subtotal.innerHTML = parseFloat((parseFloat(price) * parseFloat(quantity)).toFixed(2));
    calcTotal();
}


function calcTotal() {
    let subtotalValues = document.getElementsByName('subtotal');
    let subtotalFinal = document.getElementById('subtotal-final');
    let total = document.getElementById('total');
    let shipping = document.getElementById('shipping');
    let subtotal_result = 0;
    for (subtotalValue of subtotalValues) {
        subtotal_result += parseFloat(subtotalValue.innerHTML)
    }
    console.log('subtotal_result', subtotal_result)
    subtotalFinal.innerHTML = subtotal_result
    shipping.innerHTML = subtotal_result * 5 / 100
    total.innerHTML = subtotal_result + (subtotal_result * 5 / 100)
}

function deleteItem(itemId) {
    document.getElementById(`tr-${itemId}`).remove()
}

window.addEventListener("load", calcTotal);