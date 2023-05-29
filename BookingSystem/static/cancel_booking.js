function display_outcome(outcome) {
    let outcome_div = document.getElementById('outcome');
    if (outcome['outcome'] === 'success') {
        outcome_div.innerHTML += 'Your booking was cancelled successfully'
    } else {
        outcome_div.innerHTML += 'There was an error cancelling your booking. ' +
            'Please try again later or contact out help desk during business hours '
    }
}