/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./toursite/static/toursite/scripts/order.js":
/*!***************************************************!*\
  !*** ./toursite/static/toursite/scripts/order.js ***!
  \***************************************************/
/***/ (() => {

  document.addEventListener('DOMContentLoaded', function () {
    const startDateInput = document.getElementById('start_date');
    const endDateInput = document.getElementById('end_date');
    const numPeopleInput = document.getElementById('num_people');
    const costDisplay = document.getElementById('final_cost');
    console.log("hello");

    // Отримання значень
    const transportCost = parseInt(document.getElementById('order_script').getAttribute('data-transport-cost'));
    const hotelCostPerDay = parseInt(document.getElementById('order_script').getAttribute('data-hotel-cost'));
    const excursionCosts = document.getElementById('order_script').getAttribute('data-excursion-costs').split(',').map(Number);

    // Функція для валідації дат
    function validateDates() {
        const startDate = new Date(startDateInput.value);
        const endDate = new Date(endDateInput.value);

        if (startDate < new Date()) {
            alert("Дата початку повинна бути не менше поточної дати.");
            return false;
        }

        if (endDate < startDate) {
            alert("Дата кінця повинна бути не менше, ніж дата початку.");
            return false;
        }

        return true;
    }

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
            console.log("hello2");

        } else {
            costDisplay.textContent = "Введіть коректні дані";
            console.log("hello");

        }
    }

    // Додавання обробників подій для валідації
    startDateInput.addEventListener('input', function () {
        if (!validateDates()) {
            startDateInput.value = ''; // Очищаємо поле, якщо введено некоректну дату
        }
        calculateCost();
    });

    endDateInput.addEventListener('input', function () {
        if (!validateDates()) {
            endDateInput.value = ''; // Очищаємо поле, якщо введено некоректну дату
        }
        calculateCost();
    });

    numPeopleInput.addEventListener('input', calculateCost);

    // Додавання обробника подій для відправки форми
    document.getElementById('order').addEventListener('submit', function (event) {
        if (!validateDates()) {
            event.preventDefault(); // Перешкоджаємо відправці форми при некоректних датах
        }
    });

    // Первинний розрахунок при завантаженні сторінки
    calculateCost();
});

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./toursite/static/toursite/scripts/order.js"]();
/******/ 	
/******/ })()
;
