function display_booking(booking, passenger, flight, route) {

    format_flight(flight, route);
    format_booking(booking, route);
    format_passenger(passenger);
}

function format_flight(flight, route) {
    document.getElementById('flight_details_header').innerHTML = `<h4>Flight Details</h4>`;

    let flight_data = document.getElementById('flight_details');
    flight_data.id = "flight_booked";
    flight_data.innerHTML += `<b>Date:</b> ${flight['date']} <br>` +
        `<b>Flight Number:</b> ${flight['route_id']} <br>` +
        `<b>Price:</b> $${flight['price']} NZD<br>` +
        `<b>Departure Time:</b> ${route['departure_time']} <br>` +
        `<b>Arrival Time:</b> ${route['arrival_time']} <br>`;
    if (route['stopover_location_id'] != null) {
        flight_data.innerHTML += `<b>Stopover Location:</b> ${route['stopover_location_id']} <br>` +
            `<b>Stopover Length:</b> ${route['stopover_time']} minutes<br>`;
    } else {
        flight_data.innerHTML += `<b>Stopover Location:</b> NA <br>` +
            `<b>Stopover Length:</b> NA<br>`;
    }
}

function format_booking(booking) {
    let booking_data = document.getElementById('booking_ref');
    booking_data.id = "booking_data";
    booking_data.innerHTML += `<h3>Booking Reference: ${booking['booking_id']}</h3>`
}

function format_passenger(passenger) {
    document.getElementById("passenger_details_header").innerHTML = `<h4>Passenger Details</h4>`;

    let passenger_data = document.getElementById("passenger_details");
    passenger_data.id = "passenger_data";
    passenger_data.innerHTML += `<b>First Name:</b> ${passenger['first_name']} <br>` +
        `<b>Last Name:</b> ${passenger['last_name']} <br>` +
        `<b>Email Address:</b> ${passenger['email']} <br>`;
    if (passenger["phone_number"] !== "") {
        passenger_data.innerHTML += `<b>Phone Number:</b> ${passenger['phone_number']} <br>`;
    } else {
        passenger_data.innerHTML += `<b>Phone Number:</b> Not Provided <br>`;
    }
}

function display_error(booking, exists) {
    let error_div = document.getElementById("error");
    if (exists['exists'] === 'True') {
        error_div.innerHTML += `A booking under that name already exists for this flight <br>` +
            `Return to the home page to view your booking by entering your booking reference <br>` +
            `Please contact our helpdesk during business hours if you require additional help`;
    } else if (booking['error'] === 'unable to make booking') {
        error_div.innerHTML += `Something went wrong making your booking. <br>` +
            `Please contact our helpdesk during business hours`;
    } else {
        error_div.innerHTML += `Unable to retrieve your booking. <br> Please enter a valid booking reference or` +
            ` contact our helpdesk during business hours`;
    }

}

function create_cancel_button() {
    let cancel_button = document.createElement('button');
    cancel_button.id = 'cancel_button';
    cancel_button.type = 'submit';
    cancel_button.innerHTML = 'Cancel Booking';
    cancel_button.classList.add("btn", "btn-primary");
    return cancel_button;
}

function create_cancel_data(booking_id) {
    let cancel_id = document.createElement('input');
    cancel_id.type = 'hidden';
    cancel_id.id = 'cancel_data';
    cancel_id.name = 'cancel_data';
    cancel_id.value = booking_id;
    return cancel_id;
}

function add_cancel_option(booking_id) {
    let cancel_form = document.getElementById("cancel_button");
    let cancel_button = create_cancel_button();
    let cancel_id = create_cancel_data(booking_id);
    cancel_form.appendChild(cancel_id)
    cancel_form.appendChild(cancel_button)
}