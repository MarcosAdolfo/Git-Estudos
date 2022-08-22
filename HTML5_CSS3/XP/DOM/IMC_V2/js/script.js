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

function faixaIMC(imc)
{
    if(imc >=16 && imc < 17)
        return "Muito a baixo do peso!";
    else if(imc >= 17 && imc < 18.5)
        return "Abaixo do peso!";
    else if(imc >= 18.5 && imc < 25)
        return "Peso Normal!";
    else if(imc >= 25 && imc < 30)
        return "Acima do peso!";
    else if(imc >= 30 && imc < 35)
        return "Obesidade grau I !";
    else if(imc >= 35 && imc <= 40)
        return "Obesidade grau II !";
    else if(imc > 40)
        return "Obesidade grau III !";
    else
        return "Valor invalido!";
}

function handleButtonClick()
{
    var inputPeso = document.querySelector('#input-peso');
    var inputAltura = document.querySelector('#input-altura');
    var imcResult = document.querySelector('#imc-result');
    var imcFaixa = document.querySelector('#imc-faixa');

    var Peso = Number(inputPeso.value);
    var Altura = Number(inputAltura.value);

    var imc = calculateIMC(Peso, Altura);
    var faixa = faixaIMC(imc);
    var formattedIMC = imc.toFixed(2).replace('.',',');

    imcResult.textContent = formattedIMC;
    imcFaixa.textContent = faixa;
}

start();