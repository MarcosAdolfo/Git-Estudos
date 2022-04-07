using System; 

namespace Aula19
{

    class aula19
    {
        static void Main()
        {
            int[] n = new int[10];

            for(int num=0; num<n.Length; num++)
            {
                n[num]=0;
                Console.WriteLine("Olá - {0}",num);
            }

            for(int i = 0; i < 10; i++)
            {
                Console.WriteLine(n[i]);
            }
        }
    }

}