var time=3000; 
var wid=565;
var n=0;
setInterval(changeImg,time);
function changeImg(){
	n = n+1;
	if(n==5){
		n=0;
		var w = "-" + wid*n + "px";
		$("#scroll").css("left",w);
		$(".on").removeClass("on");
		var obj = "#i"+n;
		$(obj).addClass("on");
	}else{
		var w = "-" + wid*n + "px";
		$("#scroll").css("left",w);
		$(".on").removeClass("on");
		var obj = "#i"+n;
		$(obj).addClass("on");
	}
} 
$(window).ready(function(){
	$("#i0").click(function(){
		$("#scroll").css("left","0px");
		$(".on").removeClass("on");
		$("#i0").addClass("on");
	});
	$("#i1").click(function(){
		$("#scroll").css("left","-565px");
		$(".on").removeClass("on");
		$("#i1").addClass("on");
	});
	$("#i2").click(function(){
		$("#scroll").css("left","-1130px");
		$(".on").removeClass("on");
		$("#i2").addClass("on");
	});
	$("#i3").click(function(){
		$("#scroll").css("left","-1695px");
		$(".on").removeClass("on");
		$("#i3").addClass("on");
	});
	$("#i4").click(function(){
		$("#scroll").css("left","-2260px");
		$(".on").removeClass("on");
		$("#i4").addClass("on");
	});
});