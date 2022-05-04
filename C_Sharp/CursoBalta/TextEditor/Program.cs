using System;

namespace TextEditor
{

    class Program
    {
        static void Main()
        {
            Menu();
        }

        static void Menu()
        {
            Console.Clear();
            Console.WriteLine("Oque você deseja faze?");
            Console.WriteLine("0 - Sair\n1 - Abrir Arquivo\n2 - Criar Novo Arquivo");
            short option = short.Parse(Console.ReadLine());

            switch (option)
            {
                case 0: System.Environment.Exit(0); break;
                case 1: Abrir(); break;
                case 2: Criar(); break;
                default: Menu(); break;
            }
        }

        static void Abrir(){}

        static void Criar(){}
    }

}