using System; 

namespace Aula11
{

    class aula11
    {
        static void Main()
        {
            int n1 = 10;
            float n2 = n1;  //conversão implícita de int para float
            // ja o contrario n se aplica float para int
            // conversão explicita
            float f1 = 5.5f;
            int f2 = (int)f1; // conversão de type cast
            

            Console.WriteLine("{0}\n{1}",n2,f2);

        }
    }

}