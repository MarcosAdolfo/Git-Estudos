using System;

namespace Aula28
{

    public class Jogador
    {
        public int energia;
        bool vivo = true;


    }

    class aula28
    {
        static void Main()
        {
            Jogador j1 = new Jogador();
            Jogador j2 = new Jogador();
            
            j1.energia = 50;
            Console.WriteLine("Enegia do jogado 1: {0}",j1.energia);
            Console.WriteLine("Enegia do jogado 2: {0}",j2.energia);
        }
    }

}