function atjaunotIetvaru(which) {
  document.getElementById("lapas_saturs").innerHTML = '<'+'object id="lapas" type="text/html" data="'+which.href+'"></'+'object>';
}


window.onload = function() {
  zimetuzcanva();
    var navLinks = document.querySelectorAll('.topnav a');
    navLinks.forEach(function(link) {
      link.addEventListener('click', function() {
        navLinks.forEach(function(link) {
          link.classList.remove('active');
        });
        this.classList.add('active');
      });
    });
  }


function zimetuzcanva() {
  var kanva  = document.getElementById("zimejums");
  var konteksts = kanva.getContext("2d");
  konteksts.fillStyle = "blue";  
  konteksts.fillRect(20,20,150,100);
}

function taisnsturis() {
  var kanva  = document.getElementById("zimejums");
  var konteksts = kanva.getContext("2d");
  konteksts.strokeStyle = "red";
  konteksts.strokeRect(60,60,150,100);
}

function aplis() {
  var kanva  = document.getElementById("zimejums");
  var konteksts = kanva.getContext("2d");
  konteksts.beginPath();
  konteksts.arc(200,200,50,0,2*Math.PI);
  konteksts.lineWidth = 20;
  konteksts.fillStyle = "yellow";
  konteksts.strokeStyle = "pink";
  konteksts.fill();
  konteksts.stroke();
}

function linija() {
  var kanva  = document.getElementById("zimejums");
  var konteksts = kanva.getContext("2d");
  konteksts.beginPath();
  konteksts.moveTo(50,300);
  konteksts.lineTo(250,350);
  konteksts.lineWidth = 5;
  konteksts.strokeStyle = "green";
  konteksts.stroke();
}

function aprekins() {
  let vards = document.getElementById("vards").value;
  let pirmais = parseFloat(document.getElementById("a").value);
  let otrais = parseFloat(document.getElementById("b").value);
  if (!vards.match(/^\S[a-zA-Zā-žĀ-Ž\s]+$/)) {
    alert("Lūdzu ievadiet derīgu vārdu!"); 
      return;
  }
  
if (pirmais === "" || otrais === "" || isNaN(pirmais) || isNaN(otrais)){
  alert("Ievadi skaitli");
  return;
}
  
if (!Number. isInteger(pirmais) || !Number. isInteger(otrais)){
  alert("Ievadi veselu skaitli");
  return;
}
  
  let summa = pirmais * otrais;
  console.log("Tevi sauc: " + vards + " Atbilde ir:" + summa);
  document.getElementById("rezultats").innerHTML = "Tevi sauc: " + vards + "<br>Tu ievadīji a vērtību: " + pirmais + "<br> un otrā vērtība: "+ otrais +"<br><br> Atbilde ir:" + summa;}

