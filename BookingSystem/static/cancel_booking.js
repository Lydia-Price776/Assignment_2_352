function display_outcome(outcome) {
    let outcome_div = document.getElementById('outcome');
    if (outcome === 'success') {
        outcome_div.innerHTML += 'Your booking was cancelled successfully'
    } else {
        outcome_div.innerHTML += 'There was an error cancelling your booking <br>' +
            'Please try again later or contact our help desk during business hours '
    }
}