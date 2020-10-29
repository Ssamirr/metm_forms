// .......................for validation..............................
var validations = {
    email: [/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/, 'Please enter a valid email address'],
    integer: [/^([1-9]|[-1-9]\d+)$/, 'Please enter integer'],
};

document.querySelectorAll('.validation-email').forEach(function (element) {
    document.querySelector('#send').addEventListener('click', function () {
        let validation_email_input = element.querySelector('.input-form')
        for_email_validation(validation_email_input)
    });
})

document.querySelectorAll('.validation-integer').forEach(function (element) {
    document.querySelector('#send').addEventListener('click', function () {
        let validation_integer_input = element.querySelector('.input-form')
        for_integer_validation(validation_integer_input)
    });
})

document.querySelectorAll('.field-requirement').forEach(function (element) {
    document.querySelector('#send').addEventListener('click', function () {
        let input_requirement = element.querySelector('.input-form')
        for_requirement_input(input_requirement)
    })
})

// document.querySelectorAll('.select-options').forEach(function(element){
//     document.querySelector('#send').addEventListener('click',function(element))
// })



function for_email_validation(email) {
    let check_validation_email = new RegExp(validations['email'][0]);
    if (!check_validation_email.test(email.value)) {
        let first_span_tag = email.closest('span')
        let second_span_tag = first_span_tag.closest('span')
        if (second_span_tag.classList.contains('field-requirement')) {
            email.setCustomValidity(validations['email'][1]);
            return false;
        }
        else {
            if (email.value) {
                email.setCustomValidity(validations['email'][1]);
                return false;
            }
            else {
                email.setCustomValidity('');
            }
        }
    } else {
        email.setCustomValidity('');
    }
}

function for_integer_validation(integer) {
    console.log(integer)
    let check_validation_integer = new RegExp(validations['integer'][0]);
    if (integer.value == '0') {
        integer.setCustomValidity('');
    }
    else if (!check_validation_integer.test(integer.value)) {
        let first_span_tag = integer.closest('span')
        let second_span_tag = first_span_tag.closest('span')
        if (second_span_tag.classList.contains('field-requirement')) {
            integer.setCustomValidity(validations['integer'][1]);
            return false;
        }
        else {
            if (integer.value) {
                integer.setCustomValidity(validations['integer'][1]);
                return false;
            }
            else {
                integer.setCustomValidity('');
            }
        }
    } else {
        integer.setCustomValidity('');
    }
}

function for_requirement_input(input) {
    console.log(input.value)
    if (input.value == '') {
        input.setCustomValidity('Field must be filled');
        return false;
    }
    else {
        let parent_span = input.closest('span')
        if (parent_span.classList.contains('validation-email')) {
            for_email_validation(input)
        }
        else if (parent_span.classList.contains('validation-integer')) {
            for_integer_validation(input)
        }
        else {
            input.setCustomValidity('');
        }

    }
}

    // ...............................end validation..............................



