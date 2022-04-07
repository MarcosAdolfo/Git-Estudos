using System;

namespace Aula34
{

    class Veiculo
    {
        public int rodas;
        public int velMax;
        private bool ligado;

        public void ligar()
        {
            ligado = true;
        }
        public void desligar()
        {
            ligado = false;
        }
        public string getLigado()
        {
            if(ligado)
            {
                return "Sim";
            }
            else
            {
                return "Não";
            }
        }
    }

    class Carro:Veiculo
    {
        public string nome;
        public string cor;
        public Carro(string nome, string cor)
        {
            desligar();
            rodas = 4;
            velMax = 120;
            this.nome = nome;
            this.cor = cor;
        }
    }

    class aula34
    {
        static void Main()
        {
            Carro c1 = new Carro("Vecto","Preto");

            Console.WriteLine("Cor: {0}\nNome: {1}\nRodas: {2}\nVel.Maxima: {3}\nLigado: {4}",c1.cor,c1.nome,c1.rodas,c1.velMax,c1.getLigado());
        }
    }

}