const myNumbers = [1, 2, 3, 4];

// for (const number of myNumbers) {
//     console.log (`Number was: ${number}`)
// }

// OR

// myNumbers.forEach((element) => {
//     console.log (`Number was: ${element}`)
// })


// OR

// const myNumberFunction = (number) => {
//     console.log (`Number was: ${number}`);
// };

// myNumbers.forEach(myNumberFunction);

// myNumbers.forEach((number, index) => {
//     console.log (`Next number was: ${number}) at index ${index}`);
// })

// const myNumberFunction = (number, index) => {
//     console.log (`Number was: ${number} at index ${index}`);
// };

// myNumbers.forEach(myNumberFunction);

// const multipliedByTwo = function (numbers) {
//     const multipliedNums = [];

//     numbers.forEach((number) => {
//         const multipliedNum = number * 2;
//         multipliedNums.push(multipliedNum);
//     })

//     return multipliedNums;
// }

// console.log('Numbers before multiplication: ', myNumbers);
// console.log('Numbers after multiplication: ', multipliedByTwo(myNumbers));

const getEvens = function (arrayOfNums) {
    const evenNumbers = [];

    arrayOfNums.forEach ((number) => {
        if (number % 2 === 0) {
            evenNumbers.push(number);
        }
    })

    return evenNumbers;
}

console.log('Even numbers: ', getEvens(myNumbers));