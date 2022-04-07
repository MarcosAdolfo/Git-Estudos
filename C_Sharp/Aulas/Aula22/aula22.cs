using System;

namespace Aula22
{

    class aula22
    {
        static void Main()
        {
            int[] num = new int[3]{11,12,13};

            for(int i = 0; i < num.Length; i++)
            {
                Console.WriteLine(num[i]);
            }

            foreach(int n in num)
            {
                Console.WriteLine(n);
            }
        }
    }

}