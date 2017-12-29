$(document).ready(function(){
    jQuery(".tm-input").tagsManager();
});

function copy() {
  var copyText = document.getElementById("url");
  copyText.select();
  document.execCommand("Copy");
}
