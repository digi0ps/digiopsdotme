//Fix for Navigation Animation in Android Chromes

if (navigator.userAgent.match(/Android/i)){
	function hexy(){
		colors = ["#4CAF50", "#03A9F4", "#9C27B0", "#FF9800", "#F44336", "#4CAF50"];
		return colors[Math.floor(Math.random() * 7)];
		}
	setInterval(function(){
		$(".navbar-static-top")[0].style.backgroundColor = hexy();
	}, 3000);
}

//Heart pulsating effect 
$(function(){
setInterval(function(){
	$("#heart").fadeOut(1000).fadeIn(1000);
}, 2000);
});