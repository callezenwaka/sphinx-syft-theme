// Define constants and functions
const YEAR = new Date().getFullYear();
// let FEEDBACK = false;
// Set a boolean value
// sessionStorage.setItem("FEEDBACK", false);
const { origin, pathname } = location;
const { host, hostname, port } = new URL(origin);
const ENV = ['localhost', '127.0.0.1'].includes(hostname)? `dev` : `prod`;

async function buildNavigation() {
  // Build website nav paths
  const SITE_URL = ENV === 'prod'? `${origin}/${pathname.split('/')[1]}/${pathname.split('/')[2]}` : `http://${host}/docs/_build/html`;

  // build the href for the navigation tabs
  // const feedbackContainer = document.getElementById("feedback--container");
  const feedbackTitle = document.getElementById("feedback--title");
  const nodeList = document.querySelectorAll(".nav-item .nav-link.nav-internal");
  const links = Array.from(nodeList);

  // map href links
  links.map(link => {
    const { href } = link;
    var { pathname } = new URL(href);
    link.setAttribute("href", SITE_URL + pathname);
    return link;
  });

  // Select & replace the year element
  const copyrightElement = document.querySelector('.copyright');

  // Update the element with the modified text
  copyrightElement.textContent = `© Copyright ${YEAR}.`;

  feedbackTitle.addEventListener("click", toggleFeebackForm);

  const feedbackForm = document.querySelector("#feedback--form");
  feedbackForm.addEventListener("submit", async function (event) {
    // Prevent the default form submission
    event.preventDefault(); 
    // Your code here
    var baseSubmitURL = 'https://api.hsforms.com/submissions/v3/integration/submit'
    // Add the HubSpot portalID where the form should submit
    var portalId = '<PORTAL_ID>'
    // Add the HubSpot form GUID from your HubSpot portal
    var formGuid = '<FORM_GUID>' //replace with the formGUID copied from the form created inside HubSpot Forms
    // Build request URL
    var submitURL = `${baseSubmitURL}/${portalId}/${formGuid}`
    // Handle the form data
    await submitHSForm(submitURL);
  });

};

function toggleFeebackForm(event) {
  // Your code here
  event.preventDefault(); // Prevent the default form submission
  const feedbackContainer = document.getElementById("feedback--container");
  const feedbackArrow = document.getElementById("feedback--arrow");
  feedbackContainer.classList.toggle("feedback--box");
  feedbackContainer.classList.toggle("active");
  feedbackArrow.classList.toggle("active");
};

function formFieldsToHSJSON(form) {
  let fieldArray = [];
  let formData = new FormData(form);
  for (let field of formData) {
    let values = {
      "name": field[0],
      "value": field[1]
    }
    fieldArray.push(values)
  }
  return fieldArray;
};

function buildHSContext() {
  let hsContext = new Object()
  // hsContext.hutk = getCookie('hubspotutk');
  hsContext.pageUri = window.location.href;
  hsContext.pageName = document.title;
  return hsContext
};

async function prepareHSFormSubmission(form) {
  var submissionData = new Object()
  submissionData.submittedAt = Date.now()
  submissionData.fields = formFieldsToHSJSON(form)
  submissionData.context = buildHSContext()
  return submissionData
};

async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json() // parses JSON response into native JS objects
};

async function submitHSForm(hsFormURL) {
  const formElement = document.querySelector("#feedback--form");
  const formData = await prepareHSFormSubmission(formElement);

  // const data = await postData(hsFormURL, formData);
  const data = { inlineMessage: 'Thank you' };
  if(data.inlineMessage){
    // Set an inline thank you message
    // document.querySelector("#thankyou").innerHTML = data.inlineMessage
    const formsvgCheck = document.getElementById("form--svgcheck");
    formsvgCheck.classList.toggle("active");

    setTimeout(function () {
      // change checkmark
      formsvgCheck.classList.toggle("active");
    }, 1500);
  };
  // Reset feedback for
  document.getElementById('problem').value = 'no_problem';
};

document.addEventListener('mouseleave', function mouseLeave(event) {
  const feedbackContainer = document.getElementById("feedback--container");

  // Retrieve the value (convert back to boolean)
  const FEEDBACK = JSON.parse(sessionStorage.getItem("FEEDBACK")) || false;

  if (event.clientY <= 0 && !feedbackContainer.classList.contains('active') && !FEEDBACK) {
    // make sound
    feedbackBeep();
    // toggle feedback form
    toggleFeebackForm(event);
    // Set a boolean value
    sessionStorage.setItem("FEEDBACK", true);
  }
});

document.addEventListener("DOMContentLoaded", buildNavigation);
