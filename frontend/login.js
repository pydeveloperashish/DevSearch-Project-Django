let form = document.getElementById('login-form');

form.addEventListener('submit', (e) => {
    e.preventDefault()
    // console.log('Form was successfully submitted')
    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }
    // console.log('Form data:', formData)
    fetch('http://127.0.0.1:8000/api/users/token/', {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('Data:', data.access);
            if (data.access) {
                localStorage.setItem('token', data.access);
                window.location = 'file:///media/ashish/DATA/Python37/Django-Tutorials/DevSearch-FrontEnd-Dennis-Ivy-Course/project-list.html';

            }
            else {
                alert('Username or password is incorrect')
            }
        })

})