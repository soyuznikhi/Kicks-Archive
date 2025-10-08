let activeRequests = 0;

function showLoader() {
const loader = document.getElementById("global-loader");
loader.classList.remove("hidden");
loader.classList.add("opacity-100");
}

function hideLoader() {
const loader = document.getElementById("global-loader");
loader.classList.add("hidden");
loader.classList.remove("opacity-100");
}

async function globalFetch(url, options = {}) {
activeRequests++;
if (activeRequests === 1) showLoader(); // show loader if first request

try {
    const response = await fetch(url, options);
    return response;
} catch (err) {
    console.error("AJAX error:", err);
    throw err;
} finally {
    activeRequests--;
    if (activeRequests === 0) hideLoader(); // hide loader when no more requests
}
}
