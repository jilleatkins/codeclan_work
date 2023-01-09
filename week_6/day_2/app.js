const Pet = require('./pet.js');
const Person = require('./Person.js');

const Noodle = new Pet('Noodle', 'Cat')
Noodle.eat('chicken neck');

const Jill = new Person('Jill')
Jill.greet()