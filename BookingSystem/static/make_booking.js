function display_flight(flight, route, airports) {
    let heading_div = document.getElementById("heading");
    heading_div.innerHTML += `From ${airports['departure']} to ${airports['arrival']}`;
    document.getElementById('flight_details_header').innerHTML += `<h3>Flight Details:</h3>`

    document.getElementById('passenger_details').innerHTML += `<h3>Your Details:</h3>`

    let flight_data = display_flight_data(flight, route, "flight_to_book")
    let booking_button = document.getElementById('book_button');
    console.log(flight['seats_available'])
    if (flight['seats_available'] > 0) {
        booking_button.disabled = false;
        booking_button.title = '';
    } else {
        booking_button.disabled = true;
    }

    document.getElementById("flight_details").appendChild(flight_data);
}

function display_flight_data(flight, route, id) {
    let flight_data = document.createElement('div');
    flight_data.id = id;
    flight_data.innerHTML += `<b>Date:</b> ${flight['date']} <br>` +
        `<b>Flight Number</b>: ${flight['route_id']} <br>` +
        `<b>Price:</b> $${flight['price']} NZD<br>` +
        `<b>Departure Time:</b> ${route['departure_time']} (${airports['departure_time_zone']}) <br>` +
        `<b>Arrival Time:</b> ${route['arrival_time']} (${airports['arrival_time_zone']}) <br>`;
    if (route['stopover_location_id'] != null) {
        flight_data.innerHTML += `Stopover Location: ${route['stopover_location_id']} <br>` +
            `Stopover Length: ${route['stopover_time']} minutes<br>`;
    } else {
        flight_data.innerHTML += `<b>Stopover Location:</b> NA <br>` +
            `<b>Stopover Length:</b> NA <br>`;
    }
    return flight_data;
}