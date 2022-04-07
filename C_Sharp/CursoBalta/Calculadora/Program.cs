// See https://aka.ms/new-console-template for more information
using System;

namespace Calculadora
{

    class Program
    {
        static void Main(string[] args)
        {
            // Soma();
            Subitracao();
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
        }

        static void Subitracao()
        {
            Console.Clear();

            Console.Write("Primeiro Valor: ");
            float v1 = float.Parse(Console.ReadLine());

            Console.Write("Segundo Numero: ");
            float v2 = float.Parse(Console.ReadLine());

            Console.WriteLine("");

            float total = v1 - v2;
            Console.WriteLine($"A subitração de {v1} - {v2} = {total}");
        }
    }

}
