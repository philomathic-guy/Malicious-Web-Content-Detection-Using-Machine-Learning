function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		//alert(tablink);
		$("#p1").text("The URL being tested is - "+tablink);

	var xhr=new XMLHttpRequest();
	//alert("hii");
	//var tablink='';	
	//var safe = document.URL;
	params="url="+tablink;
	alert(params);
	var markup = "url="+tablink+"&html="+document.documentElement.innerHTML;
	xhr.open("POST","http://localhost/BE/clientServer.php",false);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xhr.send(markup);
	alert(xhr.responseText);
	$("#div1").text(xhr.responseText);	
	return xhr.responseText;
	/*if(xhr.responseText==6)
	{
		return "safe";
	}
	return "nooooo";*/
	});
}


$(document).ready(function(){
    $("button").click(function(){	
	var val = transfer();
//	$("#p1").text(val);
        });
});

chrome.tabs.getSelected(null,function(tab) {
   	var tablink = tab.url;
	$("#p1").text("The URL being tested is - "+tablink);

});
