function testLength(value, length){
    return value.value.length == length;
}
function testNumber(value){
    return !(isNaN(value));
}
function validateControl(control, name){
    //console.log(testNumber(control.value), name);
    return testNumber(control.value);
}
function validateCreditCard(value){
    console.log(value[0] == 3);
    value = value.replace(/\s/g, '');
    if(testNumber(value)){
        if(value[0] == 3){
            if(testLength(value, 15)){
                console.log("works");
                return true;
            }else{
                console.log("Invalid Credit Card Length.");
                return false;
            }
        }else if(value[0] == 6 || value[0] == 5 || value[0] == 4){
            if(testLength(value, 16)){
                console.log("works");
                return true;
            }else{
                console.log("Invalid Credit Card Length.");
                return false;
            }
        }else{
            console.log("Invalid Credid Card Number.");
            return false;
        }
    }
}
function validateDate(value){
    var today = new Date();
    var selected = new Date(value);
    if(selected.getMonth() >= today.getMonth() && selected.getFullYear() >= today.getFullYear()){
        return true;
    }else{
        console.log("Invalid Date.");
        return false;
    }
}
function validateEmail(value){
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if(value.toLowerCase().match(emailRegex)){
        return true;
    }else{
        console.log("Invalid Email.");
        return false;
    }
}
function validateCarType(control){
    var isChecked = false;
    for (var i = 0; i < control.length; i++) {
        if (control[i].checked) {
            isChecked = true;
            break;
        }
    }
    if(!isCheckedhecked){
        console.error("Please select a car type.");
        return false;
   }else{
    return true;
   }
}
function validateState(value){
   if(value == 0){
    return true;
   }else{
    return false;
   }
}
function validateDateTime (value){
   var given = new Date(value);
   var current = new Date();
   if(given <= current){
    console.error("Time must be in the Future.");
    return false;
   }else{
    return true;
   }
}
function validateDropOffTime(pickUpTime, dropOffTime){
   var pickup = new Date(pickUpTime);
   var dropoff = new Date(dropOffTime);

   if(dropoff <= pickup){
    console.error("Dropoff datetime must be after pickup datetime.");
    return false;
   }else{
    return true;
   }
}
function validateForm(){
    var cvcVal = document.getElementById("cvc");
    var fnameVal = document.getElementById("fname");
    var lnameVal = document.getElementById("lname");
    var cardName = document.getElementById("nameCard");

    var cardNum = document.getElementById("cardNo");
    var expiryDate = document.getElementById("expiry");
    var emailVal = document.getElementById("email");

    var radioButtons = document.getElementsByName("carType");

    var dropLocation = document.getElementById("dropOff");
    var pickLocation = document.getElementById("pickup");
    var pickTime = document.getElementById("pickupTime");
    var dropTime = document.getElementById("dropoffTime");

    
    if(validateCreditCard(cardNum.value) && validateDate(expiryDate.value) && testLength(cvcVal, 3) && validateControl(cvcVal, "CVC") && !validateControl(fnameVal, "First Name") && !validateControl(lnameVal, "Last Name") && !validateControl(cardName, "Name on Card") && validateEmail(emailVal.value) && validateState(pickLocation.selectedIndex) && validateState(dropLocation.selectedIndex) && validateDateTime(pickTime.value) && validateDropOffTime(pickTime.value, dropTime.value) && validateCarType(radioButtons)){
        console.log("Payment Submitted!");
        return false;
    }else{
        console.log("fail");
        return false;
    }
}