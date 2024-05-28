document.addEventListener('DOMContentLoaded', function () {
    const startDateInput = document.getElementById('start_date');
    const numPeopleInput = document.getElementById('num_people');
    const costDisplay = document.getElementById('tour_cost'); // Оголошуємо змінну для відображення вартості туру

    // Отримуємо вартість туру з атрибута data-cost
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

    // Функція для валідації дати
    function validateDate() {
        const startDate = new Date(startDateInput.value);
        const today = new Date();

        if (startDate < today) {
            alert("Дата початку повинна бути не раніше поточної дати.");
            return false;
        }

        return true;
    }

    // Додавання обробників подій для валідації та обчислення вартості
    startDateInput.addEventListener('input', function () {
        if (!validateDate()) {
            startDateInput.value = ''; // Очищаємо поле, якщо введено некоректну дату
        }
        calculateCost();
    });

    numPeopleInput.addEventListener('input', calculateCost);

    // Додавання обробника подій для відправки форми
    document.querySelector('form').addEventListener('submit', function (event) {
        if (!validateDate()) {
            event.preventDefault(); // Перешкоджаємо відправці форми при некоректній даті
        }
    });

    // Первинний розрахунок при завантаженні сторінки
    calculateCost();
});
