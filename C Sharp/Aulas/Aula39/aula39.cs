using System;

namespace Aula39
{

    abstract class Veiculo
    {
        protected int velMaxima;
        protected int velAtual;
        protected bool ligado;

        public Veiculo()
        {
            ligado = false;
            velAtual = 0;
        }

        public void setLigado(bool ligado)
        {
            this.ligado = ligado;
        }
        public bool getLigado()  // nova
        {
            return this.ligado;
        }
        public int getVelAtual()
        {
            return velAtual;
        }
        
        abstract public void aceleracao(int mult);
    }

    class Carro:Veiculo
    {
        public Carro()
        {
            velMaxima=120;
        }
        override public void aceleracao(int mult)
        {
            velAtual+=10*mult;
        }
    }

    class aula39
    {
        static void Main()
        {
            Carro carro1 = new Carro();
            carro1.aceleracao(2);
            Console.WriteLine(carro1.getVelAtual());
            Console.WriteLine("Ligado:{0}", carro1.getLigado());

            //ts
            Carro carro2 = new Carro();
            carro2.aceleracao(5);
            Console.WriteLine(carro2.getVelAtual());
            carro2.setLigado(true);
            Console.WriteLine("Ligado:{0}", carro2.getLigado());
        }
    }

}