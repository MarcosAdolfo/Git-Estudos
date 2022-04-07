using System;

namespace Aula36
{

    class Veiculo
    {
        public int velAtual;
        private int velMax;
        protected bool ligado;

        public Veiculo(int velMax)
        {
            velAtual = 0;
            this.velMax = velMax;
            ligado = false;
        }
        public bool getLigado()
        {
            return ligado;
        }
        public int getVelMax()
        {
            return velMax;
        }
    }

    class Carro:Veiculo
    {
        public string nome;

        public Carro(string nome, int vm):base(vm)
        {
            this.nome = nome;
            ligado = true;
        }
    }

    class aula36
    {
        static void Main()
        {
            Carro carro = new Carro("Chevete",375);
            Console.WriteLine("Nome........: {0}",carro.nome);
            Console.WriteLine("Vel.Maxima..: {0}",carro.getVelMax());
            Console.WriteLine("Ligado......: {0}",carro.getLigado());
        }
    }

}