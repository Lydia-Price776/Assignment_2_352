function add_flight_data(i, flights, routes) {

    let table_row = document.createElement('tbody');
    let flight_data_row = [flights[i]['date'], flights[i]['route_id'], flights[i]['price']];
    for (const j in routes) {
        if (flights[i]['route_id'] === routes[j]['route_id']) {
            flight_data_row.push(routes[j]['departure_time']);
            flight_data_row.push(routes[j]['arrival_time']);

            if (routes[j]['stopover_location_id'] != null) {
                flight_data_row.push(routes[j]['stopover_location_id']);
                flight_data_row.push(routes[j]['stopover_time']);

            } else {
                flight_data_row.push('NA');
                flight_data_row.push('NA');
            }
        }
    }

    let row_element = document.createElement('tr');
    for (const item of flight_data_row) {
        let cell = document.createElement('td');
        cell.textContent = item;
        row_element.appendChild(cell);
    }


    let check_box = add_check_box(i, flights);
    let cell = document.createElement('td');
    cell.appendChild(check_box);
    row_element.appendChild(cell);
    table_row.appendChild(row_element);


    return table_row;
}


function handleCheckboxAndButton() {
    return function (checkbox) {
        let checkboxes = document.getElementsByName('check_box');
        checkboxes.forEach(function (currentCheckbox) {
            if (currentCheckbox.id !== checkbox.target.id) {
                currentCheckbox.checked = false;
            }
        });

        let enable = true;

        for (let i = 0; i < checkboxes.length; i++) {
            if (checkboxes[i].checked) {
                enable = false;
                break;
            }
        }

        document.getElementById('booking_button').disabled = enable;
    };
}

function add_check_box(i, flights) {
    let check_box = document.createElement('input');
    check_box.type = 'checkbox';
    check_box.name = 'check_box';
    check_box.id = `check_box${i}`;
    check_box.onclick = handleCheckboxAndButton();
    check_box.value = JSON.stringify(flights[i]);
    return check_box;
}

function add_submit_button() {
    let submit_button = document.createElement('button')
    submit_button.type = 'submit';
    submit_button.id = 'booking_button';
    submit_button.innerHTML = 'Book';
    submit_button.classList.add("btn", "btn-primary");
    submit_button.disabled = true;
    document.getElementById('button').appendChild(submit_button);
}

function create_table() {
    let table = document.getElementById("table");
    let t_header = document.createElement('thead');
    let header_row = document.createElement('tr');

    let headings = ['Date', 'Flight Number', 'Price', 'Departure Time', 'Arrival Time', 'Stopover Location', 'Stopover Length', 'Select To Book'];
    headings.forEach(function (heading) {
        let th = document.createElement('th');
        th.scope = "col";
        th.textContent = heading;
        header_row.appendChild(th);
    });
    t_header.appendChild(header_row);

    table.appendChild(t_header);

}

function view_data(flights, routes, airports) {
    let heading_div = document.getElementById("heading");
    heading_div.innerHTML += `From ${airports['departure']} to ${airports['arrival']}`;

    let match = document.getElementById('matches');

    if (flights.length > 0) {
        create_table(flights)
        if (flights.length === 1) {
            match.innerHTML = `<h3>${flights.length} Match Found: </h3>`
        } else {
            match.innerHTML = `<h3>${flights.length} Matches Found: </h3>`
        }
        for (const i in flights) {
            let row = add_flight_data(i, flights, routes);
            document.getElementById('table').appendChild(row);
        }
        add_submit_button();
    } else {
        match.innerHTML = `<h3>No Matches Found. </h3>` +
            `<p> Please try entering a different date and make sure the arrival and departure locations are different </p>`
    }
}

function display_error_past_date() {
    let booking_form = document.getElementById("booking_form");
    let error = document.createElement('div');
    error.id = "error";
    error.innerHTML = `Unable to display past flights for booking. Please enter future departure date.`;
    error.style.fontSize = '20px';
    error.classList.add('text-center');
    booking_form.appendChild(error);
}