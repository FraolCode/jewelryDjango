$(document).ready(function () {		if ($.cookie(cookie_name) != "true" && $('body').outerWidth() > 979) {		//alert(cookie_name);$("#orthoPopupnewsletter").modal({show: true});		$(".send-reqest").click(function(){			var email = $("#otnewsletter-input").val();			$.ajax({				type: "POST",				headers: { "cache-control": "no-cache" },				async: false,				url: field_path,				data: "name=dixit&email="+email,				success: function(data) {					if (data)						$(".labAlert").text(data);				}			});		});		$('#otnewsletter-input').keypress(function(event){		  var keycode = (event.keyCode ? event.keyCode : event.which);		  if (keycode == '13') {					var email = $("#otnewsletter-input").val();					$.ajax({						type: "POST",						headers: { "cache-control": "no-cache" },						async: false,						url: field_path,						data: "name=dixit&email="+email,						success: function(data) {							if (data)								$(".labAlert").text(data);						}					});					event.preventDefault();		  }		});                $("#ortho_newsletter_dont_show_again").prop("checked") == false;	}			$('#ortho_newsletter_dont_show_again').change(function(){	    if($(this).is(':checked')){		$.cookie(cookie_name, "true");	//	console.log($.cookie(cookie_name, "true"));	    }else{		$.cookie(cookie_name, "false");	//	console.log($.cookie(cookie_name, "false"));	    }	});});