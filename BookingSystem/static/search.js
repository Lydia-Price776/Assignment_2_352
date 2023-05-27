function view_data(flights, routes) {

    document.getElementById("book_button").style.display = "none"

    if (flights.length > 0) {
        let flight_data = document.createElement('div')
        if (flights.length === 1) {
            flight_data.innerHTML += `<h2>${flights.length} Match Found </h2>`
        } else {
            flight_data.innerHTML += `<h2>${flights.length} Matches Found </h2>`
        }
        for (const i in flights) {
            let check_box = document.createElement('input');
            check_box.type = 'checkbox';
            check_box.id = 'check_box'
            check_box.value = flights[i]['route_id']
            document.getElementById('booking-form').appendChild(check_box)


            flight_data.id = `flight_${i}`
            flight_data.innerHTML += `Date: ${flights[i]['date']} <br>` +
                `Flight Number: ${flights[i]['route_id']} <br>` +
                `Price: $${flights[i]['price']} NZD<br>`
            for (const j in routes) {
                if (flights[i]['route_id'] === routes[j]['route_id']) {
                    flight_data.innerHTML += `Departure Time: ${routes[j]['departure_time']} <br>` +
                        `Arrival Time: ${routes[j]['arrival_time']} <br>`
                    if (routes[j]['stopover_location_id'] != null) {
                        flight_data.innerHTML += `Stopover Location: ${routes[j]['stopover_location_id']} <br>` +
                            `Stopover Length: ${routes[j]['stopover_time']} <br>`
                    }
                }
            }

            flight_data.innerHTML += `</div><br>`
            document.getElementById("booking_form").appendChild(flight_data)

        }
        document.getElementById("book_button").style.display = "block"

    } else {
        let flight_data = document.createElement('div')
        flight_data.innerHTML = `<h2>No Matches Found. </h2> <br>` +
            `<p> Please try entering a different date and make sure the arrival and departure locations are different </p>`
        document.getElementById("booking_form").appendChild(flight_data)

    }
}

function handleCheckbox(checkbox) {
    let checkboxes = document.getElementsByName("check_box");
    checkboxes.forEach(function (currentCheckbox) {
        if (currentCheckbox !== checkbox) {
            currentCheckbox.checked = false;
        }
    });
}

