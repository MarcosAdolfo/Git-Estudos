using System;

namespace Aula43
{

    public interface Veiculo
    {
        void liga();
        void desligar();
        void info();
    }

    public interface Combate
    {
        void disparar();
    }

    class Carro:Veiculo,Combate
    {
        public bool ligado;
        private int municao;

        public Carro()
        {
            setMunicao(100);
        }

        public void setMunicao(int qtdr)
        {
            this.municao = qtdr;
        }
        public void liga()
        {
            this.ligado = true;
        }
        public void desligar()
        {
            this.ligado = false;
        }
        public void disparar()
        {

        }
        public void info()
        {

        }
    }

    class aula43
    {
        static void Main()
        {
            Carro c1 = new Carro();
        }
    }

}