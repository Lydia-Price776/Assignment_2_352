function display_flight(flight, route) {
    let flight_data = display_flight_data(flight, route, "flight_to_book")
    let form = document.getElementById('booking_details');
    form.insertBefore(flight_data, form.firstChild);
}

function display_flight_data(flight, route, id) {
    let flight_data = document.createElement('div');
    flight_data.id = id;
    flight_data.innerHTML += `Date: ${flight['date']} <br>` +
        `Flight Number: ${flight['route_id']} <br>` +
        `Price: $${flight['price']} NZD<br>` +
        `Departure Time: ${route['departure_time']} <br>` +
        `Arrival Time: ${route['arrival_time']} <br>`;
    if (route['stopover_location_id'] != null) {
        flight_data.innerHTML += `Stopover Location: ${route['stopover_location_id']} <br>` +
            `Stopover Length: ${route['stopover_time']} <br>`;
    }
    return flight_data;
}