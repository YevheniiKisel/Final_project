// Java script
//////////////////////////////////////////////////////////////////////////
// Make pages on /subscription change by clicking on button
// Detect every step and button inside POST form
const steps = Array.from(document.querySelectorAll('form .step'));
const nextButton = document.querySelectorAll('form .btn-next');
const previousButton = document.querySelectorAll('form .btn-previous');
const form = document.querySelector('form');
const checkoutButton = document.querySelector('form .btn-next.btn-checkOut')

// Function that change step to the next one
nextButton.forEach(button=>{
    button.addEventListener('click', (e) => {
        changeStep('next');
    })
})

// Function that change step to the previous one
previousButton.forEach(button=>{
    button.addEventListener('click', (e)=>{
        changeStep('previous');
    })
})

// Function helper. Read what atribute was passed and switch steps
function changeStep(btn){
    let index = 0;
    const active = document.querySelector('form .step.active');
    index = steps.indexOf(active);
    // If button next was clicked, and step was filled: transition to the next step
    if (btn === 'next' && validateStep(active)){
        steps[index].classList.remove('active');
        index ++;
        steps[index].classList.add('active');
    }
    else if(btn === 'previous'){
        steps[index].classList.remove('active');
        index --;
        steps[index].classList.add('active');
    }
     else{
        alert('Please submit all inputs')
        return false;
     }
}

//Function helper. Check if all inputs were fulfielld 
function validateStep(active) {
    // This function deals with validation of the form fields
    var inputs, i, j, valid = true;
    inputs = active.getElementsByTagName("input");
    // A loop that checks every input field in the current step:
    for (i = 0; i < inputs.length; i++) {
      // If a field is empty...
      if (inputs[i].value == "") {
        // and set the current valid status to false:
        return valid = false;
      }
    }
    // A loop that checks every radio input in the current step:
    // Get all <div> with radio buttons 
    let divRadioInputs = Array.from(active.querySelectorAll('form .radioButton'));
    // A loop, that checks every div, if there is just one radiobutton checked
    for (i = 0; i < divRadioInputs.length; i++) {
        let section = Array.from(divRadioInputs[i].getElementsByTagName('input'))
        for (j = 0; j < section.length; j++){
            if (section[j].checked){
                break;
            }
        }
        if (j == section.length){
            return valid = false
        }
    }
    return valid; // return the valid status
}
/////////////////////////////////////////////////////////////////////////////////////////// 












// jQuery

// Re-configure a calendar
$( '#deliveryDate' ).flatpickr({
    altInput: true,
    altFormat: 'F j, Y',
    dateFormat: 'Y-m-d',
    minDate: 'today',
    maxDate: new Date().fp_incr(27),
    inline: false,
    "enable": [
        function(date) {
           return (date.getDay() === 2 || date.getDay() === 4);  // disable Thuesday and Thursday
        }
    ],
    "locale": {
        "firstDayOfWeek": 1 // set start day of week to Monday
    }
  });

//Update checkout
checkoutButton.addEventListener('click', function() {
    // Place value into placeholders
    let frequency = $('input:checked[name="perWeek"]').val() ;
    $('#frequency').text(frequency);
    let period = $('input:checked[name="durationMonth"]').val();
    $('#period').text(period);
    let date = $('#deliveryDate').val();
    $('#date').text(date);
    let time = $('#deliveryTime').val();
    $('#time').text(time);
    let starterPack = $('input:checked[name="starterPack"]').val();
    $('#starterPack').text(starterPack);
    //Calculate total
    let total = 0;
    //Add base prise
    if (frequency == 1) {
        total += 150;
    }
    else if (frequency == 2) {
        total +=280;
    }
    // Add extras
    if (starterPack == 'yes') {
        total += 150;
    }
    $('#total').text(total);
})



