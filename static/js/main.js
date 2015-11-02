//TODO setup a mysql server to hold sec data
$(function(){
  fetchMedia = function(groupid, pos, stride){
    query = "/ajax/"+groupid+"/"+pos+"/"+stride;
    $.get(query, function(htmldata){
      $("#gallery").html(htmldata);
    })
  }
  updateStatus = function(groupid, pos, stride){
    $("#status").attr("data-groupid", groupid);
    $("#status").attr("data-pos", pos);
    $("#status").attr("data-stride", stride);
  }
  $("#leftarrow").click(function(){
    groupid = $("#status").attr("data-groupid");
    groupid=groupid-1;
    stride = $("#status").attr("data-stride");
    pos = $("#status").attr("data-pos") - stride;
    updateStatus(groupid, pos, stride);
    fetchMedia(groupid, pos, stride);
    return false;
  });
  $("#rightarrow").click(function(){
    groupid = parseInt($("#status").attr("data-groupid"));
    groupid=groupid+1;
    stride = parseInt($("#status").attr("data-stride"));
    pos = parseInt($("#status").attr("data-pos")) + stride;
    updateStatus(groupid, pos, stride);
    fetchMedia(groupid, pos, stride);
    return false;
  });
});
