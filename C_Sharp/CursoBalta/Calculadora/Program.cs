// See https://aka.ms/new-console-template for more information
using System;

namespace Calculadora
{

    class Program
    {
        static void Main(string[] args)
        {
            Menu();
        }

        static void Menu()
        {
            Console.Clear();

            Console.WriteLine("Escolha um opção:");
            Console.WriteLine("1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n5 - Sair");

            Console.WriteLine("--------------------");

            Console.Write("Opção: ");
            short res = short.Parse(Console.ReadLine());

            switch(res)
            {
                //case 0:Soma();break;
                case 1:Soma();break;
                case 2:Subtracao();break;
                case 3:Divisao();break;
                case 4:Multiplicacao();break;
                case 5:Console.Clear(); System.Environment.Exit(0); break;
                default: Menu();break;
            }
        }

        static void Soma()
        {
            Console.Clear();

            Console.Write("Primeiro Valor: ");
            float v1 = float.Parse(Console.ReadLine());

            Console.Write("Segundo Valor: ");
            float v2 = float.Parse(Console.ReadLine());

            Console.WriteLine("");

            float total = v1 + v2;
            Console.WriteLine($"A soma de {v1} + {v2} = {total}");
            Console.ReadKey();
            Menu();
        }

        static void Subtracao()
        {
            Console.Clear();

            Console.Write("Primeiro Valor: ");
            float v1 = float.Parse(Console.ReadLine());

            Console.Write("Segundo Numero: ");
            float v2 = float.Parse(Console.ReadLine());

            Console.WriteLine("");

            float total = v1 - v2;
            Console.WriteLine($"A subitração de {v1} - {v2} = {total}");
            Console.ReadKey();
            Menu();
        }

        static void Divisao()
        {
            Console.Clear();

            Console.Write("Primeiro Valor: ");
            float v1 = float.Parse(Console.ReadLine());

            Console.Write("Segundo Numero: ");
            float v2 = float.Parse(Console.ReadLine());

            Console.WriteLine("");

            float total = v1 / v2;
            Console.WriteLine($"A Divisão de {v1} / {v2} = {total}");
            Console.ReadKey();
            Menu();
        }

        static void Multiplicacao()
        {
            Console.Clear();

            Console.Write("Primeiro Valor: ");
            float v1 = float.Parse(Console.ReadLine());

            Console.Write("Segundo Numero: ");
            float v2 = float.Parse(Console.ReadLine());

            Console.WriteLine("");

            float total = v1 * v2;
            Console.WriteLine($"A Multiplicação de {v1} * {v2} = {total}");
            Console.ReadKey();
            Menu();
        }
    }

}
