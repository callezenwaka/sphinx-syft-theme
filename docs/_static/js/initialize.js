// // handle site constants
// const LANGUAGE = 'en';
// const VERSION = 'latest';
// const YEAR = new Date().getFullYear();

// handle window location and url
// const { origin, pathname } = location;
// const { host, hostname, port } = new URL(origin);
// const ENV = ['localhost', '127.0.0.1'].includes(hostname)? `dev` : `prod`;
// const SITE_URL = ENV === 'prod'? `${origin}/${LANGUAGE}/${VERSION}` : `http://${host}`;
// const env = hostname === 'syftbook.readthedocs.io'? `prod` : `dev`;
// const SITE_URL = hostname === ('localhost' || '127.0.0.1')? `http://${host}/docs/_build/html`: `${origin}/en/latest`;

// function buildNavigation() {
//   // build the href for the navigation tabs
//   const nodeList = document.querySelectorAll(".nav-item .nav-link.nav-internal");
//   const links = Array.from(nodeList);

//   // map href links
//   links.map( link => {
//     const { href } = link;
//     var { pathname } = new URL(href);
//     link.setAttribute("href", SITE_URL + pathname);
//     return link;
//   });

// };

// document.addEventListener("locationchange", buildNavigation);


// document.addEventListener("DOMContentLoaded", buildNavigation);
{/* <>
<script src="https://tracking.hotjar.com/script.js"></script>
<script></script>
<script>
  const { origin, pathname } = location;
  const { host, hostname, port } = new URL(origin);
  const ENV = ['localhost', '127.0.0.1'].includes(hostname)? `dev` : `prod`;
  console.log('ENV: ', ENV);
  hj = new Hotjar({
    siteID: "|env|YOUR_HOTJAR_SITE_ID|",
    isDevelopment: ENV === 'prod'? true : false, // Change to false for production
  });
</script>

</> */}

async function sendData() {
  const formData = new FormData(form);
  console.log("Server response:", formData);
  // Add additional data to the FormData if needed
  // Example: formData.append("additionalField", "someValue");

  // try {
  //     const response = await fetch("https://example.com/api", {
  //         method: "POST",
  //         body: formData, // Set the FormData instance as the request body
  //     });

  //     if (response.ok) {
  //         const data = await response.json();
  //         console.log("Server response:", data);
  //     } else {
  //         console.error("Error:", response.status);
  //     }
  // } catch (error) {
  //     console.error("Network error:", error);
  // }
}

const form = document.querySelector("#feedack");
form.addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent the default form submission
  sendData(); // Handle the form data
});
