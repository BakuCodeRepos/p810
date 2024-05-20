function manageOrderButton() {
    let cardNumber = document.getElementById('card-number');
    let cardHolder = document.getElementById('card-holder');
    let expireDate = document.getElementById('expire-date');
    let cvv = document.getElementById('cvv');
    let orderButton = document.getElementById('order-button');

    if (
        cardNumber.value &&
        cardHolder.value &&
        expireDate.value &&
        cvv.value
    ) {
        orderButton.disabled = false;
    } else {
        orderButton.disabled = true;
    }
}

function checkValidCardNumber() {
    cardNumber = document.getElementById('card-number');
    cardNumberError = document.getElementById('card-number-error');
  
    if (cardNumber.value.length !== 16) {
      cardNumberError.classList.remove('d-none');
    } else {
      cardNumberError.classList.add('d-none');
    }
    if (cardNumber.value.length > 16) {
      cardNumber.value = cardNumber.value.slice(0, 16);
      checkValidCardNumber();
    }
  }
  
  
  function checkValidCvv() {
    cvv = document.getElementById('cvv');
    cvvError = document.getElementById('cvv-error');
  
    if (cvv.value.length !== 3) {
      cvvError.classList.remove('d-none');
    } else {
      cvvError.classList.add('d-none');
    }
    if (cvv.value.length > 3) {
      cvv.value = cvv.value.slice(0, 3);
      checkValidCvv();
    }
  }

function setExpireDate() {
    let expireDate = document.getElementById('expire-date');

    if (expireDate.value.length === 3) {
        expireDate.value = expireDate.value.slice(0, 2)
    } else if (expireDate.value.length === 2) {
        expireDate.value = `${expireDate.value.slice(0, 2)}/${expireDate.value.slice(2, 3)}`
    }
}

function isDoneOrder() {
    $.ajax({
      method: "PUT",
      url: is_done_url,
      headers: { "X-CSRFToken": csrftoken_ },
      data: {
        is_done: true,
      },
      dataType: "json",
      success: function () {
        window.location.href = home_url;
      },
      error: function(data) {
        console.log('error cixdiiiii', data);
      }
    });
  }