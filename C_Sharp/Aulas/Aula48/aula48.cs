using System;

namespace Aula48
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

        public int fat(int n)
        {
            int res = 0;
            if(n <= 1)
            {
                res = 1;
            }
            else
            {
                res = n * fat(n-1);
            }
            return res;
        }
    }

    class aula48
    {
        static void Main()
        {
            Calc calc = new Calc();
            var res = calc.soma(10.5,5,10,5.5);
            int fato = calc.fat(10);

            Console.WriteLine("{0}\n{1}",res,fato);
        }
    }

}