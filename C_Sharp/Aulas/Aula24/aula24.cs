using System;

namespace Aula24
{

    class aula24
    {
        static void Main()
        {
            int v1,v2,r;

            ola();

            for(int i = 0; i < 5; i++)
            {
                ola();
            }

            v1 = int.Parse(Console.ReadLine());
            v2 = Convert.ToInt32(Console.ReadLine());
            soma(v1,v2);
            r = mutiplicacao(v1,v2);
            Console.WriteLine("A mutiplicação é: {0}",r);
        }

        static void ola()
        {
            Console.WriteLine("Olá Mundo");
        }

        static void soma(int n1, int n2)
        {
            int res = n1 + n2;
            Console.WriteLine("A soma de {0} e {1} é: {2}",n1,n2,res);
        }

        static int mutiplicacao(int n1, int n2)
        {
            int res = n1 * n2;
            return res;
        }
    }

}