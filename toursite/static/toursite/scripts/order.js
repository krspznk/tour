document.addEventListener('DOMContentLoaded', function () {
    const startDateInput = document.getElementById('start_date');
    const endDateInput = document.getElementById('end_date');
    const numPeopleInput = document.getElementById('num_people');
    const costDisplay = document.getElementById('final_cost');
    const transportCost = parseInt(document.getElementById('order_script').getAttribute('data-transport-cost'));
    const hotelCostPerDay = parseInt(document.getElementById('order_script').getAttribute('data-hotel-cost'));
    const excursionCosts = document.getElementById('order_script').getAttribute('data-excursion-costs').split(',').map(Number);

    function calculateCost() {
        const startDate = new Date(startDateInput.value);
        const endDate = new Date(endDateInput.value);
        const numPeople = parseInt(numPeopleInput.value);

        if (startDate && endDate && numPeople) {
            const totalDays = Math.ceil((endDate - startDate) / (1000 * 60 * 60 * 24));
            const hotelCost = hotelCostPerDay * totalDays;
            const excursionCost = excursionCosts.reduce((total, cost) => total + cost, 0);
            const finalCost = transportCost + hotelCost + excursionCost * numPeople;

            costDisplay.textContent = finalCost;

        } 
    }

    startDateInput.addEventListener('input', calculateCost);
    endDateInput.addEventListener('input', calculateCost);
    numPeopleInput.addEventListener('input', calculateCost);

    calculateCost();
});
