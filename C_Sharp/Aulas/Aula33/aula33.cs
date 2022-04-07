using System;

namespace Aula33
{

    class Jogador
    {
        private int energia;
        private string nome;

        public Jogador(string nome)
        {
            this.nome = nome;
            energia = 100;
        }

        public int getEnergia()
        {
            return energia;
        }
        public string getNome()
        {
            return nome;
        }

        public void setEnergia(int e)
        {
            if(e<0)
            {
                if(energia+e < 0)
                {
                    energia = 0;
                }else{energia += e;}
            }

            else if(e>0)
            {
                if(energia+e > 100)
                {
                    energia = 100;
                }else{energia += e;}
            }
        }
    }

    class aula33
    {
        static void Main()
        {
            Jogador j1 = new Jogador("Trier");
            
            j1.setEnergia(-150);
            j1.setEnergia(50);

            Console.WriteLine("Nome: {0}\nEnergia: {1}",j1.getNome(),j1.getEnergia());
        }
    }

}