using System; 

namespace Aula09
{

    class aula09
    {
        static void Main()
        {
            //Bitwise (>> e <<) opera no código binario
            int num1=10,num2=10,num3=10;
            num1=num1<<1; //dobra
            num2=num2>>1; //metade
            num3=num3<<2; //dobra 2x
            Console.WriteLine("{0}\n{1}\n{2}",num1,num2,num3);
        }
    }

}
