$(function () {
    $('#myForm').validate({
        rules: {
            first_name: { required: true, minlength: 3, maxlength: 10 },
            last_name: { required: true, minlength: 3, maxlength: 10 },
            email: { required: true, email: true },
            dob: { required: true }
        },
        messages: {
            first_name: {
                required: 'Please enter a firstname',
                minlength: 'Minimum 3 characters',
                maxlength: 'Maximum 10 characters'
            },
            last_name: {
                required: 'Please enter a lastname',
                minlength: 'Minimum 3 characters',
                maxlength: 'Maximum 10 characters'
            },
            email: {
                required: 'Please enter your email',
                email: 'Enter a valid email'
            },
            dob: {
                required: 'Please provide a date of birth'
            }
        },
        errorElement: 'small',
        errorClass: 'text-danger',
        highlight:   el => $(el).addClass('is-invalid'),
        unhighlight: el => $(el).removeClass('is-invalid')
        // highlight: function (el) {
        //     $(el).addClass('is-invalid')
        // },
        // unhighlight: function (el) {
        //     $(el).removeClass('is-invalid')
        // }
    })
})