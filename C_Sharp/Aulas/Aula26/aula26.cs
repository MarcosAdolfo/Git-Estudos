using System;

namespace Aula26
{

    class aula26
    {
        static void Main()
        {
            int divid,divis,quoc,rest;
            divid = 10;
            divis = 5;
            quoc = divide(divid,divis, out rest);

            Console.WriteLine("{0}/{1}:quociente = {2} e resto = {3}",divid,divis,quoc,rest);
        }

        static int divide(int dividendo, int divisor, out int resto)
        {
            int quotient;
            quotient = dividendo / divisor;
            resto = dividendo % divisor;
            return quotient;
        }
    }

}