using System;

namespace Aula31
{

    static public class Jogador
    {
        static public int energia;
        static public bool vivo;
        static public string nome;
        
        static public void iniciar()
        {
            energia = 100;
            vivo = true;
            nome = "Jogador";
        }
        static public void iniciar(string n)
        {
            energia = 100;
            vivo = true;
            nome = n;
        }
        static public void info()
        {
            Console.WriteLine("Nome: {0}\nEnegia: {1}\nEstado: {2}\n",nome,energia,vivo);
        }
    }


    class Inimigo
    {
        static public bool alerta;
        public string nome;

        public Inimigo(string n)
        {
            alerta = false;
            nome = n;
        }
        public void info()
        {
            Console.WriteLine(nome);
            Console.WriteLine(alerta);
            Console.WriteLine("--------");
        }
    }


    class aula31
    {
        static void Main()
        {
            string nome1;
            Console.Write("Nome: ");
            nome1 = Console.ReadLine();

            Jogador.iniciar(nome1);
            Jogador.info();

            Inimigo i1 = new Inimigo("Crack");
            Inimigo i2 = new Inimigo("Slim");
            Inimigo i3 = new Inimigo("BleckTw");

            Inimigo.alerta = true;
            
            i1.info();
            i2.info();
            i3.info();
        }
    }

}