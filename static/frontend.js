document.addEventListener('DOMContentLoaded', function() {
    var analyzeButton = document.getElementById('analyzeButton');
    analyzeButton.addEventListener('click', analyzeCompany);
});

function analyzeCompany() {
    var companyName = document.getElementById("companyName").value;
    var analysisType = document.getElementById("analysisType").value;
    var resultElement = document.getElementById("analysisResult");

    resultElement.innerHTML = "Loading...";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/analyze", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            resultElement.innerHTML = ''; // Clear previous content
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                var formattedResult = convertUrlsToLinks(response.result);
                resultElement.innerHTML = formattedResult;
            } else {
                resultElement.innerHTML = "Error: Could not analyze company. Status code: " + xhr.status;
            }
        }
    };

    var data = JSON.stringify({
        "company": companyName,
        "type": analysisType
    });

    xhr.send(data);
}

function convertUrlsToLinks(text) {
    var urlRegex = /(https?:\/\/[^\s\)]+)/g;
    return text.replace(urlRegex, function(url) {
        // Attempt to decode the URL, then remove trailing characters
        try {
            url = decodeURIComponent(url).replace(/[)\]]+$/, '');
        } catch (e) {
            console.error('Error decoding URL:', e);
        }
        // Return the anchor tag with the corrected URL
        return '<a href="' + url + '" target="_blank">' + url + '</a>';
    });
}