$(window).ready(function(){
	$("#c_left").mouseleave(function(){
		$("#fast_b").css("display","none");
	});
	$("#c_left").mouseover(function(){
		$("#fast_b").css("display","block");
	});
})
var time=3000; 
var m=1;
setInterval(changeImg,time);
function changeImg(){
	m = m+1;
	if(m==5){
		m=1;
		var obj = "#a"+m;
		$(obj).fadeIn(1500);
		m = 4;
		var obj1 = "#a"+m;
		$(obj1).fadeOut(1500);
		m=1;
	}else{
		var obj = "#a"+m;
		$(obj).fadeIn(1500);
		var c=m-1;
		var obj1 = "#a"+c;
		$(obj1).fadeOut(1500);
	}
} 