document.addEventListener('DOMContentLoaded', function() {
    const numPeopleInput = document.getElementById('num_people');
    const costDisplay = document.getElementById('cost_display');

    numPeopleInput.addEventListener('change', function() {
        const numPeople = parseInt(this.value);
        if (!isNaN(numPeople) && numPeople > 0) {
            const cost = numPeople * parseInt(costDisplay.dataset.cost);
            costDisplay.textContent = 'До сплати: ' + cost + " ₴";
        } else {
            costDisplay.textContent = 'До сплати: ' + parseInt(costDisplay.dataset.cost) + " ₴";
        }
    });
});
