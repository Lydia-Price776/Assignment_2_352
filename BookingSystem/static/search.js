function view_data(flights, routes) {

    if (flights.length > 0) {
        let match = document.createElement('div')
        if (flights.length === 1) {
            match.innerHTML += `<h2>${flights.length} Match Found </h2>`
        } else {
            match.innerHTML += `<h2>${flights.length} Matches Found </h2>`
        }
        document.getElementById('booking_form').appendChild(match)
        for (const i in flights) {
            let check_box = document.createElement('input');
            check_box.type = 'checkbox';
            check_box.name = "check_box";
            check_box.id = `check_box${i}`;
            check_box.value = flights[i]['route_id'];
            check_box.onclick = function (checkbox) {
                let checkboxes = document.getElementsByName("check_box");
                checkboxes.forEach(function (currentCheckbox) {
                    if (currentCheckbox.id !== checkbox.target.id) {
                        currentCheckbox.checked = false;
                    }
                });
            }
            document.getElementById('booking_form').appendChild(check_box)
            let flight_data = document.createElement("label");
            flight_data.htmlFor = `check_box${i}`;
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
        let submit_button = document.createElement("button")
        submit_button.type = 'submit';
        submit_button.id = 'booking_button';
        submit_button.innerHTML = 'Book';
        document.getElementById("booking_form").appendChild(submit_button);

    } else {
        let no_match = document.createElement('div')
        no_match.innerHTML = `<h2>No Matches Found. </h2> <br>` +
            `<p> Please try entering a different date and make sure the arrival and departure locations are different </p>`
        document.getElementById("booking_form").appendChild(no_match)

    }
}

function handleCheckbox(checkbox) {

}

