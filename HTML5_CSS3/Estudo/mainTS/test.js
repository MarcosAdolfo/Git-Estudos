//<p id="exibe"></p>
//<script>
var text = '{"trens":'
'[ + {"trem":"0145", "linha": "azul"}, '+
'{"trem":"0146", "linha": "vermelha"}, '+
'{"trem":"0147", "linha":"verde"} ] }';

x = JSON.parse(text);

console.log(x.trens[trem] + " " + x.trens[linha] );
//$("#exibe").html = ______;
