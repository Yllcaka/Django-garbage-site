// /*const factorial = function fac(n) {
//             return n < 2 ? 1 : n * fac(n - 1)
//         }

//         console.log(factorial(10))
//         */
// /*function map(f, a) {
//     let result = [],
//         i; // Create a new Array // Declare variable
//     for (i = 0; i != a.length; i++)
//         result[i] = f(a[i]);
//     return result;
// }
// const f = function (x) {
//     return x * x * x;
// }

// function f(x) {
//     return x * x * x;
// }
// let numbers = [0, 1, 2, 5, 10];
// let cube = map(f, numbers);
// console.log(cube);
// */
// class Rectangle {
//     constructor(height, width) {
//         this.height = height;
//         this.width = width;
//     }
// }
// var man = new Object();
// var people = {
//     emri: "Ylli",
//     mbiemri: "Caka",
//     mosha: 18,
//     fullname: function () {
//         return `${this.emri} ${this.mbiemri}`
//     }
// }

// function Njeri(emri, mbiemri, mosha) {
//     this.first = emri;
//     this.last = mbiemri;
//     this.age = mosha;
//     /*this.fullname = function () {
//         return `${this.first} ${this.last}`;
//     }
//     */
//     this.fullname = function () {
//         return `${this.first} ${this.last}`;
//     }
// }
// var ylli = new Njeri("Ylli", "Caka", "19");
// man.emri = "Njeri";
// console.log(ylli.fullname());
// console.log(people.fullname());
// console.log(man.emri);
// // console.log((1, 2) => {
// //     return a * b
// // })
function factorial(n) {
    if (n < 2) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

function foo() {
    for (var i = 0; i < arguments.length; i++) {
        console.log(arguments[i]);
    }
}
// console.log(factorial(10));
console.log(foo(1, 2, 3, 4, 5))