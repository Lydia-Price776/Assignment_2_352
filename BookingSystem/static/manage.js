function display_booking(booking, passenger, flight, route) {
    let flight_data = format_flight(flight, route, "flight_booked");
    let booking_details = format_booking(booking,route);
    let passenger_details = format_passenger(passenger);

    let booking_details_div = document.getElementById("booking_details");
    booking_details_div.appendChild(booking_details);
    booking_details_div.appendChild(passenger_details);
    booking_details_div.appendChild(flight_data);
}

function format_flight(flight, route) {
    let flight_data = document.createElement('div');
    flight_data.id = "flight_booked";
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

function format_booking(booking, route) {
    let booking_data = document.createElement('div');
    booking_data.id = "booking_data";
    booking_data.innerHTML += `Booking Refernce: ${booking['booking_id']} <br>` +
        `Route: ${route['departure_location_id']} to ${route['arrival_location_id']}`

    return booking_data;
}

function format_passenger(passenger) {
    let passenger_data = document.createElement('div');
    passenger_data.id = "passenger_data";
    passenger_data.innerHTML += `First Name: ${passenger['first_name']} <br>` +
        `Last Name: ${passenger['last_name']} <br>` +
        `Email Address: ${passenger['email']} <br>`;
    if (passenger["phone_number"] !== "") {
        passenger_data.innerHTML += `Phone Number: ${passenger['phone_number']} <br>`;
    } else {
        passenger_data.innerHTML += `Phone Number: Not Provided <br>`;
    }
    return passenger_data;

}