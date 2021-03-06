$(document).ready(function(){
    $('#date').mask('0000-00-00');
    $('#phone').mask('(00)000-00-00');
});
function validationAll() {
    if (
        document.getElementById("phone").classList.contains('is-valid')
        && document.getElementById("first_name").classList.contains('is-valid')
        && document.getElementById("delivery_date").classList.contains('is-valid')
        && document.getElementById("delivery_time").classList.contains('is-valid')
        && document.getElementById("address").classList.contains('is-valid')
        && document.getElementById("payment").classList.contains('is-valid')
        && document.getElementById("delivery_time").classList.contains('is-valid')
    ) {
        document.getElementById("order-submit").disabled = false;
        document.getElementById("alert-message").style.display = 'none';
    } else {
        document.getElementById("order-submit").disabled = true;
        document.getElementById("alert-message").style.display = 'block';
    }
}
validationAll();


function validateField(field, fieldId, minCount, maxCount) {
    if (field.length < minCount || field.length >= maxCount) {
        document.getElementById(fieldId).className = 'form-control is-invalid';
        validationAll();
    } else {
        document.getElementById(fieldId).className = 'form-control is-valid';
        validationAll();
    }
}

function validatePaymentWay() {
    validPayment = document.querySelector('#payment').value;
    validateField(validPayment, "payment", 1, 2);
}

function validatePhone() {
    let phoneMasked = document.getElementById("phone").value;
    var numb = phoneMasked.match(/\d/g);
    numb = numb.join("");
    validateField(numb, "phone", 9, 10);
}

function validateDate() {
    let dateField = document.getElementById("delivery_date").value;
    var thenum = dateField.match(/\d+/g).map(Number).join('');
    validateField(dateField, "delivery_date", 10, 11);
}

function validateTime() {
    validTime = document.querySelector('#delivery_time').value;
    validateField(validTime, "delivery_time", 1, 2);
}

function validateAddress() {
    let address = document.getElementById("address").value;
    validateField(address, "address", 5, 100);
}

function validateName() {
    let nameField = document.getElementById("first_name").value;
    validateField(nameField, "first_name", 3, 100);
}

function validateComment() {
    let commentField = document.getElementById("comment");
    if (commentField.value.length >= 100) {
        commentField.className = 'form-control is-invalid';
        validationAll();
    } else {
        commentField.className = 'form-control is-valid';
        validationAll();
    }
}

function phoneNumberToDigits() {
    let phoneMasked = document.getElementById("phone").value;
    var thenum = phoneMasked.match(/\d/g).map(Number);
    document.getElementById('phone').value = thenum.join('');
}

let submitBtn = document.getElementById('order-submit');

submitBtn.addEventListener('click', function(event){
    document.getElementById("order-submit").disabled = true;
    submitBtn.innerHTML = ('Ожидайте');
    event.preventDefault();
    let order = localStorage.getItem('order');
    phoneNumberToDigits();
    let redirectLink = '';
    let form = new FormData(document.querySelector("#order-form"));
    form.append("order", order);
    postData("/order/", form);
});

function postData(url = '', data = {}) {
    return fetch(url, {
        method: 'POST',
        redirect: 'manual',
        body: data,
    })
        .then(function(response) {
           return response.text();
        })
        .then(function(data) {
        let validPayment = document.querySelector('#payment').value;
            if (validPayment === '2'){
                if(data !== "error") {
                    localStorage.clear();
                    return window.location.href=data;
                } else {
                    $('#ModalCenteredWarning').modal('show');
                    return error = true;
                }
            } else {
                $('#ModalCenteredSucces').modal('show');
                localStorage.clear();
            }
        })
        .catch( (e) => {
            if (e.message) {
                alertString.innerHTML = (e.message);
                document.getElementById("alert-message").style.display = 'block';
            } else {
                alertString.innerHTML = ('Ошибка соединения');
                document.getElementById("alert-message").style.display = 'block';
            }
       })
}

