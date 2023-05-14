chrome.storage.sync.get('blockList', function(data) {
  if (data.blockList) {
    document.querySelector('#block-list').value = data.blockList.join('\n');
  }
});


document.querySelector('#save-btn').addEventListener('click', function() {
  var blockList = document.querySelector('#block-list').value.split('\n');
  blockList = blockList.map(function(url) {
    return url.trim();
  }).filter(function(url) {
    return url !== '';
  });
  chrome.storage.sync.set({blockList: blockList}, function() {
    alert('Block list saved!');
  });
});
