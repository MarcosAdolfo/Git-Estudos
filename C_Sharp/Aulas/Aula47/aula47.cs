using System;

namespace Aula47
{

    class Calc
    {
        public int soma(params int[]n)
        {
            int s = 0;

            for(int i = 0; i < n.Length; i++)
            {
                s += n[i];
            }

            return s;
        }

        public double soma(params double[]n)
        {
            double s = 0;

            for(int i=0; i < n.Length; i++)
            {
                s += n[i];
            }
            return s;
        }
    }

    class aula47
    {
        static void Main()
        {
            Calc calc = new Calc();
            var res = calc.soma(10.5,5,10,5.5);

            Console.WriteLine(res);
        }
    }

}