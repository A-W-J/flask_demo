function createPerson(name, age, occupation) {
    // Create the data object
    const personData = {
        Name: name,
        Age: age,
        Occupation: occupation
    };

    // Send a POST request to the server
    fetch('/create_person', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(personData)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        alert('Person created: ' + JSON.stringify(personData));
    })
    .catch(error => console.error('Error:', error));
}

