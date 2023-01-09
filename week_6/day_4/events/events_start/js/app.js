// // 1. Which element will be dispatching the event?
// (e.g. document)
// // 2. Which event should we listen for?
// (e.g. 'DOMContentLoaded')
// // 3. Which piece of code should we run when the event is dispatched?
// (e.g. callback)

document.addEventListener('DOMContentLoaded', () => {
  console.log('JavaScript has loaded');

// ####################################################

// HANDLE BUTTON CLICK

  const handleButtonClick = function() {
    const resultParagraph = document.querySelector('#button-result');
    resultParagraph.textContent = 'That button has MOST DEFINITELY been clicked because you are an idiot.';
  }

  const button = document.querySelector('#button');
  button.addEventListener('click', handleButtonClick);

//##################################################### 

// HANDLE INPUT
  // 1. Get value from the input.
  // 2. Update the paragraph text.

  const handleInput = function(event) {
    const resultParagraph = document.querySelector('#input-result');
    resultParagraph.textContent = `You typed: "${event.target.value}" up there because you are a big idiot.`;
  }

  const textInput = document.querySelector('#input')
  textInput.addEventListener('input', handleInput);

//##################################################### 

// HANDLE SELECT (DROP-DOWN BOX)

  const handleSelectChange = function(event) {
    const resultParagraph = document.querySelector('#select-result');
    resultParagraph.textContent = `You selected: "${event.target.value}" because you are a stupid idiot.`;
  }

  const select = document.querySelector('#select');
  select.addEventListener('change', handleSelectChange);

//##################################################### 

// HANDLE FORM SUBMIT

  const handleFormSubmit = function(event) {
    event.preventDefault();
    const resultParagraph = document.querySelector('#form-result');
    resultParagraph.textContent = `
    You've said your name is
    "${event.target.first_name.value}
    ${event.target.last_name.value}"
    because you are a stupid idiot and lick fart holes.
    `
  }

  const form = document.querySelector('#form');
  form.addEventListener('submit', handleFormSubmit);

});
