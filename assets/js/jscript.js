



   
$(document).ready(function(){
	
		// for employee filter
  $("#employeeSearch").on("keyup", function() {
    var value = $(this).val().toLowerCase(), allhidden=false;
    $("._t_r.tr_patt").filter(function(i) {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
	  console.log(i);
    })
	$("._t_r.tr_patt").each(function(e){
		if(this.style.display != "none" ) {allhidden=false}
		else {allhidden = true}
		
		
	});
	
	
	if(allhidden){
		$("#table_msg_below").html("SNAP! No Record Found For Current Filter")
	}
	else{
		$("#table_msg_below").html("")
	}

  });
  // for add new employee form
  $(".form-field").each(function(){
		if($(this).children("input").prop('required')){
			$(this).children("label").append("*").css("font-weight","bold")
		}
	})
		// for filter
  $(".chosen-select").chosen({width: "200px"});
  
  
  // for profile btn -	> .pmenu-item
  
  $("").click(function(e){
	  e.preventDefault();
	  var a = $(this).prop("classList")[1];
	  $(".section-basi").addClass("hidden");
	  $("#"+a).removeClass("hidden");
	  
	  $(".pmenu-item").removeClass("b-selected");
	  $(this).addClass("b-selected");
	  
  })
  
  
  
  
  
  
  
});




