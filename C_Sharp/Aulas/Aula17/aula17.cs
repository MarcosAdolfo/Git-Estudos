using System;

namespace Aula17
{

    class aula17
    {
        static void Main()
        {
            int[] n = new int[5];
            int[] num = new int[3]{55,77,99};
            int[] nn = {11,22,33};

            n[0] = 111;
            n[1] = 222;
            n[2] = 333;
            n[3] = 444;
            n[4] = 555;

            Console.WriteLine("{0}\n{1}\n{2}",n[0],num[2],nn[1]);
        }
    }

}