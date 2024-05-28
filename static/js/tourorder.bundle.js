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

/***/ "./assets/scripts/tourorder.js":
/*!*************************************!*\
  !*** ./assets/scripts/tourorder.js ***!
  \*************************************/
/***/ (() => {

eval("document.addEventListener('DOMContentLoaded', function () {\n  var numPeopleInput = document.getElementById('num_people');\n  var costDisplay = document.getElementById('cost_display');\n  numPeopleInput.addEventListener('change', function () {\n    var numPeople = parseInt(this.value);\n    if (!isNaN(numPeople) && numPeople > 0) {\n      var cost = numPeople * parseInt(costDisplay.dataset.cost);\n      costDisplay.textContent = 'До сплати: ' + cost + \" ₴\";\n    } else {\n      costDisplay.textContent = 'До сплати: ' + parseInt(costDisplay.dataset.cost) + \" ₴\";\n    }\n  });\n});\n\n//# sourceURL=webpack://tourproject/./assets/scripts/tourorder.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./assets/scripts/tourorder.js"]();
/******/ 	
/******/ })()
;