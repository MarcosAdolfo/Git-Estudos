var state = {board: [], currentGame: [], savedGame: []};

function start()
{
    readLocalStorage();
    createBoard();
    newGame();
}

function readLocalStorage()
{
    if(!window.localStorage)
    {
        return;
    }

    var saveGamesFromLocalStorage = window.localStorage.getItem('saved-games');

    if(saveGamesFromLocalStorage)
    {
        state.savedGame = JSON.parse(saveGamesFromLocalStorage);
    }
}

function writeToLocalStorage()
{
    window.localStorage.setItem('saved-games', JSON.stringify(state.savedGame));
}

function createBoard()
{
    state.board = [];

    for(var i = 1; i <= 60; i++)
    {
        state.board.push(i);
    }
}

function newGame()
{
    resetGame();
    render();
    renderButtons();
    renderSaveGame();

    console.log(state.currentGame);
}

function render()
{
    renderBoard();
    renderButtons();
    renderSaveGame();
}

function renderBoard()
{
    var divBoard = document.querySelector('#magasena-board');

    divBoard.innerHTML = '';

    var ulNumbers = document.createElement('ul');
    ulNumbers.classList.add('numbers');

    for(var i = 0; i < state.board.length; i++)
    {
        var correntNumber = state.board[i]

        var liNumber = document.createElement('li');
        liNumber.textContent = correntNumber;
        liNumber.classList.add('number');

        liNumber.addEventListener('click', handleNumberClick);

        if(isNumberInGame(correntNumber))
        {
            liNumber.classList.add('selected-number');
        }

        ulNumbers.appendChild(liNumber);
    }

    divBoard.appendChild(ulNumbers);
}

function handleNumberClick(event)
{
    var value = Number(event.currentTarget.textContent);

    if(isNumberInGame(value))
    {
        removeNumberFromGame(value);
    }else
    {
        addNumberToGame(value);
    }
    console.log(state.currentGame);
    render();
}

function renderButtons()
{
    var divButton = document.querySelector('#megasena-buttons');
    divButton.innerHTML = '';

    var buttonNewGame = createNewGameButton();
    var buttonRandomGame = createRandomGameButton();
    var buttonSaveGame = createSaveGameButton();

    divButton.appendChild(buttonNewGame);
    divButton.appendChild(buttonRandomGame);
    divButton.appendChild(buttonSaveGame);
}

function createNewGameButton()
{
    var button = document.createElement('button');
    button.textContent = 'Novo Jogo';

    button.addEventListener('click',newGame);
    return button;
}

function createRandomGameButton()
{
    var button = document.createElement('button');
    button.textContent = 'Jogo Aleatorio';

    button.addEventListener('click',randomGame);
    return button;
}

function createSaveGameButton()
{
    var button = document.createElement('button');
    button.textContent = 'Salvar Jogo';
    button.disabled = !isGameComplete();

    button.addEventListener('click',saveGame);
    return button;
}

function renderSaveGame()
{
    var divSavedGames = document.querySelector('#megasena-saved-games');

    divSavedGames.innerHTML = '';

    if(state.savedGame.length === 0)
    {
        divSavedGames.innerHTML = '<p>Nem um Jogo Salvo</p>';
    }else
    {
        var ulSaveGames = document.createElement('ul');

        for(var i = 0; i < state.savedGame.length; i++)
        {
            var currentGame = state.savedGame[i];

            var liGame = document.createElement('li');
            
            liGame.textContent = currentGame.join(', ');

            ulSaveGames.appendChild(liGame);
        }

        divSavedGames.appendChild(ulSaveGames);
    }
}

function addNumberToGame(numberToADD)
{
    if(numberToADD < 1 || numberToADD > 60)
    {
        console.error('Numero Invalido', numberToADD);
        return;
    }
    if(state.currentGame.length >= 6)
    {
        console.error('O jogo ja esta completo!');
        return;
    }
    if(isNumberInGame(numberToADD))
    {
        console.error('Este Numero ja Esta no Jogo!', numberToADD);
        return;
    }
    state.currentGame.push(numberToADD);
}

function removeNumberFromGame(numberToRemove)
{
    if(numberToRemove < 1 || numberToRemove > 60)
    {
        console.error('Numero Invalido', numberToRemove);
        return;
    }
    
    var newGame = [];

    for(var i = 0; i < state.currentGame.length; i++)
    {
        var currentGame = state.currentGame[i];

        if(currentGame === numberToRemove)
        {
            continue;
        }
        newGame.push(currentGame);
    }
    state.currentGame = newGame;
}

function isNumberInGame(numberToCheck)
{
    return state.currentGame.includes(numberToCheck);
}

function saveGame()
{
    if(!isGameComplete())
    {
        console.error('O jogo não esta completo!');
        return;
    }

    state.savedGame.push(state.currentGame);
    writeToLocalStorage();
    newGame();

    console.log(state.savedGame);
}

function isGameComplete()
{
    return state.currentGame.length === 6;
}

function resetGame()
{
    state.currentGame = [];
}

function randomGame()
{
    resetGame();

    while(!isGameComplete())
    {
       var randoNumeber = Math.ceil(Math.random() * 60);
       addNumberToGame(randoNumeber);
    }
    
    console.log(state.currentGame);
    render();
}

start();