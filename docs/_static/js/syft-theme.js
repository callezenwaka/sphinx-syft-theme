// Import CSS variables
// ref: https://css-tricks.com/getting-javascript-to-talk-to-css-and-sass/
// import "../styles/sphinx-syft-theme.scss";

/**
 * A helper function to load scripts when the DOM is loaded.
 * This waits for everything to be on the page first before running, since
 * some functionality doesn't behave properly until everything is ready.
 */
var sbRunWhenDOMLoaded = (cb) => {
  if (document.readyState != "loading") {
    cb();
  } else if (document.addEventListener) {
    document.addEventListener("DOMContentLoaded", cb);
  } else {
    document.attachEvent("onreadystatechange", function () {
      if (document.readyState == "complete") cb();
    });
  }
};

/**
 * Toggle text field
 * @param {*} id
 */
function toggleConditional(selectId, conditionalId) {
  const select = document.getElementById(selectId);
  const conditional = document.getElementById(conditionalId);
  if (select.value === "no" && selectId !== "problem-encountered") {
    conditional.style.display = "block";
  } else if (select.value === "yes" && selectId === "problem-encountered") {
    conditional.style.display = "block";
  } else {
    conditional.style.display = "none";
  }
}

/**
 * Handle feedback submission
 */
async function addFeedback() {
  // TODO:
  const feedbackTitle = document.getElementById("feedback--title");
  if (!feedbackTitle) return;
  feedbackTitle.addEventListener("click", toggleFeebackForm);

  const feedbackForm = document.querySelector("#feedback--form");
  feedbackForm.addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the default form submission
    // Your code here
    const formElement = document.querySelector("#feedback--form");
    const formData = new FormData(formElement);

    const formsvgCheck = document.getElementById("form--svgcheck");
    formsvgCheck.classList.toggle("active");
    setTimeout(function () {
      // change checkmark
      formData.forEach((value, key) => {
        console.log(`${key}: ${value}`);
      });
      document.getElementById("description").value = "";
      document.getElementById("email").value = "";
      formsvgCheck.classList.toggle("active");
    }, 1500);
  });
}

/**
 * Beep on feedback activation
 */
async function feedbackBeep() {
  const sound = new Audio("/_static/audio/bot_notification.mp3");
  sound.play();
}

/**
 * Toggle feedback
 * @param {*} event
 */
function toggleFeebackForm(event) {
  // Your code here
  event.preventDefault(); // Prevent the default form submission
  const feedbackContainer = document.getElementById("feedback--container");
  const feedbackArrow = document.getElementById("feedback--arrow");
  feedbackContainer.classList.toggle("feedback--box");
  feedbackContainer.classList.toggle("active");
  feedbackArrow.classList.toggle("active");
}

/**
 * Define the function to handle scroll and toggle feedback form
 */
function addScrollEvent() {
  // TODO:
  const FEEDBACK_KEY = "syft-feedback";
  document.addEventListener("scroll", function (event) {
    const feedbackContainer = document.getElementById("feedback--container");
    if (!feedbackContainer) return;

    // Retrieve the value (convert back to boolean)
    const FEEDBACK = JSON.parse(localStorage.getItem(FEEDBACK_KEY)) || false;
    const isFormActive = feedbackContainer.classList.contains("active");
    const scrollPosition = window.scrollY + window.innerHeight;
    const threshold = document.documentElement.scrollHeight * 0.95;

    if (scrollPosition >= threshold && !isFormActive && !FEEDBACK) {
      // make sound
      feedbackBeep();
      // toggle feedback form
      toggleFeebackForm(event);

      // Set a boolean value
      localStorage.setItem(FEEDBACK_KEY, true);
    }
  });
}

/**
 * Set up functions to load when the DOM is ready
 */
sbRunWhenDOMLoaded(addFeedback);
sbRunWhenDOMLoaded(addScrollEvent);
