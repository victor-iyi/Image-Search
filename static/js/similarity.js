$(function(){
  $("#most-similar").bind("click", function() {
    $.getJSON("/_similarity", {
      action: "most_similar",
      word1: $("input[name=word-1]").val(),
      word2: $("input[name=word-2]").val(),
      word3: $("input[name=word-3]").val()
    }, function(data) {
      $("#most-similar").attr("value", data.result);
    });
    return false;
  });
});

$(function(){
  $("#similar-by-word").bind("click", function() {
    $.getJSON("/_similarity", {
      action: "similarity_by_word",
      word: $("input[name=word]").val()
    }, function(data) {
      $("#similar-by-word").attr("value", data.result);
    });
    return false;
  });
});

$(function(){
  $("#doesnt-match").bind("click", function() {
    $.getJSON("/_similarity", {
      action: "doesnt_match",
      phrase: $("input[name=phrase]").val()
    }, function(data) {
      $("#doesnt-match").attr("value", data.result);
    });
    return false;
  });
});