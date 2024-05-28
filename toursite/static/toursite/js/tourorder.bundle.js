/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./toursite/static/toursite/scripts/tourorder.js":
/*!*******************************************************!*\
  !*** ./toursite/static/toursite/scripts/tourorder.js ***!
  \*******************************************************/
/***/ (() => {

  document.addEventListener('DOMContentLoaded', function () {
    const startDateInput = document.getElementById('start_date');
    const numPeopleInput = document.getElementById('num_people');
    const costDisplay = document.getElementById('tour_cost'); // Оголошуємо змінну для відображення вартості туру

    var tourCost = parseInt(costDisplay.getAttribute("data-cost"));

    function calculateCost() {
        const startDate = new Date(startDateInput.value);
        const numPeople = parseInt(numPeopleInput.value);

        if (startDate && numPeople) {
            const finalCost = tourCost * numPeople;

            costDisplay.textContent = 'До сплати: ' + finalCost + ' ₴';

        } else {
            costDisplay.textContent = "Введіть коректні дані";
        }
    }

    function validateDate() {
        const startDate = new Date(startDateInput.value);
        const today = new Date();

        if (startDate < today) {
            alert("Дата початку повинна бути не раніше поточної дати.");
            return false;
        }

        return true;
    }

    startDateInput.addEventListener('input', function () {
        if (!validateDate()) {
            startDateInput.value = ''; 
        }
        calculateCost();
    });

    numPeopleInput.addEventListener('input', calculateCost);

    document.querySelector('form').addEventListener('submit', function (event) {
        if (!validateDate()) {
            event.preventDefault(); 
        }
    });

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
/******/ 	__webpack_modules__["./toursite/static/toursite/scripts/tourorder.js"]();
/******/ 	
/******/ })()
;