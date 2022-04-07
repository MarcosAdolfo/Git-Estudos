using System;

namespace Aula37
{

    class Base
    {
        public Base()
        {
            Console.WriteLine("Construto da class Base");
        }
    }

    class Derivada1:Base
    {
        public Derivada1()
        {
            Console.WriteLine("Construto da class Derivada 1");
        }
    }

    class Derivada2:Derivada1
    {
        public Derivada2()
        {
            Console.WriteLine("Construto da class Derivada 2");
        }
    }

    class aula37
    {
        static void Main()
        {
            Derivada2 derivada2 = new Derivada2();
        }
    }

}