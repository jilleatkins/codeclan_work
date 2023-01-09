const myForEach = function (arrayOfElements, callbackFunctionToExecute) {
    for (const element of arrayOfElements) {
        callback(element);
    }
}
                                                                                                                                                                                                                                                                                                                                                     
const numbers = [1, 2, 3, 4];

const myCallback = (element) => {
    console.log(`My element was: ${element}`);
}

// This
myForEach(numbers, myCallback);

// is equivalent to:
numbers.forEach(myCallback);