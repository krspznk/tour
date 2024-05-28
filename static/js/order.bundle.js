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

/***/ "./assets/scripts/order.js":
/*!*********************************!*\
  !*** ./assets/scripts/order.js ***!
  \*********************************/
/***/ (() => {

eval("document.addEventListener('DOMContentLoaded', function () {\n  var startDateInput = document.getElementById('start_date');\n  var endDateInput = document.getElementById('end_date');\n  var numPeopleInput = document.getElementById('num_people');\n  var costDisplay = document.getElementById('final_cost');\n  console.log(\"hello\");\n\n  // Отримання значень\n  var transportCost = parseInt(document.currentScript.getAttribute('data-transport-cost'));\n  var hotelCostPerDay = parseInt(document.currentScript.getAttribute('data-hotel-cost'));\n  var excursionCosts = document.currentScript.getAttribute('data-excursion-costs').split(',').map(Number);\n  function calculateCost() {\n    var startDate = new Date(startDateInput.value);\n    var endDate = new Date(endDateInput.value);\n    var numPeople = parseInt(numPeopleInput.value);\n    console.log(\"hello1\");\n    if (startDate && endDate && numPeople) {\n      var totalDays = Math.ceil((endDate - startDate) / (1000 * 60 * 60 * 24));\n      var hotelCost = hotelCostPerDay * totalDays;\n      var excursionCost = excursionCosts.reduce(function (total, cost) {\n        return total + cost;\n      }, 0);\n      var finalCost = transportCost + hotelCost + excursionCost * numPeople;\n      costDisplay.textContent = finalCost;\n      console.log(\"hello2\");\n    } else {\n      costDisplay.textContent = \"Введіть коректні дані\";\n      console.log(\"hello\");\n    }\n  }\n\n  // Додавання обробників подій input\n  startDateInput.addEventListener('input', calculateCost);\n  endDateInput.addEventListener('input', calculateCost);\n  numPeopleInput.addEventListener('input', calculateCost);\n\n  // Первинний розрахунок при завантаженні сторінки\n  calculateCost();\n});\n\n//# sourceURL=webpack://tourproject/./assets/scripts/order.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./assets/scripts/order.js"]();
/******/ 	
/******/ })()
;