$('#ModalCenteredSucces').on('hidden.bs.modal', function (e) {
window.location="/"})


//! moment.js locale configuration

;(function (global, factory) {
   typeof exports === 'object' && typeof module !== 'undefined'
       && typeof require === 'function' ? factory(require('../moment')) :
   typeof define === 'function' && define.amd ? define(['../moment'], factory) :
   factory(global.moment)
}(this, (function (moment) { 'use strict';


    function plural(word, num) {
        var forms = word.split('_');
        return num % 10 === 1 && num % 100 !== 11 ? forms[0] : (num % 10 >= 2 && num % 10 <= 4 && (num % 100 < 10 || num % 100 >= 20) ? forms[1] : forms[2]);
    }
    function relativeTimeWithPlural(number, withoutSuffix, key) {
        var format = {
            'ss': withoutSuffix ? 'секунда_секунды_секунд' : 'секунду_секунды_секунд',
            'mm': withoutSuffix ? 'минута_минуты_минут' : 'минуту_минуты_минут',
            'hh': 'час_часа_часов',
            'dd': 'день_дня_дней',
            'MM': 'месяц_месяца_месяцев',
            'yy': 'год_года_лет'
        };
        if (key === 'm') {
            return withoutSuffix ? 'минута' : 'минуту';
        }
        else {
            return number + ' ' + plural(format[key], +number);
        }
    }
    var monthsParse = [/^янв/i, /^фев/i, /^мар/i, /^апр/i, /^ма[йя]/i, /^июн/i, /^июл/i, /^авг/i, /^сен/i, /^окт/i, /^ноя/i, /^дек/i];

    // http://new.gramota.ru/spravka/rules/139-prop : § 103
    // Сокращения месяцев: http://new.gramota.ru/spravka/buro/search-answer?s=242637
    // CLDR data:          http://www.unicode.org/cldr/charts/28/summary/ru.html#1753
    var ru = moment.defineLocale('ru', {
        months : {
            format: 'января_февраля_марта_апреля_мая_июня_июля_августа_сентября_октября_ноября_декабря'.split('_'),
            standalone: 'январь_февраль_март_апрель_май_июнь_июль_август_сентябрь_октябрь_ноябрь_декабрь'.split('_')
        },
        monthsShort : {
            // по CLDR именно "июл." и "июн.", но какой смысл менять букву на точку ?
            format: 'янв._февр._мар._апр._мая_июня_июля_авг._сент._окт._нояб._дек.'.split('_'),
            standalone: 'янв._февр._март_апр._май_июнь_июль_авг._сент._окт._нояб._дек.'.split('_')
        },
        weekdays : {
            standalone: 'воскресенье_понедельник_вторник_среда_четверг_пятница_суббота'.split('_'),
            format: 'воскресенье_понедельник_вторник_среду_четверг_пятницу_субботу'.split('_'),
            isFormat: /\[ ?[Вв] ?(?:прошлую|следующую|эту)? ?\] ?dddd/
        },
        weekdaysShort : 'вс_пн_вт_ср_чт_пт_сб'.split('_'),
        weekdaysMin : 'вс_пн_вт_ср_чт_пт_сб'.split('_'),
        monthsParse : monthsParse,
        longMonthsParse : monthsParse,
        shortMonthsParse : monthsParse,

        // полные названия с падежами, по три буквы, для некоторых, по 4 буквы, сокращения с точкой и без точки
        monthsRegex: /^(январ[ья]|янв\.?|феврал[ья]|февр?\.?|марта?|мар\.?|апрел[ья]|апр\.?|ма[йя]|июн[ья]|июн\.?|июл[ья]|июл\.?|августа?|авг\.?|сентябр[ья]|сент?\.?|октябр[ья]|окт\.?|ноябр[ья]|нояб?\.?|декабр[ья]|дек\.?)/i,

        // копия предыдущего
        monthsShortRegex: /^(январ[ья]|янв\.?|феврал[ья]|февр?\.?|марта?|мар\.?|апрел[ья]|апр\.?|ма[йя]|июн[ья]|июн\.?|июл[ья]|июл\.?|августа?|авг\.?|сентябр[ья]|сент?\.?|октябр[ья]|окт\.?|ноябр[ья]|нояб?\.?|декабр[ья]|дек\.?)/i,

        // полные названия с падежами
        monthsStrictRegex: /^(январ[яь]|феврал[яь]|марта?|апрел[яь]|ма[яй]|июн[яь]|июл[яь]|августа?|сентябр[яь]|октябр[яь]|ноябр[яь]|декабр[яь])/i,

        // Выражение, которое соотвествует только сокращённым формам
        monthsShortStrictRegex: /^(янв\.|февр?\.|мар[т.]|апр\.|ма[яй]|июн[ья.]|июл[ья.]|авг\.|сент?\.|окт\.|нояб?\.|дек\.)/i,
        longDateFormat : {
            LT : 'H:mm',
            LTS : 'H:mm:ss',
            L : 'DD.MM.YYYY',
            LL : 'D MMMM YYYY г.',
            LLL : 'D MMMM YYYY г., H:mm',
            LLLL : 'dddd, D MMMM YYYY г., H:mm'
        },
        calendar : {
            sameDay: '[Сегодня, в] LT',
            nextDay: '[Завтра, в] LT',
            lastDay: '[Вчера, в] LT',
            nextWeek: function (now) {
                if (now.week() !== this.week()) {
                    switch (this.day()) {
                        case 0:
                            return '[В следующее] dddd, [в] LT';
                        case 1:
                        case 2:
                        case 4:
                            return '[В следующий] dddd, [в] LT';
                        case 3:
                        case 5:
                        case 6:
                            return '[В следующую] dddd, [в] LT';
                    }
                } else {
                    if (this.day() === 2) {
                        return '[Во] dddd, [в] LT';
                    } else {
                        return '[В] dddd, [в] LT';
                    }
                }
            },
            lastWeek: function (now) {
                if (now.week() !== this.week()) {
                    switch (this.day()) {
                        case 0:
                            return '[В прошлое] dddd, [в] LT';
                        case 1:
                        case 2:
                        case 4:
                            return '[В прошлый] dddd, [в] LT';
                        case 3:
                        case 5:
                        case 6:
                            return '[В прошлую] dddd, [в] LT';
                    }
                } else {
                    if (this.day() === 2) {
                        return '[Во] dddd, [в] LT';
                    } else {
                        return '[В] dddd, [в] LT';
                    }
                }
            },
            sameElse: 'L'
        },
        relativeTime : {
            future : 'через %s',
            past : '%s назад',
            s : 'несколько секунд',
            ss : relativeTimeWithPlural,
            m : relativeTimeWithPlural,
            mm : relativeTimeWithPlural,
            h : 'час',
            hh : relativeTimeWithPlural,
            d : 'день',
            dd : relativeTimeWithPlural,
            M : 'месяц',
            MM : relativeTimeWithPlural,
            y : 'год',
            yy : relativeTimeWithPlural
        },
        meridiemParse: /ночи|утра|дня|вечера/i,
        isPM : function (input) {
            return /^(дня|вечера)$/.test(input);
        },
        meridiem : function (hour, minute, isLower) {
            if (hour < 4) {
                return 'ночи';
            } else if (hour < 12) {
                return 'утра';
            } else if (hour < 17) {
                return 'дня';
            } else {
                return 'вечера';
            }
        },
        dayOfMonthOrdinalParse: /\d{1,2}-(й|го|я)/,
        ordinal: function (number, period) {
            switch (period) {
                case 'M':
                case 'd':
                case 'DDD':
                    return number + '-й';
                case 'D':
                    return number + '-го';
                case 'w':
                case 'W':
                    return number + '-я';
                default:
                    return number;
            }
        },
        week : {
            dow : 1, // Monday is the first day of the week.
            doy : 4  // The week that contains Jan 4th is the first week of the year.
        }
    });

    return ru;

})));



