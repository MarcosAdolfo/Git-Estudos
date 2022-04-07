using System;

namespace Aula35
{

    class Veiculo
    {
        private int rodas;
        public int velMax;
        private bool ligado;

        public Veiculo(int rodas)
        {
            this.rodas = rodas;
        }

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
            return (ligado?"Sim":"Não");
        }
        public int getRodas()
        {
            return rodas;
        }
        public void setRodas(int rodas)
        {
            if(rodas<0)
            {
                this.rodas = 0;
            }
            else if(rodas>40)
            {
                this.rodas = 40;
            }
            else{this.rodas = rodas;}
        }
    }

    class Carro:Veiculo
    {
        public string nome;
        public string cor;
        public Carro(string nome, string cor):base(4)
        {
            desligar();
            velMax = 120;
            this.nome = nome;
            this.cor = cor;
        }
    }

    class CarroCombate:Carro
    {
        public int municao;
        public CarroCombate():base("Trit","Verde")
        {
            municao = 100;
            setRodas(6);
        }
    }

    class aula35
    {
        static void Main()
        {
            Carro c1 = new Carro("Vecto","Preto");
            CarroCombate cc1 = new CarroCombate();

            c1.ligar();

            Console.WriteLine("Cor: {0}\nNome: {1}\nRodas: {2}\nVel.Maxima: {3}\nLigado: {4}",c1.cor,c1.nome,c1.getRodas(),c1.velMax,c1.getLigado());
            Console.WriteLine("Cor: {0}\nNome: {1}\nRodas: {2}\nVel.Maxima: {3}\nLigado: {4}\nMunição: {5}",cc1.cor,cc1.nome,cc1.getRodas(),cc1.velMax,cc1.getLigado(),cc1.municao);
        }
    }

}