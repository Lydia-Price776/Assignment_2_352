function display_booking(booking, passenger, flight, route) {
    let booking_details_div = document.getElementById("booking_details");

    let flight_data = format_flight(flight, route, "flight_booked");
    let booking_details = format_booking(booking, route);
    let passenger_details = format_passenger(passenger);
    console.log(passenger)
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

function display_error() {
    let booking_details_div = document.getElementById("booking_details");
    let no_booking_div = document.createElement('div');
    no_booking_div.id = "booking_data";
    no_booking_div.innerHTML += `Something went wrong making your booking. ` +
        `Please contact our helpdesk during business hours`;
    booking_details_div.appendChild(no_booking_div);
}

function create_cancel_button() {
    let cancel_button = document.createElement('button');
    cancel_button.id = 'cancel_button';
    cancel_button.type = 'submit';
    cancel_button.innerHTML = 'Cancel Booking';
    return cancel_button;
}

function create_cancel_data(booking_id) {
    let cancel_id = document.createElement('input');
    cancel_id.type = 'hidden';
    cancel_id.id = 'cancel_booking';
    cancel_id.name = 'cancel_booking';
    cancel_id.value = booking_id
    return cancel_id;
}

function add_cancel_option(booking_id) {
    let cancel_form = document.getElementById("cancel_booking");
    let cancel_button = create_cancel_button();
    let cancel_id = create_cancel_data(booking_id);
    cancel_form.appendChild(cancel_id)
    cancel_form.appendChild(cancel_button)
}