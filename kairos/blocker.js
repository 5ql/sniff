chrome.storage.sync.get("blockedSites", function (data) {
  var blockedSites = data.blockedSites || [];
  chrome.webRequest.onBeforeRequest.addListener(
    function (details) {
      for (var i = 0; i < blockedSites.length; i++) {
        if (details.url.indexOf(blockedSites[i]) !== -1) {
          return { cancel: true };
        }
      }
    },
    { urls: ["<all_urls>"] },
    ["blocking"]
  );
});
