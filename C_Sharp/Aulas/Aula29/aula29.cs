using System;

namespace Aula29
{

    public class Jogador
    {
        public int energia;
        public bool vivo;
        public string nome;
        public Jogador(string n)
        {
            energia = 100;
            vivo = true;
            nome = n;
        }
        ~Jogador()
        {
            Console.WriteLine("Jogado {0} Morto!!!",nome);
        }
    }

    class aula29
    {
        static void Main()
        {
            string nome1;
            Console.Write("Nome: ");
            nome1 = Console.ReadLine();

            Jogador j1 = new Jogador(nome1);
            Jogador j2 = new Jogador("Théoq");
            
            j1.energia = 50;
            Console.WriteLine("Nome do jogado 1: {0}",j1.nome);
            Console.WriteLine("Nome do jogado 2: {0}",j2.nome);
        }
    }

}