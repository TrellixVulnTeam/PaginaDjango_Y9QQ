function fecha(){
	var dt = new Date();
	var mes = dt.getMonth()+1;
    var dia = dt.getDate();
    var anio = dt.getFullYear();
    alert('Fecha de hoy: '+mes + '-' + dia + '-' + anio);
}
function menu(){
	document.getElementById("menu").style.display="none";
	document.getElementById("abajo").style.display="inline";
}
function aparece(){
	document.getElementById("menu").style.display="block";
	document.getElementById("abajo").style.display="none";
}