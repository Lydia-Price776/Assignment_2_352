function view_data(flights, routes) {


    document.getElementById("book_button").style.display = "none"

    if (flights.length > 0) {
        if (flights.length === 1) {
            document.getElementById("flight_data").innerHTML += `<h2>${flights.length} Match Found </h2>`
        } else {
            document.getElementById("flight_data").innerHTML += `<h2>${flights.length} Matches Found </h2>`
        }
        for (const i in flights) {
            document.getElementById("flight_data").innerHTML += `<div id = "check_box"><input type="checkbox" name = 'check_box'value = ${flights[i]['route_id']} onclick="handleCheckbox(this)"> Select to Book </input></div><br>`
            console.log(flights[i])
            document.getElementById("flight_data").innerHTML += `<div id = 'flight_info'>Date: ${flights[i]['date']} <br>` +
                `Flight Number: ${flights[i]['route_id']} <br>` +
                `Price: $${flights[i]['price']} NZD<br>`
            for (const j in routes) {
                console.log(routes[j])
                if (flights[i]['route_id'] === routes[j]['route_id']) {
                    document.getElementById("flight_data").innerHTML +=
                        `Departure Time: ${routes[j]['departure_time']} <br>` +
                        `Arrival Time: ${routes[j]['arrival_time']} <br>`
                    console.log(routes[j]['stopover_location_id'])
                    if (routes[j]['stopover_location_id'] != null) {
                        document.getElementById("flight_data").innerHTML +=
                            `Stopover Location: ${routes[j]['stopover_location_id']} <br>` +
                            `Stopover Length: ${routes[j]['stopover_time']} <br>`
                    }
                }
            }

            document.getElementById("flight_data").innerHTML += `</div><br>`
            document.getElementById("book_button").style.display = "block"

        }
    } else {
        document.getElementById("flight_data").innerHTML = `<h2>No Matches Found. </h2> <br>` +
            `<p> Please try entering a different date and make sure the arrival and departure locations are different </p>`
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

function book_flight() {
    const uri = `http://127.0.0.1:8000/book/`;
    const config = "";
    const win = window.open(uri, "", config);
}