var erp = {
	ur:{
		ip:"https://api.ipify.org?format=json",
		log:"http://127.0.0.1:8000/register/json/ua_empl"
	},
	o: {}, // initial object
	btn:{},
	ini: function(){ //initiate required script for page
		a=this;
		a.jax("json",{},"get",a.ur.ip,function(e){a.o.ip=e.ip; console.log("Device IP : "+e.ip);});	
		a.jax("json",{"u":a.o.b,"c":a.o.c},"get",a.ur.log,
				
				function(e){
					
					var d = JSON.parse(e.response)
					console.log("Settings Recieved...")
					a.html($("#sigmaBdy"),d,"new_reg");
					
					});
	},
    a: function () { // 
		o = this;
		$(".__register__").on("click",o.pop("","abc",
			function(p){
				
				o.append($('body'),$('<div class="modal-pop">hi</div>'));
				console.log('hey');
				
			},
			function(p){
				
				
			}
		))
    },

    b: function () {
 
    },

    c: function (cb) {
       
    },

    firstResponse: function (a,b,c,d,e,msg,f,t=this) { // render the first response to the app about features.
	
		f(a,b,c,d,e,t);
		console.log(msg);
    },
	myObject:function(a,msg,f,t=this){
			
		f(a,t);
		//console.log(msg,"// Hide me in deployment //");
	},
	jax:function(t,d,m,u,rfn,efn){
		$.ajax({
			dataType:t,data:d,
			method:m,
			url:u,
			success: function(e){return rfn(e)},
			error:function(e){return efn(e)}
			})
		},
	html:function(par,d,cond){
		
		if(cond=="new_reg"){
			var h='',l=d.length;
			for(var i=0;i<l;i++){ 
				h=h+'<tr class="data-tr-tow _t_r tr_patt">'+
						'<td class="td-cell">'+ (i+1) +'</td>'+
						'<td class="td-cell">'+ d[i].pk +'</td>'+
						'<td class="td-cell ename">'+ d[i].fields.First_name +'</td>'+
						'<td class="td-cell">'+d[i].Father_name+'</td>'+
						'<td class="td-cell">'+
							'<input id="'+ d[i].pk +'" class="yesbox" type="checkbox"/>'+
							'<button class="select-btn">Select</button>'+
						'</td>'+
					'</tr>';
					
			}
			
		}
		else{
			par.html(d);
		}
		
		
		
	},
	append:function(par,d,cond){
		console.log(d,par);
		par.append(d);
		
		
	},
	pop:function(d,p,fnopen,fnclose){
			
			fnopen(p);
			fnclose(p);
			
	},
	formValidate:function(a,b,msg,fn,t=this){
		fn(a,b,t);
	},
	formPop:function(el,b,msg){
		var f = el.find("form");
		f.each(function(){
			fld = $(this).find("input,select,textarea,radio")
			fld.each(function(){
				if((this.tagName== "INPUT") && (this.value != this.defaultValue)) alert("#name has changed");
			});
			console.log(fld)
		});
		
	},	
	kill:function(e){
		e.remove();
	},
	del:function(e){
		e={}
	},
	jxerr:function(e,p){
		var err = function(e){
			switch(e.status){
				case 0: return {code:"ERR_0 NET_CONNECTION_ERR",text:"Internet connection is lost."};
					break;
				case 403: return {code:"ERR_403 ACCESS_FORBIDDEN",text:"This is an unauthorized request or something is missing."};
					break;
				case 404: return {code:"ERR_404 REQST_NOT_FOUND",text:"This request is unavailable right now."};
					break;
				case 500: return {code:"ERR_500 INTERNAL_ERROR",text:"Something is wrong with server."};
					break;
				case 503: return {code:"ERR_503 SERVICE_ERROR",text:"This services is unavailable."};
					break;
				default: return {code:"Unknown ERROR",text:"There was an error. Please try again."};
			}
		}
		var eo = err(e)
		this.html(p,'<div class="errcd1">'+ eo.code +"! "+ eo.text +'</div>')
	},
	lastResponse(){
		
		$('a').each(function(){
			var l = window.location.hash;
			if($(this).attr('href')==l) $(this).click();
			if($(this).hasClass("nohash")) $(this).on("click",function(e){e.preventDefault();})
		});
		
	},
	reRunJs(){
		$('a').each(function(){
			
			if($(this).hasClass("nohash")) $(this).on("click",function(e){e.preventDefault();})	
		});
	},
	loadthis(e,fn){
		fn(e);
	},
	tableFilter(s,filter,msgBefore,msg){
		var el = $('<div class="gomsg">'+msg+'</div>')
		
		s.on("keyup", function() {
			//console.log(new Date().getTime());
			var value = $(this).val().toLowerCase(), allhidden=true;
			filter.find('tr').filter(function(i) {
			  $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
			})
			filter.find('tr').each(function(e){
				if(this.style.display != "none" ) {allhidden=false}
				
				
				
			});
			
			
			if(allhidden){
				el.insertAfter(msgBefore)
			}
			else{
				el.remove();	
			}
			//console.log(new Date().getTime());
		  });
	},
	tpl:{
		
		l:'<div class="loader"></div>'
		
	}
	
	
};

$(document).ready(function(){
	
erp.firstResponse("csrftoken","userid","userhash",new Date(),window.navigator,"ERP Initialized...",function(a,b,c,d,e,t){t.o={a:a,b:b,c:c,d:d,e:e};});
erp.ini();
erp.myObject({"a":"b"},'Emp code object created ...',function(a,t){t.o.emp_code_status=a});
erp.myObject({},'Testing ...',function(a,t){t.o.testObject=a});
erp.myObject($("#dep-sel"),'Button Code s1',function(b,t){	
														t.btn.s1=b;
														t.btn.s1.on('change',function(e){
														$("#id_Department").val($("#dep-sel").val())
														}).trigger("change");
													
													});
												
												
												
									
erp.lastResponse();





});



/**  

In MEthODS /funtions/

**/

function logError(){
	
	var v=$("input[name='next']").val();
	console.log(v,"<---");
	if(v!=''){
		var pop1 = $("#username_pop");
		$(".inhead_logger_input").css({'border-color':'red'});
		pop1.children(".msg").html("You need to login first!")
		pop1.show();
		pop1.on("mouseout",function(){ pop1.fadeOut(1000);})
		setInterval(function(){ pop1.fadeOut(1000);}, 10000);
		
		
	}
	
}

