using System;

namespace Aula49
{

    class Mat
    {
        public static double pi = 3.14;

        public static int doubro(int n)
        {
            return n*2;
        }
    }

    class aula49
    {
        static void Main()
        {
            double vpi = Mat.pi;
            int num = 10;

            Console.WriteLine(Mat.doubro(num));
            Console.WriteLine(vpi);
        }
    }

}