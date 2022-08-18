function start()
{
    var buttonCalculeteIMC = document.querySelector('#button-IMC');
    buttonCalculeteIMC.addEventListener('click', handleButtonClick);

    var inputPeso = document.querySelector('#input-peso');
    var inputAltura = document.querySelector('#input-altura');

    inputPeso.addEventListener('input', handleButtonClick);
    inputAltura.addEventListener('input', handleButtonClick);

    handleButtonClick();
}

function calculateIMC(peso,altura)
{
    return peso / (altura * altura);
}

function handleButtonClick()
{
    var inputPeso = document.querySelector('#input-peso');
    var inputAltura = document.querySelector('#input-altura');
    var imcResult = document.querySelector('#imc-result');

    var Peso = Number(inputPeso.value);
    var Altura = Number(inputAltura.value);

    var imc = calculateIMC(Peso, Altura);
    var formattedIMC = imc.toFixed(2).replace('.',',');

    imcResult.textContent = formattedIMC;
}

start();