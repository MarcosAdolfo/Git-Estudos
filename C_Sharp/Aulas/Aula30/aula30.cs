using System;

namespace Aula30
{

    public class Jogador
    {
        public int energia;
        public bool vivo;
        public string nome;
        public Jogador()
        {
            energia = 100;
            vivo = true;
            nome = "Jogador";
        }
        public Jogador(string n)
        {
            energia = 100;
            vivo = true;
            nome = n;
        }
        public Jogador(string n,int e)
        {
            energia = e;
            vivo = true;
            nome = n;
        }
        public Jogador(string n,int e,bool v)
        {
            energia = e;
            vivo = v;
            nome = n;
        }
        public void info()
        {
            Console.WriteLine("Nome: {0}\nEnegia: {1}\nEstado: {2}\n",nome,energia,vivo);
        }
        ~Jogador()
        {
            Console.WriteLine("Jogado {0} Morto!!!",nome);
        }
    }

    class aula30
    {
        static void Main()
        {
            string nome1;
            Console.Write("Nome: ");
            nome1 = Console.ReadLine();

            Jogador j1 = new Jogador();
            Jogador j2 = new Jogador(nome1);
            Jogador j3 = new Jogador("Théoq",100);
            Jogador j4 = new Jogador("Arlanck",200,true);
            Jogador j5 = new Jogador("BreikVet",150,false);
            
            j1.info();
            j2.info();
            j3.info();
            j4.info();
            j5.info();
        }
    }

}